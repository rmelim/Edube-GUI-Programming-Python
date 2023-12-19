"""
pocket_calc.py -- Elaborado por Rui Duarte dos Santos Melim.

Escenario:
¿Alguna vez has usado una calculadora de bolsillo común? 
Preferimos preguntarte primero, ya que somos conscientes de que estos 
dispositivos pasaron de moda hace algún tiempo y fueron reemplazados 
por aplicaciones de computadoras y teléfonos inteligentes.

Esto es exactamente lo que queremos que aquí se implementa: una 
calculadora de "bolsillo" simple de cuatro funciones. Se puede equipar 
con muchas funciones adicionales, pero sumar, restar, multiplicar y dividir 
es imprescindible: no hay calculadora sin estas operaciones.

Además, la calculadora necesita una función de signo de cambio, un botón de 
punto decimal y el botón de borrar. No es necesario mencionar que la calculadora 
debe ser resistente a los intentos de división cero, en cuyo caso debería mostrar 
un mensaje de error en lugar de producir un resultado no deseado o generar una 
excepción.

Las imágenes de pantallas que están dentro de sta misma carpeta son solo una sugerencia. 
Puede diseñar la interfaz de usuario de una manera diferente, y será buena siempre que 
su calculadora funcione correctamente. No podemos recopilar todos los requisitos estrictos 
en un solo lugar, solo podemos decir que cada vez que tenga dudas sobre cómo implementar 
un comportamiento en particular, simplemente debe tomar una calculadora de bolsillo real y 
verificar cómo funciona en el contexto específico.

Estas son algunas de nuestras suposiciones:
1.- Responder solo a los clics del ratón; las pulsaciones del teclado se pueden ignorar 
silenciosamente.
2.- El ancho de la pantalla es 10 - use una fuente de ancho fijo para trabajar con ella.
3.- No se le permite llenar la pantalla con más de 10 caracteres (incluido el punto decimal 
y el signo menos si es necesario); Si el resultado necesita que se presenten más caracteres, 
debe mostrar un mensaje de error.
4.- Se le permite eliminar algunos dígitos menos significativos ubicados después del punto 
decimal para acortar el resultado en efecto.
5.- Si el resultado no tiene dígitos significativos después del punto decimal, el punto no 
debería aparecer en la pantalla.
"""

import tkinter as tk


def _create_buttons(count, form, event, width, height, text):
    """
    Crea los botones necesarios para la calculadora.

    Arguments:
        count -- Cantidad de botones a crear.
        form -- Objeto ventana que contienea la calculadora.
        event -- Método ligado al evento Click del botón.
        width -- Ancho del botón.
        height -- Altura del botón.
        text -- Lista que contine el valor del atributo text de cada botón.

    Returns:
        Retorna una lista con los objetos tipo Button requeridos.
    """
    buttons = []
    for i in range(count):
        buttons.append(tk.Button(form, text=text[i], width=width, height=height))
        buttons[i].bind("<Button-1>", event)
    return buttons


def _adjust_decimals(value):
    """
    Ajusta la parte decimal, si existe, de manera que el resultado no sea
    un numero de más de 10 dígitos incluyendo signo y/o punto decimal.

    Arguments:
        value -- Valor de tipo float a evaluar

    Returns:
        El número ya formateado.
    """
    if value.is_integer():
        return str(int(value))
    if len(str(value)) > 10:
        len_decimals = 10 - len(str(int(value))) - 1
        if len_decimals <= 0:
            return str(int(value))
        return str(int(value) + round((value % 1), len_decimals))
    return str(value)


def _eval_expression(expression):
    """
    Evalua la operación aritmética indicada en la Calculadora.

    Arguments:
        expression -- Expresión aritmética a evaluar.

    Returns:
        Resultado de la operación aritmética dada según expression.
    """
    try:
        result = eval(expression)
    except ZeroDivisionError:
        return "Error!"
    result = str(result)
    if "." in result:
        result = _adjust_decimals(float(result))
    if len(result) > 10:
        return "Error!"
    return result


