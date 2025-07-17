import tkinter as tk
from tkinter import messagebox
from UMF import mover_informes  # asumimos que tenés esa función aparte

def ejecutar():
    mover_informes()
    messagebox.showinfo("Listo", "Los informes fueron movidos.")

root = tk.Tk()
root.title("Organizador de Informes")
root.geometry("300x100")

boton = tk.Button(root, text="Mover Informes", command=ejecutar)
boton.pack(expand=True)

root.mainloop()