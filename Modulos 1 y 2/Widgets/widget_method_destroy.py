import tkinter as tk

time_counter = "5"


def timer():
    global time_counter
    time_counter = str(int(time_counter) - 1)
    label.config(text=time_counter)
    label.after(1000, timer)


def suicide():
    frame.destroy()


window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg="green")
button = tk.Button(frame, text="I'm a frame's child")
button.place(x=10, y=10)
label = tk.Label(frame, text=time_counter, font=("Arial", "16", "bold"), bg="green")
label.place(x=150, y=10)
label.after(1000, timer)
frame.after(5000, suicide)
frame.pack()
window.mainloop()
