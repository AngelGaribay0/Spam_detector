import tkinter as tk
from tkinter import messagebox


def mostrar_mensaje():
    messagebox.showinfo("aviso", "boton precionado")
ventana = tk.Tk()
ventana.title("ventana simple")
label = tk.Label(ventana, text="preciona el boton para ver un mensaje")
label.pack(pady=10)
boton = tk.Button(ventana, text="haz click aqui",command=mostrar_mensaje)
boton.pack(pady=10)

ventana.mainloop()