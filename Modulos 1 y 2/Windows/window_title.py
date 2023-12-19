import tkinter as tk

counter = 10


def click(*args):
    global counter
    if counter > 0:
        counter -= 1
    window.title(str(counter))


window = tk.Tk()
window.title(str(counter))
window.bind("<Button-1>", click)
window.mainloop()