class Calculator:
    """Clase para instanciar un objeto Calculadora."""

    def __init__(self, w_=6, h_=3):
        # Ventana de la calculadora.
        self.__calc = tk.Tk()
        # Variable observable y pantalla de la calculadora.
        self.__value = tk.StringVar(value="0")
        self.__display = tk.Entry(
            self.__calc,
            textvariable=self.__value,
            font=("Consolas", "16", "bold"),  # font=("Curier", "16", "bold"),
            justify=tk.RIGHT,
            state="readonly",
            width=10,
        )
        # Botones con los números.
        self.__numbers_key = _create_buttons(
            10, self.__calc, self.__click_number, w_, h_, [str(i) for i in range(10)]
        )
        # Botón con el punto decimal.
        self.__decimal_key = _create_buttons(1, self.__calc, self.__click_decimal, w_, h_, ["."])
        # Botones con las operaciones aritméticas.
        self.__opers_key = _create_buttons(
            4, self.__calc, self.__click_operator, w_, h_, ["+", "-", "*", "/"]
        )
        # Botón de igualdad.
        self.__equal_key = _create_buttons(1, self.__calc, self.__click_equal, w_, h_ + 4, ["="])
        # Botón para alternar entre positivo y negativo.
        self.__pos_neg_key = _create_buttons(1, self.__calc, self.__click_pos_neg, w_, h_, ["+/-"])
        # Botón para borrar.
        self.__clear_key = _create_buttons(1, self.__calc, self.__click_clear, w_, h_ + 4, ["C"])
        # Variables varias de operación.
        self.__decimal_switch = False
        self.__oper_switch = False
        self.__expression = ""

    def __construct_calc(self):
        self.__calc.title("Calculadora")
        self.__calc.resizable(width=False, height=False)
        self.__calc.config(borderwidth=5)
        self.__display.grid(row=0, column=0, columnspan=5, sticky=tk.NSEW)
        for i in range(9, 0, -1):
            self.__numbers_key[i].grid(row=(9 - i) // 3 + 1, column=(i - 1) % 3, sticky=tk.NSEW)
        self.__pos_neg_key[0].grid(row=4, column=0, sticky=tk.NSEW)
        self.__numbers_key[0].grid(row=4, column=1, sticky=tk.NSEW)
        self.__decimal_key[0].grid(row=4, column=2, sticky=tk.NSEW)
        for i in range(4):
            self.__opers_key[i].grid(row=i + 1, column=3, sticky=tk.NSEW)
        self.__clear_key[0].grid(row=1, column=4, rowspan=2, sticky=tk.NSEW)
        self.__equal_key[0].grid(row=3, column=4, rowspan=2, sticky=tk.NSEW)

    def __click_number(self, ev=None):
        if self.__value.get() != "Error!":  # Verifica que no exista mensaje de Error en pantalla.
            if self.__value.get() == "0" or self.__oper_switch:  # Se inicia un número nuevo.
                self.__value.set("")
                self.__decimal_switch = False
                self.__oper_switch = False
            # Asegura que no se escriba un número de más de 10 de longitud incluyendo signo.
            if len(self.__value.get()) < 10:
                self.__value.set(self.__value.get() + ev.widget["text"])

    def __click_decimal(self, ev=None):
        # Asegura que no exista mensaje de Error en pantalla y que no se
        # escriba un número de más de 10 de longitud incluyendo signo y
        # punto decimal.
        if self.__value.get() != "Error!" and len(self.__value.get()) < 10:
            if not self.__decimal_switch:  # Pone el punto decimal si no se ha usado antes.
                self.__value.set(self.__value.get() + ".")
                self.__decimal_switch = True

    def __click_pos_neg(self, ev=None):
        # Asegura que no exista mensaje de Error o un 0 en pantalla y que
        # no se escriba un número de más de 10 de longitud incluyendo signo
        # y punto decimal.
        if (
            self.__value.get() != "Error!"
            and self.__value.get() != "0"
            and len(self.__value.get()) < 10
        ):
            value = float(self.__value.get())
            self.__value.set(_adjust_decimals(value * -1))

    def __click_operator(self, ev=None):
        if self.__value.get() != "Error!" and self.__value.get() != "0":
            if not self.__oper_switch:
                self.__value.set(_eval_expression(self.__expression + self.__value.get()))
                self.__expression = self.__value.get() + ev.widget["text"]
                self.__oper_switch = True
            else:
                self.__expression = self.__expression[:-1] + ev.widget["text"]

    def __click_equal(self, ev=None):
        if self.__value.get() != "Error!":
            if self.__oper_switch:
                self.__expression = self.__expression[:-1]
            self.__value.set(_eval_expression(self.__expression + self.__value.get()))
            self.__expression = ""
            self.__decimal_switch = False
            self.__oper_switch = False

    def __click_clear(self, ev=None):
        self.__value.set("0")
        self.__decimal_switch = False
        self.__oper_switch = False
        self.__expression = ""

    def execute(self):
        self.__construct_calc()
        self.__calc.mainloop()


calc = Calculator()
calc.execute()
