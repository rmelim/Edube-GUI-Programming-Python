import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="blue")
canvas.create_oval(100, 100, 300, 200, outline="red", width=20, fill="white")
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
