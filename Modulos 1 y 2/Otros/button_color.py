import tkinter as tk


window = tk.Tk()
button = tk.Button(window, text="Button #1", bg="red", fg="yellow")
button.pack()
window.mainloop()


window = tk.Tk()
button = tk.Button(
    window,
    text="Button #1",
    bg="MediumPurple",
    fg="LightSalmon",
    activeforeground="LavenderBlush",
    activebackground="HotPink",
)
button.pack()
window.mainloop()


# Igual al anterior pero con colores en hexadecimnal.
window = tk.Tk()
button = tk.Button(
    window,
    text="Button #1",
    bg="#9370DB",
    fg="#FFA07A",
    activeforeground="#FFF0F5",
    activebackground="#FF69B4",
)
button.pack()
window.mainloop()
