import tkinter as tk
from tkinter import messagebox


def question_yes_no():
    answer = messagebox.askyesno("?", "To be or not to be?")
    print(answer)


window = tk.Tk()
window.title("Ask yes no")
window.resizable(width=False, height=False)
window.geometry("300x30")
button = tk.Button(window, text="Ask the question!", command=question_yes_no)
button.pack()
window.mainloop()


def question_ok_cancel():
    answer = messagebox.askokcancel("?", "I'm going to format your hard drive")
    print(answer)


window = tk.Tk()
window.title("Ask ok cancel")
window.resizable(width=False, height=False)
window.geometry("300x30")
button = tk.Button(window, text="What are your plans?", command=question_ok_cancel)
button.pack()
window.mainloop()


def question_retry_cancel():
    answer = messagebox.askretrycancel("?", "I'm going to format your hard drive")
    print(answer)


window = tk.Tk()
window.title("Ask retry cancel")
window.resizable(width=False, height=False)
window.geometry("300x30")
button = tk.Button(window, text="What are your plans?", command=question_retry_cancel)
button.pack()
window.mainloop()


def question():
    answer = messagebox.askquestion("?", "I'm going to format your hard drive")
    print(answer)


window = tk.Tk()
window.title("Ask question")
window.resizable(width=False, height=False)
window.geometry("300x30")
button = tk.Button(window, text="What are your plans?", command=question)
button.pack()
window.mainloop()


def question_error():
    answer = messagebox.showerror("!", "Your code does nothing!")
    print(answer)


window = tk.Tk()
window.title("Show error")
window.resizable(width=False, height=False)
window.geometry("300x30")
button = tk.Button(window, text="Alarming message", command=question_error)
button.pack()
window.mainloop()


def question_warning():
    answer = messagebox.showwarning("Be careful!", "Big Brother is watching you!")
    print(answer)


window = tk.Tk()
window.title("Show warning")
window.resizable(width=False, height=False)
window.geometry("300x30")
button = tk.Button(window, text="What's going on?", command=question_warning)
button.pack()
window.mainloop()
