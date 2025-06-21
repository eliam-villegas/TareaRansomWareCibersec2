import os
import ctypes

def obtener_fondo_actual():
    # Lee el fondo actual en Windows
    SPI_GETDESKWALLPAPER = 0x0073
    buffer = ctypes.create_unicode_buffer(512)
    ctypes.windll.user32.SystemParametersInfoW(SPI_GETDESKWALLPAPER, 512, buffer, 0)
    return buffer.value

def cambiar_fondo_de_pantalla(ruta_imagen):
    resultado = ctypes.windll.user32.SystemParametersInfoW(20, 0, ruta_imagen, 3)
    return resultado
