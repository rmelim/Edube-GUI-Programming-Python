import tkinter as tk
from tkinter import messagebox


"""
**********************************************************
Ejemplo showinfo  y un par de objetos que manejan eventos.
**********************************************************
"""


def clicked():
    messagebox.showinfo("info", "some\ninfo")


window = tk.Tk()
button_1 = tk.Button(window, text="Show info", command=clicked)
button_1.pack()
button_2 = tk.Button(window, text="Quit", command=window.destroy)
button_2.pack()
window.mainloop()


"""
*********************************************************************
Ejemplo objetos que manejan eventos y objetos que no manejan eventos.
*********************************************************************
"""


def click():
    tk.messagebox.showinfo("Click!", "I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.pack()

button = tk.Button(window, text="Button", command=click)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.pack()

window.mainloop()

"""
*********************************************************************
Ejemplo de objetos que son clickeables y objetos que no lo son y como
debe manejarse sus eventos.

Ver lo declarado en Line I y Line II.
*********************************************************************
"""


def click_event(event=None):
    tk.messagebox.showinfo("Click!", "I love clicks!")


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click_event)  # Line I
label.pack()

button = tk.Button(window, text="Button", command=click_event)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click_event)  # Line II
frame.pack()

window.mainloop()


"""
*********************************************************************
Ejemplo en donde se  observa el uso del objeto Event (creado al hacer
"bind" a un objeto no clickeable) y como se puede extrear información
de él.
*********************************************************************
"""


def click_ev(event=None):
    if event is None:
        tk.messagebox.showinfo("Click!", "I love clicks!")
    else:
        string = f"x={str(event.x)},y={str(event.y)},num={str(event.num)},type={event.type}"
        tk.messagebox.showinfo("Click!", string)


window = tk.Tk()
label = tk.Label(window, text="Label")
label.bind("<Button-1>", click_ev)
label.pack()

button = tk.Button(window, text="Button", command=click_ev)
button.pack(fill=tk.X)

frame = tk.Frame(window, height=30, width=100, bg="#55BF40")
frame.bind("<Button-1>", click_ev)
frame.pack()

window.mainloop()


"""
***********************************************************************
Ejemplo en donde se observa como se puede "desunir" la función para
un Event, unida por el método bind() del objeto, y volverla a unir
con el objeto Event.

Aquí se crea una ventana con dos botones.

El primero funciona como un interruptor de encendido/apagado;
cambiando el comportamiento del segundo botón.

Cuando el interruptor está encendido, al hacer clic en el segundo botón
se activa un cuadro de mensaje.

Cuando el interruptor está apagado, hacer clic en el segundo botón no
tiene ningún efecto, además que el título del mismo cambia según su
estado.
***********************************************************************
"""

switch = True


def on_off():
    global switch
    if switch:
        button_2.config(command=lambda: None)
        button_2.config(text="Gee!")
    else:
        button_2.config(command=peekaboo)
        button_2.config(text="Peekaboo!")
    switch = not switch


def peekaboo():
    messagebox.showinfo("", "PEEKABOO!")


def do_nothing():
    pass


window = tk.Tk()
buton_1 = tk.Button(window, text="On/Off", command=on_off)
buton_1.pack()
button_2 = tk.Button(window, text="Peekaboo!", command=peekaboo)
button_2.pack()
window.mainloop()


"""
***********************************************************************
Ejemplo en donde se nota el uso del método unbind() ql cual "desune" un
"callback" del objeto Event y como volver a unirlo.    
***********************************************************************
"""

switch = True
words = ["Old", "McDonald", "Had", "A", "Farm"]
word_no = 0


def on_off_label():
    global switch
    if switch:
        label.unbind("<Button-1>")
    else:
        label.bind("<Button-1>", rhyme)
    switch = not switch


def rhyme(dummy):
    global word_no, words
    word_no += 1
    label.config(text=words[word_no % len(words)])


window = tk.Tk()
button = tk.Button(window, text="On/Off", command=on_off_label)
button.pack()
label = tk.Label(window, text=words[0])
label.bind("<Button-1>", rhyme)
label.pack()
window.mainloop()


"""
***********************************************************************
Ejemplo en donde se ve le unso del método bind_all() del objeto window.

Este método une todos los widgets del window a un objeto Event. Para 
desunirlos, se utilizaría el método unbind_all().
***********************************************************************
"""


def hello(dummy):
    messagebox.showinfo("", "Hello!")


window = tk.Tk()
button = tk.Button(window, text="On/Off")
button.pack()
label = tk.Label(window, text="Label")
label.pack()
frame = tk.Frame(window, bg="yellow", width=100, height=20)
frame.pack()
window.bind_all("<Button-1>", hello)
window.mainloop()
