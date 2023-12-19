import tkinter as tk

window = tk.Tk()
canvas = tk.Canvas(window, width=400, height=400, bg="blue")
canvas.create_text(
    200,
    200,
    text="Mary\nhad\na\nlittle\nlamb",
    font=("Arial", "40", "bold"),
    justify=tk.CENTER,
    fill="white",
)
button = tk.Button(window, text="Quit", command=window.destroy)
canvas.grid(row=0)
button.grid(row=1)
window.mainloop()
