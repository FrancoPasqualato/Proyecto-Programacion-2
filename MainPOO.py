from tkinter import *
from tkinter import messagebox
from tkinter.font import Font

class frames():
    def __init__(self,ubi,tamaño,color,tipo):
        self.ubi = ubi
        self.tamaño = tamaño
        self.color = color
        self.tipo = tipo
        vent = Frame(ubi,tamaño,color,tipo)
        vent.pack

    # def construir (self,ubi,tamaño):
    #     self.tipo = Frame
    #     self.ubi = ubi
    #     self.tamaño = tamaño




"""Vemtana Principal"""
main = Tk()
main.geometry("1920x1080")
main.title("ELECTRO A")
main.resizable(0,0)
main.config(bg="blue")
main.state("zoomed")





ventana = frames
ventana("main","192x108","red")
        


main.mainloop() 