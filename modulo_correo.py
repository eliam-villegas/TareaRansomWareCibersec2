from enviar_correo import enviar_contrasena
from dotenv import load_dotenv
import os

load_dotenv()

REMITENTE = os.getenv("CORREO_REMITENTE")
CLAVE_APP = os.getenv("CLAVE_APP")

def enviar_clave(destinatario, contrasena):
    return enviar_contrasena(destinatario, contrasena, REMITENTE, CLAVE_APP)
