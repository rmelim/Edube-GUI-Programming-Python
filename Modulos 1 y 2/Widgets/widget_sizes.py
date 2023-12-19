import tkinter as tk


window = tk.Tk()

button_1 = tk.Button(window, text="Ordinary button")
button_1.pack()

button_2 = tk.Button(window, text="Exceptional button")
button_2.pack()

# El ancho del fotograma 3D que rodea algunos widgets.
button_2["borderwidth"] = 10

# La anchura del fotograma adicional dibujado alrededor
# del widget cuando obtiene el foco.
button_2["highlightthickness"] = 10

# La anchura/altura de un espacio/margen vacío adicional
# alrededor del widget.
button_2["padx"] = 10
button_2["pady"] = 5

# El índice del carácter dentro del texto del widget, que
# debe presentarse como subrayado o de otra manera -1
# (la letra/dígito subrayado se puede usar como tecla de
# acceso directo, pero necesita una devolución de llamada
# especializada para funcionar).
button_2["underline"] = 1

window.mainloop()
