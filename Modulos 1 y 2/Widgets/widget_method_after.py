import tkinter as tk

is_white = True


def blink():
    global is_white
    if is_white:
        color = "black"
    else:
        color = "white"
    is_white = not is_white
    frame.config(bg=color)
    frame.after(500, blink)


window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg="white")
frame.after(500, blink)
frame.pack()
window.mainloop()
