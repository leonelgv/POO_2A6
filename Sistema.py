# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

# Crea una clase Python para definir el interfaz de usuario de
# la aplicación. Cuando se cree un objeto del tipo 'Aplicacion'
# se ejecutará automáticamente el método __init__() qué
# construye y muestra la ventana con todos sus widgets:

class Aplicacion():

    def __init__(self, window):
        # Initializations
        self.window = window
        #self.window.geometry('320x200')
        self.window.configure(bg = 'white')
        self.window.title('Grupo 2A de Informática')

        # Creating a Frame Container
        frame = LabelFrame(self.window, text= 'Sumar dos números')
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20, padx = 20)

        # Operador1 Input
        Label(frame, text = 'Operador 1: ').grid(row = 1, column = 0)
        self.operador1 = Entry(frame)
        self.operador1.focus()
        self.operador1.grid(row = 1, column = 1)

        # Operador2 Input
        Label(frame, text='Operador 2: ').grid(row=2, column=0)
        self.operador2 = Entry(frame)
        self.operador2.grid(row = 2, column = 1)

        # Resultado Output
        Label(frame, text='Resultado: ').grid(row = 3, column=0)

        # Output Messages
        self.message = Label(frame, text = '', fg = 'red')
        self.message.grid(row = 3, column = 1)

        # Buttons
        ttk.Button(frame, text = "Sumar", command = self.sumar).grid(row = 4, column = 0)
        ttk.Button(frame, text = "Salir", command = quit).grid(row = 4, column = 1)

    def validacion(self):
        return (len(self.operador1.get()) != 0 and len(self.operador2.get()) != 0)

    def sumar(self):
        if self.validacion():
            try:
                a = float(self.operador1.get())
            except ValueError:
                a = 0
            try:
                b = float(self.operador2.get())
            except ValueError:
                b = 0
            c = a + b
            d = "%.12f" % c
            self.message['text'] = c
        else:
            self.message['text'] = 'Operador 1 y Operador 2 son requeridos'

# Define la función main() que es en realidad la que indica
# el comienzo del programa. Dentro de ella se crea el objeto
# aplicación 'mi_app' basado en la clase 'Aplicación':

def main():
    window = Tk()
    mi_app = Aplicacion(window)
    window.mainloop()
    return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es
# importado:

if __name__ == '__main__':
    main()