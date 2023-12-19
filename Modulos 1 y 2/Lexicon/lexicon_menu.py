import tkinter as tk
from tkinter import messagebox


def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")


def are_you_sure(event=None):
    if messagebox.askyesno("", "Are you sure you want to quit the App?"):
        window.destroy()


def open_file():
    messagebox.showinfo("Open doc", "We'll open a file here...")


window = tk.Tk()

main_menu = tk.Menu(window)  # Crea el menú principal.
window.config(menu=main_menu)  # Lo asigna a la ventana.

# Crea el sub-menú File ligado al principal.
sub_menu_file = tk.Menu(main_menu, tearoff=0)

# Añade el sub-menú File como un sub-menú a su vez.
# La propiedad "underline" indica la tecla Alt-hotkey.
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)

# Añade una opción al sub-menú File.
sub_menu_file.add_command(label="Open...", underline=0, command=open_file)

# Crea un sub-menú dentro del sub-menú File y se añada como otyro sub-menú.
sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open recent file...", underline=5, menu=sub_sub_menu_file)

for i in range(8):  # Crea una simulación para el sub-menú de archivos recientes.
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". file.txt", underline=0)

sub_menu_file.add_separator()  # Añade un separador.

# Se agrega una opción adicional al sub-menú File, ligado a la función (callback) "are_you_sure".
# Se utiliza la propiedad "accelerator" para indicar un shortcut. Esto sólo lo muestra no lo
# liga al callback respectivo.
sub_menu_file.add_command(label="Quit", accelerator="Ctrl-Q", underline=0, command=are_you_sure)
sub_menu_help = tk.Menu(main_menu)

main_menu.add_command(label="About...", command=about_app, underline=1)

# Se liga el shortcut Ctrl-Q a la función "are_you_sure".
window.bind_all("<Control-q>", are_you_sure)

window.mainloop()
