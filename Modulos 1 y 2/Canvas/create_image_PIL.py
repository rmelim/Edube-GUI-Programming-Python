import tkinter as tk

# Para usar archívos de imagen .JPG hay que utilizar el módulo PIL
# y sus respectivas clases Image e ImageTk.
#
# Se puede instalar con: pip install pillow
from PIL import Image, ImageTk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="red")
jpg = Image.open("logo.jpg")
image = ImageTk.PhotoImage(jpg)
canvas.create_image(200, 200, image=image)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
