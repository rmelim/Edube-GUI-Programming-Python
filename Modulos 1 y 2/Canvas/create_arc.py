import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="yellow")
canvas.create_arc(10, 100, 380, 300, outline="red", width=5)
canvas.create_arc(
    10, 100, 380, 300, outline="blue", width=5, style=tk.CHORD, start=90, fill="white"
)
canvas.create_arc(10, 100, 380, 300, outline="green", width=5, style=tk.ARC, start=180, extent=180)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
