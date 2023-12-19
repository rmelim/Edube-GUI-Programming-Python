"""
tic_tac_toe.py Elaborado por Rui Duarte dos Santos Melim.

Escenario:
Programa GUI simple que pretenda jugar al tres en raya (Tic-Tac-Toe) con 
el usuario. Sin algoritmos de inteligencia artificial. (Puede hacerce si 
realmente quieres crear un competidor real).

Así es como se ve el juego en el principio y el final del mismo (ver imágens 
dentro de esta misma carpeta).

Para facilitar la tarea, vamos a simplificar un poco el juego. Estas son nuestras
suposiciones:

1.- la computadora (es decir, su programa) reproduce 'X', y las X siempre son rojas.
2.- El usuario (por ejemplo, usted) juega 'O', y las O siempre son verdes.
3.- El tablero consta de 9 fichas, y el papel de ficha lo desempeña un botón (Button)
4.- El primer movimiento pertenece a la computadora. Siempre pone su primera 'X' en 
el centro del tablero.
5.- El usuario ingresa su movimiento haciendo clic en la ficha elegida (hacer clic en 
las fichas que no están libres es ineficaz).
6.- El programa comprueba si se cumplen las condiciones de fin del juego, y si el juego 
ha terminado, se muestra un cuadro de mensaje que anuncia el ganador, de lo contrario, 
el ordenador responde con su movimiento y se repite la comprobación.

Nota:
Se utiliza "random" para generar los movimientos de la computadora.
"""


import tkinter as tk
from tkinter import messagebox
from random import randrange


class TicTacToe:
    def __init__(self):
        self.__wnd = tk.Tk()
        self.__wnd.title("TicTacToe")
        self.__wnd.resizable(width=False, height=False)
        self.__tiles = self.__create_tiles__()
        self.__move = 1

    def __create_tiles__(self):
        buttons = []
        for i in range(9):
            buttons.append(
                tk.Button(self.__wnd, width=4, height=2, font=("Helvetica", "20", "bold"), fg="red")
            )
            buttons[i].grid(row=i // 3, column=i % 3)
            buttons[i]["text"] = "" if i != 4 else "X"
            if i != 4:
                buttons[i].bind("<Button-1>", self.__click__)
        return buttons

    def __victory__(self, sign):
        # Si hay menos de 5 movimientos, no evalua nada.
        if self.__move >= 5:
            # Evalua las filas.
            #
            for i in [0, 3, 6]:
                if (
                    self.__tiles[i]["text"]
                    == self.__tiles[i + 1]["text"]
                    == self.__tiles[i + 2]["text"]
                    == sign
                ):
                    return True
            # Evalua las columnas.
            #
            for i in [0, 1, 2]:
                if (
                    self.__tiles[i]["text"]
                    == self.__tiles[i + 3]["text"]
                    == self.__tiles[i + 6]["text"]
                    == sign
                ):
                    return True
            # Evalua las diagonales.
            #
            if (
                self.__tiles[0]["text"]
                == self.__tiles[4]["text"]
                == self.__tiles[8]["text"]
                == sign
                or self.__tiles[2]["text"]
                == self.__tiles[4]["text"]
                == self.__tiles[6]["text"]
                == sign
            ):
                return True
        # End of method.
        return False

    def __play_machine__(self):
        tile = 4
        while self.__tiles[tile]["text"] in ("X", "O"):
            tile = randrange(9) - 1
        self.__tiles[tile]["text"] = "X"
        self.__tiles[tile].unbind("<Button-1>")
        self.__move += 1
        if self.__victory__("X"):
            messagebox.showinfo("Game Over", "I Win!")
            self.__wnd.destroy()

    def __click__(self, ev=None):
        ev.widget["fg"] = "green"
        ev.widget["text"] = "O"
        ev.widget.unbind("<Button-1>")
        self.__move += 1
        if self.__victory__("O"):
            messagebox.showinfo("Game Over", "You Win!")
            self.__wnd.destroy()
        else:
            self.__play_machine__()

    def start(self):
        self.__wnd.mainloop()


game = TicTacToe()
game.start()
