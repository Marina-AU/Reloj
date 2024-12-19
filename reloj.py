# Importando librerias

from tkinter import *
from tkinter.ttk import *
from time import strftime

#Función actualizar reloj

def actualizar_reloj():
    etiqueta_hm.config(text=strftime ("%H:%M"))
    etiqueta_s.config(text=strftime ("%S"))
    etiqueta_fecha.config(text=strftime ("%A, %d/%m/%Y"))
    etiqueta_s.after(1000, actualizar_reloj)

#Creando ventana

app = Tk()
app.title("Reloj Dijital")
app.config(background="black")

#Etiquetas de horas, minutos y segundos

frame_hora = Frame()
frame_hora.pack()
etiqueta_hm = Label(frame_hora, font=("digital-7", 100), foreground="cyan", background="black", text="H:M")
etiqueta_hm.grid(row=0, column=0)

etiqueta_s = Label(frame_hora, font=("digital-7", 50), foreground="cyan", background="black", text="s")
etiqueta_s.grid(row=0, column=1, sticky="n")

#Etiqueta de fecha y su ubicación

etiqueta_fecha = Label(app, font=("digital-7", 50), foreground="cyan", background="black", text="día d/m/aaaa")
etiqueta_fecha.pack(anchor="center")

#Efecto de brillo

brillo = Label(app, background="white", foreground="white", text="", font=("digital-7", 100))
brillo.place(x=etiqueta_hm.winfo_x(), y=etiqueta_hm.winfo_y())
brillo.after(500, lambda: brillo.place_forget())

#Mostrando ventana y llamar reloj

actualizar_reloj()

app.mainloop()