import tkinter as tk

message = "Quick brown fox jumps over the lazy dog"
window = tk.Tk()
label_1 = tk.Label(window, text=message)
label_1.grid(column=0, row=0)
label_2 = tk.Label(window, text=message, font=("Times", "12"))
label_2.grid(column=0, row=1)
label_3 = tk.Label(window, text=message, font=("Arial", "16", "bold"))
label_3.grid(column=0, row=2)
window.mainloop()
