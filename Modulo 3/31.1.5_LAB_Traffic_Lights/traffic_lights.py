"""
traffic_lights.py -- Elaborado por Rui Duarte dos Santos Melim.

Escenario:
L tupla que consta de cuatro tuplas de tres elementos es un conjunto de
reglas que describen el comportamiento de los semáforos de estilo británico. 

Supongamos que el primer elemento de todas las tuplas internas se asigna a 
la luz roja, el segundo, a la amarilla y el tercero, a la verde. 

Verdadero significa que la luz está encendida, Falso - apagado.

Como ves, hay cuatro fases diferentes:
1.- Se enciende la luz roja.
2.- las luces rojas y amarillas se encienden juntas.
3.- Se enciende la luz verde.
4.- Se enciende la luz amarilla.

La tarea es implementar un modelo que muestre cómo funciona una señal de tráfico 
de este tipo. El modelo debe tener el siguiente aspecto mostrado en la imagen que
está dentro de esta misma carpeta (traffic_lights.png)

Como puede ver, el modelo se compone de tres widgets:

1.- El lienzo (Canvas) es un fondo para las tres luces.
2.- El botón (Buton) llamado "Siguiente". Al hacer clic en él, la señal pasa a la 
siguiente fase.
3.- El botón (Button) llamado "Salir". Al hacer clic en él, se sale inmediatamente 
del programa.

Nota:
Use la tupla de fases como una "base de conocimiento" para todo el código. El código 
tiene que adaptarse a cualquier cambio realizado en la tupla, por ejemplo, puede haber 
más o menos de cuatro fases y las combinaciones de las luces también pueden ser diferentes.
"""

from tkinter import Tk, Button, Canvas


phases = (
    (True, False, False),
    (True, True, False),
    (False, False, True),
    (False, True, False),
)


def light_next():
    state = int(trafic_lights.getvar("states"))
    lights.create_oval(
        10,
        5,
        110,
        105,
        outline="black",
        width=2,
        fill="red" if phases[state % 4][0] else "grey",
    )
    lights.create_oval(
        10,
        110,
        110,
        210,
        outline="black",
        width=2,
        fill="yellow" if phases[state % 4][1] else "grey",
    )
    lights.create_oval(
        10,
        215,
        110,
        320,
        outline="black",
        width=2,
        fill="green" if phases[state % 4][2] else "grey",
    )
    state += 1
    trafic_lights.setvar("states", str(state))


trafic_lights = Tk()
trafic_lights.setvar("states", "0")
trafic_lights.resizable(width=False, height=False)

lights = Canvas(trafic_lights, height=325, width=120, bg="grey")
lights.grid(row=0, column=0, columnspan=3)
light_next()

next_light = Button(trafic_lights, text="Next", command=light_next)
next_light.grid(row=1, column=1)

quit_light = Button(trafic_lights, text="Quit", command=trafic_lights.destroy)
quit_light.grid(row=2, column=1)

trafic_lights.mainloop()
