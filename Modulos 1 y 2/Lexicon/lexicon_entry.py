import tkinter as tk

# Aquí sin necesidad de utilizar una variable Global
# def digits_only(*args):
#     string = text.get()
#     if (
#         len(string) > 5 or string == "" or not string[len(string) - 1].isdigit()
#     ):  # Field's content is valid.
#         text.set(string[: len(string) - 1])

last_string = ""


def digits_only(*args):
    global last_string
    string = text.get()
    if len(string) <= 5 and (string == "" or string.isdigit()):  # Field's content is valid.
        last_string = string
    else:
        text.set(last_string)


window = tk.Tk()
text = tk.StringVar()
entry = tk.Entry(window, textvariable=text, width=6)
text.set(last_string)
text.trace("w", digits_only)
entry.pack()
entry.focus_set()
window.mainloop()
