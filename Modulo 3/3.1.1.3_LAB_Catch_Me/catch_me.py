"""
catch_me.py -- Elaborado por Rui Duarte dos Santos Melim

Escenario:
Un juego simple, un juego infinito que los humanos no pueden ganar.

Estas son las reglas:
* El juego continúa entre TkInter y el usuario (probablemente tú)
* TkInter abre una ventana de 500x500 píxeles y coloca un botón que dice 
"¡Atrápame!" en la esquina superior izquierda de la ventana.
* Si el usuario mueve el cursor del mouse sobre el botón, el botón salta 
inmediatamente a otra ubicación dentro de la ventana; debe asegurarse de 
que la nueva ubicación esté lo suficientemente distante como para evitar 
que el usuario haga un clic instantáneo,
* ¡El botón no debe cruzar los límites de la ventana durante el salto!

Ver la imagen de muestra para su referencia dentro de esta misma carpeta.

Utilice el método place() para mover el botón y el método bind() para asignar 
su propia devolución de llamada.
"""

import tkinter as tk
from tkinter import messagebox
import random as rnd


def catched():
    messagebox.showinfo("Fin del Juego", "Te felicito. ¡Me has atrapado!")


def mouseover(ev=None):
    x = rnd.randint(1, 500) - btn_catch.winfo_reqwidth()
    x = 1 if x < 1 else x

    y = rnd.randint(1, 500) - btn_catch.winfo_reqheight()
    y = 1 if y < 1 else y

    btn_catch.place(x=x, y=y)


window = tk.Tk()
window.resizable(width=False, height=False)
window.title("Catch me if you can!")
window.geometry("500x500")

btn_catch = tk.Button(window, text="¡Atrápame!", command=catched)
btn_catch.place(x=10, y=10)
btn_catch.bind("<Enter>", mouseover)

window.mainloop()
