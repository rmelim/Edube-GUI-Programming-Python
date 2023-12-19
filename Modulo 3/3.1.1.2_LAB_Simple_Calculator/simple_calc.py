"""º
simple_calc.py -- Creado por Rui Durte dos Santos Melim

Escenario:
Crea una calculadora. Una calculadora muy sencilla y muy específica. 
Mire la imagen contenida en esta misma carpeta (calc.png).

Contiene dos campos que el usuario puede usar para ingresar argumentos, 
un botón de opción para seleccionar la operación a realizar y un botón 
para iniciar la evaluación.

Esperamos que la calculadora se comporte de la siguiente manera:
1.- Si ambos campos contienen números válidos (enteros o flotantes), al 
hacer clic en el botón Evaluar debería aparecer una ventana de información 
que muestre el resultado de la evaluación.
2.- Si alguno de los campos contiene datos no válidos (por ejemplo, una 
cadena o un campo está vacío), al hacer clic en el botón Evaluar debería 
aparecer una ventana de error que describa el problema y el foco debe moverse 
al campo que causa el problema.

No olvide proteger su código para que no se divida por cero y use el administrador 
de cuadrícula (grid manager) para componer el interior de la ventana.
"""

import tkinter as tk
from tkinter import messagebox as mbox


def evaluate():
    try:
        num_1 = float(var_num_1.get())
    except ValueError:
        num_1 = None

    try:
        num_2 = float(var_num_2.get())
    except ValueError:
        num_2 = None

    if num_1 is None:
        mbox.showerror("Error", "El primer operador no es numérico")
        entry_num_1.focus()
        return None

    if num_2 is None:
        mbox.showerror("Error", "El segundo operador no es numérico")
        entry_num_2.focus()
        return None

    num_1 = float(num_1)
    num_2 = float(num_2)

    match radio_var.get():  # Válido a partir de Pyhon 3.10
        case 1:
            oper = num_1 + num_2
        case 2:
            oper = num_1 - num_2
        case 3:
            oper = num_1 * num_2
        case 4:
            try:
                oper = num_1 / num_2
            except ZeroDivisionError:
                mbox.showerror(
                    "Error", "El segundo operador es cero.\nNo puede realizarse la división."
                )
                entry_num_2.focus()
                return None

    mbox.showinfo("Resultado", str(oper))
    var_num_1.set("")
    var_num_2.set("")
    entry_num_1.focus_set()


calc = tk.Tk()
calc.title("Calculator")

radio_var = tk.IntVar()
radio_add = tk.Radiobutton(calc, text="+", variable=radio_var, value=1)
radio_add.grid(row=0, column=1)
radio_add.select()
radio_rest = tk.Radiobutton(calc, text="-", variable=radio_var, value=2)
radio_rest.grid(row=1, column=1)
radio_mult = tk.Radiobutton(calc, text="*", variable=radio_var, value=3)
radio_mult.grid(row=2, column=1)
radio_div = tk.Radiobutton(calc, text="/", variable=radio_var, value=4)
radio_div.grid(row=3, column=1)

var_num_1 = tk.StringVar()
entry_num_1 = tk.Entry(calc, textvariable=var_num_1)
entry_num_1.grid(row=1, column=0, rowspan=2)
entry_num_1.focus_set()

var_num_2 = tk.StringVar()
entry_num_2 = tk.Entry(calc, textvariable=var_num_2)
entry_num_2.grid(row=1, column=2, rowspan=2)

button_eval = tk.Button(calc, text="Evaluate", command=evaluate)
button_eval.grid(row=4, column=1)

calc.mainloop()
