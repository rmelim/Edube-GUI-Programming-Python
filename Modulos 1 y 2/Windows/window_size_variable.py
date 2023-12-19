import tkinter as tk

size = 100
grows = True


def click(*args):
    global size, grows
    if grows:
        size += 50
        if size >= 500:
            grows = False
    else:
        size -= 50
        if size <= 100:
            grows = True
    window.geometry(str(size) + "x" + str(size))


window = tk.Tk()
window.geometry("100x100")  # Se mide en pixeles geometry("widthxheight")
window.bind("<Button-1>", click)
window.mainloop()
