import tkinter as tk


def on_off_01():
    global button
    state = button["text"]
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button["text"] = state


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off_01)
button.place(x=50, y=100, width=100)
window.mainloop()


def on_off_02():
    global button
    state = button.cget("text")
    if state == "ON":
        state = "OFF"
    else:
        state = "ON"
    button.config(text=state)


window = tk.Tk()
button = tk.Button(window, text="OFF", command=on_off_02)
button.place(x=50, y=100, width=100)
window.mainloop()
