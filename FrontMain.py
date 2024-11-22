from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import sqlite3
from tkinter import ttk
from Libraries.validaciones import *

carrito = []

"""conexion a la base de datos"""
conexion = sqlite3.connect("BaseElectroA.db")
tabla = conexion.cursor()

"""Funciones"""

def login():
	main.geometry("400x600")
	frame_login = ttk.Frame(main,style='login.TFrame')
	frame_login.pack(fill=BOTH,expand=1)
	def verificarLogin():
		frame_login.pack_forget()
		principal()
	boton_login = ttk.Button(frame_login,text="Ingresar",style='botonLogin.TButton',command=verificarLogin)
	boton_login.pack(side=BOTTOM,pady=40)

def cargar_tabla():
    tabla.execute('SELECT * FROM Clientes') #obtenemos la info de la tabla
    
    datos = tabla.fetchall() #obtenemos todos los registros
    
    return datos

def cargar_lista():
    Listbox.delete(0,END) #limpiar datos de la tabla
    datos = cargar_tabla() #obtenemos los datos de la base
    
    #insertamos los datos en la lista
    for fila in datos:
        texto_fila = ','.join(str(columna)for columna in fila)
        Listbox.insert(END, texto_fila)


"""colores"""
#Paleta 1
gris= "#343838"
azul1 = "#005f6b"
azul2 = "#008c9e"
celeste1= "#00b4cc"
celeste2= "#00dffc"

#Paleta 2
negro ="#0a0c0d"
azulnegro= "#213635"
azulceleste= "#1c5052"
celestepastel= "#348e91"
blanco= "#f2f2f2"

#Paleta 3 Grices
gris1="#4f5f6f"
gris2="#667687"
gris3="#7d8e9f"
gris4="#94a5b6"
gris5="#abbcce"

#-------------------
# celeste = "#5BCBC1"
#gris_oscuro = "#67686A"
# gris_oscuro2 = "#383F4C"
#negro2 = "#1D1F21"
# negro_claro = "#25282A"
naranja = "#DB9E34"
arena = "#EAD28A"

ColorBotones = naranja
fondoBoton = arena

"""Vemtana Principal"""

main = Tk()
main.geometry("1920x1080")
main.title("ELECTRO A")
main.resizable(0,0)
main.config(bg=gris1)
main.state("zoomed")

"""Comandos Botones"""

#CLIENTES
def MenuClientes():
    frame_clientes = Frame(main,bg=gris2)
    frame_clientes.pack(side=RIGHT,fill=Y,ipadx=718)
    
    # frame_titulo_clientes = Frame(frame_clientes,bg=negro)
    # frame_titulo_clientes.place(x=500,y=100,width=200,height=50)
    
    titulo_clientes = Label(frame_clientes,text="CLIENTES",bg=gris2,font=("Trebuchet MS", 40))
    titulo_clientes.pack(side=TOP,ipady=20)
    
    """Clientes"""

    boton_agregar = Button(frame_clientes,activebackground=fondoBoton,bg=ColorBotones,text="Agregar",font=("Comic Sans MS",17),width=18,height=1,bd=3,relief="groove",justify="center",cursor="hand2")
    boton_agregar.place(x=20,y=980)
    
    frame_nav_clientes = Frame(frame_clientes,height=60,relief="solid",bg=gris2,borderwidth=1)
    frame_nav_clientes.pack(fill=Y,ipadx=880)
    
    entry_nombre = Entry(frame_nav_clientes,font=("Comic Sans MS",12),)
    entry_nombre.pack(side=LEFT,padx=10)
    # lista_clientes = Listbox(frame_clientes, width=80, height=20,)
    # lista_clientes.pack()
    
    # scrollbar = Scrollbar(frame_clientes, orient=VERTICAL)
    # scrollbar.pack(side=RIGHT, fill=Y)
    # scrollbar.config(command=lista_clientes.yview)
    # cargar_lista()

#CARRITO
def Carrito():
    frame_carrito = Frame(main,bg=gris2)
    frame_carrito.pack(side=RIGHT,fill=Y,ipadx=718)
    titulo_carrito = Label(frame_carrito,text="Carrito",bg=gris2,font=("Trebuchet MS", 40))
    titulo_carrito.pack(side=TOP,ipady=20)


"""Frame Navegacion Izquierdo"""
#el espaciado entre los botones es de y=45
frame_navegacion =Frame(main, bg=gris1,borderwidth=2)
frame_navegacion.pack(side=LEFT,fill=Y,ipadx=82)

boton_inicio = Button(frame_navegacion,activebackground=fondoBoton,bg=ColorBotones,text="Inicio",font=("Comic Sans MS",11),width=16,height=1,bd=3,relief="groove",justify="center",cursor="hand2")
boton_inicio.place(x=2,y=10)

boton_clientes = Button(frame_navegacion,command=MenuClientes,activebackground=fondoBoton,bg=ColorBotones,text="Clientes",font=("Comic Sans MS",11),width=16,height=1,bd=3,relief="groove",justify="center",cursor="hand2")
boton_clientes.place(x=2,y=55)

boton_Turnos = Button(frame_navegacion,activebackground=fondoBoton,bg=ColorBotones,text="Turnos",font=("Comic Sans MS",11),width=16,height=1,bd=3,relief="groove",justify="center",cursor="hand2")
boton_Turnos.place(x=2,y=100)

boton_Carrito = Button(frame_navegacion,command=Carrito,activebackground=fondoBoton,bg=ColorBotones,text="Carrito",font=("Comic Sans MS",11),width=16,height=1,bd=3,relief="groove",justify="center",cursor="hand2")
boton_Carrito.place(x=2,y=145)

boton_Comprobantes = Button(frame_navegacion,activebackground=fondoBoton,bg=ColorBotones,text="Comprobantes",font=("Comic Sans MS",11),width=16,height=1,bd=3,relief="groove",justify="center",cursor="hand2")
boton_Comprobantes.place(x=2,y=190)

boton_cerrar = Button(frame_navegacion,activebackground=fondoBoton,bg=ColorBotones,text="Cerrar",font=("Comic Sans MS",11),width=16,height=1,bd=3,relief="groove",justify="center",cursor="hand2")
boton_cerrar.place(x=2,y=1010)






main.mainloop()