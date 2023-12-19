"""
clicker.py -- Elaborado por Rui Duarte dos Santos Melim.

Escenario:
Juego simple pero desafiante, que pueda ayudar a muchas personas a mejorar 
sus habilidades de percepción y memoria visual. 

Llamaremos al juego The Clicker, ya que hacer clic es lo que esperamos 
del jugador.

El tablero del Clicker consta de 25 botones y cada uno de los botones contiene 
un número aleatorio del rango 1..999. Nota: ¡cada número es diferente!

Debajo del tablero hay un temporizador que inicialmente muestra 0. 

El temporizador se inicia cuando el usuario hace clic en el tablero por primera 
vez.

Para el estado inicial del tablero de The Clicker vea la imagen clicker_inicio.png
que se encuentra dentro de esta misma carpeta.

Esperamos que el jugador haga clic en todos los botones en el orden impuesto por los 
números, desde el más bajo hasta el más alto. Las reglas adicionales son:

1.- El botón en el que se ha hecho clic correctamente cambia el estado del botón a 
DISABLED (atenúa el botón).
2.- El botón en el que se ha hecho clic incorrectamente no muestra ninguna actividad.
3.- El temporizador aumenta su valor cada segundo.
4.- Cuando todos los botones están atenuados, es decir, el jugador ha completado su tarea, 
el temporizador se detiene inmediatamente.

Así es como se ve el tablero cuando termina el juego (ver imagen clicker_final.png).

Sugerencia:
Considere la posibilidad de usar el evento "<Button-1>" en lugar de establecer la propiedad 
"command" del objeto Button, ya que puede simplificar el código.
"""

import tkinter as tk
from random import randint


class Clicker:
    def __init__(self):
        self.__board = tk.Tk()
        self.__board.title("Clicker")
        self.__board.resizable(width=False, height=False)
        self.__numbers = self.__nums_generator__()
        self.__create_buttons__()
        self.__counter = tk.StringVar(value="0")
        self.__timer = tk.Label(self.__board, textvariable=self.__counter)
        self.__timer.grid(row=5, column=2)
        self.__id_job = ""

    def __nums_generator__(self):
        nums = []
        i = 0
        while i < 25:
            num = randint(1, 999)
            while num in nums:
                num = randint(1, 999)
            nums.append(num)
            i += 1
        return nums

    def __create_buttons__(self):
        buttons = []
        for row in range(5):
            buttons.append([])
            for col in range(5):
                buttons[row].append(tk.Button(self.__board, width=10, height=1))
                buttons[row][col].grid(row=row, column=col)
                buttons[row][col].bind("<Button-1>", self.__click__)
                buttons[row][col]["text"] = str(self.__numbers[row * 5 + col])

    def __update_timer__(self):
        self.__counter.set(str(int(self.__counter.get()) + 1))
        self.__id_job = self.__board.after(1000, self.__update_timer__)

    def __click__(self, ev=None):
        if self.__counter.get() == "0":
            self.__update_timer__()
        self.__numbers.sort()
        if int(ev.widget["text"]) == self.__numbers[0]:
            ev.widget.unbind("<Button-1>")
            ev.widget["state"] = tk.DISABLED
            del self.__numbers[0]
        if len(self.__numbers) == 0:
            self.__board.after_cancel(self.__id_job)

    def start(self):
        self.__board.mainloop()


game = Clicker()
game.start()
