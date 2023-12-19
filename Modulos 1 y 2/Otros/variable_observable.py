import tkinter as tk


def r_observer(*args):
    print("Reading")


def w_observer(*args):
    print("Writing")


dummy = tk.Tk()  # Nececitamos esto aunque no mostraremos ninguna ventana
variable = tk.StringVar()
variable.set("abc")
r_obsid = variable.trace("r", r_observer)
w_obsid = variable.trace("w", w_observer)
variable.set(variable.get() + "d")  # lectura seguida de escritura
variable.trace_vdelete("r", r_obsid)
variable.set(variable.get() + "e")
variable.trace_vdelete("w", w_obsid)
variable.set(variable.get() + "f")
print(variable.get())
