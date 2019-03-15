# -*- coding: utf-8 -*-

# Importa las clases de la librería TKInter
from tkinter import *
from tkinter import ttk
from Circulo import Circulo

class CirculoWindow():

    def __init__(self, window):
        self.window = window
        self.window.configure(bg = 'white')
        self.window.title('Circulo')

        # Crear un frame container
        frame = LabelFrame(self.window, text = 'Calcular el área y perimetro')
        frame.grid(row = 0, column = 0, columnspan = 4, padx = 20, pady = 20)

        # Input - Datos de entrada

        # Agregar un label
        Label(frame, text = 'Radio: ').grid(row = 1, column = 0)

        # Agregar un textbox
        self.radio = Entry(frame)
        self.radio.focus()
        self.radio.grid(row = 1, column = 1)

        # Output - Datos de salida

        # Agregar un label
        Label(frame, text = 'Área: ').grid(row = 2, column = 0)

        # Agregar mensajes de salida
        self.area = Label(frame, text = 'Área', fg = 'blue')
        self.area.grid(row = 2, column = 1)

        # Agregar una etiqueta (label)
        Label(frame, text='Perímetro: ').grid(row = 3, column = 0)

        # Agregar mensajes de salida
        self.perimetro = Label(frame, text = 'Perímetro', fg = 'red')
        self.perimetro.grid(row = 3, column = 1)

        # Agregar botones

        ttk.Button(frame, text = 'Calcular', command = self.calcular).grid(row = 4, column = 0)
        ttk.Button(frame, text = 'Salir', command = quit).grid(row = 4, column = 1)

    def validacion(self):
        return len(self.radio.get()) != 0

    def calcular(self):
        if self.validacion():
            try:
                radio = float(self.radio.get())
                circulo = Circulo(radio)
                self.area['text'] = circulo.getArea()
                self.perimetro['text'] = circulo.getPerimetro()
            except ValueError:
                self.area['text'] = 'El radio debe ser un número'
                self.perimetro['text'] = 'El radio debe ser un número'
        else:
            self.area['text'] = 'El radio está vacio'

def main():
    window = Tk()
    mi_programa = CirculoWindow(window)
    window.mainloop()
    return 0

if __name__ == '__main__':
    main()
