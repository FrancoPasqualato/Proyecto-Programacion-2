from tkinter import *
from tkinter.font import Font

ventana = Tk()
ventana.geometry("800x600")
ventana.title("Frames")
frame = Frame(ventana,bg="red")
frame.pack()

bigFont = Font(
   family="helvetica",
    size=40,
    weight="bold", # bold es negrita, normal es letra normal
    slant="roman", # roman es para la derecha, italic es para la izquierda
    underline= 0, #1 es subrayado, 0 es sin subrayar
    overstrike=0) #1 es tachado , 2 es sin tachar

    


ventana.mainloop()


# Palabras clave
"""
fg= color de la fuente
bg= color de fondo
bd= ancho del borde
cursor= modifica el puntero dentro del frame
height= altura
width= ancho
relief= tipo de borde
ventana.resizable(0,0) #0 no modificar tamaño, 1 si
ventana.state("zoomed") #Dar la forma maxima de la pantalla a la ventana
ventana.configure() # sirve para configurar las caracteristicas de las ventanas
"""
# FUENTES
"""
Arial: Una fuente sans-serif común.
Helvetica: Similar a Arial, también es una fuente sans-serif.
Times New Roman: Una fuente serif clásica.
Courier New: Una fuente de tipo monoespaciada.
Verdana: Otra fuente sans-serif con buena legibilidad.
Tahoma: Similar a Verdana, también es una fuente sans-serif.
Georgia: Una fuente serif que es adecuada para textos largos.
Trebuchet MS: Una fuente sans-serif legible en pantalla.
Calibri: Una fuente sans-serif moderna utilizada en versiones más recientes de Windows.
Comic Sans MS: Una fuente informal y a menudo utilizada para propósitos lúdicos.

"bold", # bold es negrita, normal es letra normal
"roman", # roman es para la derecha, italic es para la izquierda
underline= 0, #1 es subrayado, 0 es sin subrayar
overstrike=0, #1 es tachado , 2 es sin tachar
"""