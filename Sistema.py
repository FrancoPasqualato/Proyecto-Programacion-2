from Libraries.validaciones import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar
import sqlite3
import random
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import tables
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import sys
import os
import time
from datetime import datetime

#pillow(imagenes)
#reportlab(pdfs)
#cerberus(validaciones)
NOMBRE_PROGRAMA = "Electro A"
conexion = sqlite3.connect("BaseElectroA.db")
total_venta = 0
carrito = []
numero_factura = 0
venta_cancelada = False

#Paleta Colores 1
Naranja_intenso= '#FF6F00'
marron= '#5D4037'
Arena_clara= '#D7CCC8'
Beige_neutro= '#A1887F'
Gris_cálido_neutro= '#B0BEC5'
gris_oscuro = '#2a2c31'
gris_claro = '#5e5f63'

def misEstilos():
	global estilos
	color_navegacion='#FF6F00'
	color_navegacion2= '#2a2c31'
	color_fondo = gris_oscuro
	estilos = ttk.Style()
	estilos.theme_use("alt")
	estilos.configure("programa.TLabel",background=color_navegacion2,foreground='snow',font=('Calibri',24),relief= RAISED)
	estilos.configure("titulo.TLabel",background= color_navegacion2,foreground='snow',font=('Calibri',24))
	estilos.configure("entradas.TLabel",background='gray22',foreground='snow',font=('Calibri',13))
	estilos.configure("entradasCrud.TLabel",background='#5e5f63',foreground='black',font=('Calibri',15,'bold'),relief=FLAT,height=2,)
	#Login
	estilos.configure('login.TFrame',background='#2a2c31',relief=FLAT,border=0)
	estilos.configure('usuario.TLabel',background= color_fondo, foreground= color_navegacion,border=0, borderwidth=0)
	estilos.configure('fondo.TFrame',background=color_fondo,relief=FLAT,border=0)
	estilos.configure('clientes.TFrame',background=gris_claro,relief=FLAT,border=0)
	estilos.configure('principal.TFrame',background='gray22',relief=FLAT,border=0)
	estilos.configure('navegacion.TFrame',background=color_navegacion,relief=FLAT,border=0)
	estilos.configure('transparente.TFrame',background=color_fondo,relief=FLAT,border=0)
	estilos.configure('blanco.TFrame',background="white",relief=FLAT,border=0)
	estilos.configure('red.TFrame',background="red",relief=FLAT,border=0)	
	estilos.configure('botonNavegacion.TButton',background=color_navegacion,foreground='snow',font=('Calibri',13),relief=FLAT,bd=0,)
	estilos.map('botonNavegacion.TButton',background=[('pressed',color_navegacion2),('active',color_navegacion2)])
	estilos.configure('botonLogin.TButton',background=color_navegacion,foreground='snow',font=('Calibri',13),relief=FLAT,bd=0,)
	estilos.map('botonLogin.TButton',background=[('pressed',color_navegacion2),('active',color_navegacion2)])
	estilos.configure('carrito.Treeview', rowheight=100)
	#Tabla de articulos
	estilos.configure("tabla.Treeview",background=gris_claro,foreground="snow",font=("Calibri",11),fieldbackground=gris_claro,)
	estilos.configure("tabla_carrito.Treeview",background=gris_claro,foreground="snow",font=("Calibri",11),fieldbackground=gris_claro,maxwidth=400,)
	estilos.configure('tabla.Treeview.Heading', background=color_navegacion,foreground= "snow",font = ("Calibri",12),)
	estilos.map('tabla.Treeview.Heading', background=[('selected', color_fondo),('active', color_fondo)])
	#Pruebas
	estilos.configure('pruebas.TFrame',background="blue",relief=FLAT,border=0)
	

	return estilos

def login():
	ventana.geometry("400x600")
	ventana.title("Inicio de Sesion a Electro A")
	frame_login = ttk.Frame(ventana,style='login.TFrame')
	frame_login.pack(fill=BOTH,expand=1)
	def verificarLogin():
		frame_login.pack_forget()
		principal()
	boton_login = ttk.Button(frame_login,text="Ingresar",style='botonLogin.TButton',command=verificarLogin)
	boton_login.pack(side=BOTTOM,pady=40)
	label_usuario = ttk.Label(frame_login,text= 'Usuario', font=("Calibri",30),style='usuario.TLabel')
	label_usuario.pack(side=TOP,pady=50)
	entry_usuario = Entry(frame_login,font=("Calibri",15))
	entry_usuario.configure(background='#D7CCC8', foreground='Black',width=35 ,borderwidth=0)
	entry_usuario.pack(side=TOP)
	label_contraseña = ttk.Label(frame_login,text= 'Constraseña', font=("Calibri",30),style='usuario.TLabel')
	label_contraseña.pack(side=TOP,pady=50)
	entry_contraseña = Entry(frame_login,font=("Calibri",15))
	entry_contraseña.configure(background='#D7CCC8', foreground='Black',width=35 ,borderwidth=0,show="*")
	entry_contraseña.pack(side=TOP)


def principal():
	ventana.state("zoomed")
	ventana.title("Sistema de Electroa A")
	frame_botones= ttk.Frame(ventana,style='navegacion.TFrame')
	frame_botones.pack(side=LEFT,fill=Y)
	frame_contenido = ttk.Frame(ventana,style='principal.TFrame')
	frame_contenido.pack(side=LEFT,fill=BOTH,expand=1)

	titulo_programa = ttk.Label(frame_botones,text=NOMBRE_PROGRAMA,anchor="c",justify=RIGHT,style="programa.TLabel")
	titulo_programa.pack(fill=X)
	inicio(frame_contenido)
	def verInicio():
		borrarFrames()
		if 'frame_inicio' not in globals():
			inicio(frame_contenido)
		else:
			frame_inicio.pack(fill=BOTH,expand=1)
	boton_inicio = ttk.Button(frame_botones,text='Inicio',style='botonNavegacion.TButton',command=verInicio)
	boton_inicio.pack(ipady=20,ipadx=10)
	def verArticulos():
		borrarFrames()
		if 'frame_articulos' not in globals():
			articulos(frame_contenido)
		else:
			frame_articulos.pack(fill=BOTH,expand=1)
	boton_Articulos = ttk.Button(frame_botones,text='Articulos',style='botonNavegacion.TButton',command=verArticulos)
	boton_Articulos.pack(ipady=20,ipadx=10)
	def verClientes():
		borrarFrames()
		if 'frame_clientes' not in globals():
			clientes(frame_contenido)
		else:
			frame_clientes.pack(fill=BOTH,expand=1)
	boton_clientes = ttk.Button(frame_botones,text='Clientes',style='botonNavegacion.TButton',command=verClientes)
	boton_clientes.pack(ipady=20,ipadx=10)
	def verProveedores():
		borrarFrames()
		if 'frame_proveedores' not in globals():
			proveedores(frame_contenido)
		else:
			frame_proveedores.pack(fill=BOTH,expand=1)
	boton_proveedores = ttk.Button(frame_botones,text='Proveedores',style='botonNavegacion.TButton',command=verProveedores)
	boton_proveedores.pack(ipady=20,ipadx=10)
	def verCompras():
		borrarFrames()
		if 'frame_compras' not in globals():
			compras(frame_contenido)
		else:
			frame_compras.pack(fill=BOTH,expand=1)
	boton_compras = ttk.Button(frame_botones,text='Compras',style='botonNavegacion.TButton',command=verCompras)
	boton_compras.pack(ipady=20,ipadx=10)
	def verVentas():
		borrarFrames()
		if 'frame_ventas' not in globals():
			ventas(frame_contenido)
		else:
			frame_ventas.pack(fill=BOTH,expand=1)
	boton_ventas = ttk.Button(frame_botones,text='Ventas',style='botonNavegacion.TButton',command=verVentas)
	boton_ventas.pack(ipady=20,ipadx=10)

def borrarFrames():
	if 'frame_inicio' in globals():
		frame_inicio.pack_forget()
	if 'frame_articulos' in globals():
		frame_articulos.pack_forget()
	if 'frame_clientes' in globals():
		frame_clientes.pack_forget()
	if 'frame_proveedores' in globals():
		frame_proveedores.pack_forget()
	if 'frame_compras' in globals():
		frame_compras.pack_forget()
	if 'frame_ventas' in globals():
		frame_ventas.pack_forget()
	
def inicio(frame_contenido):
	global frame_inicio
	frame_inicio = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_inicio.pack(fill=BOTH,expand=1)
	label_titulo = ttk.Label(frame_inicio,text="SISTEMA DE VENTAS",style='titulo.TLabel')
	label_titulo.pack()
	label_profe = ttk.Label(frame_inicio,text="Creado por el profe",style='entradas.TLabel')
	label_profe.pack(side=BOTTOM)

def cargar_articulos_global(tabla_treeview):
		tabla = conexion.cursor()
		tabla.execute("SELECT * FROM articulos ")
		datos = tabla.fetchall()
		for dato in datos:
			id_categoria = (dato[1],)
			tabla.execute("SELECT nombre FROM categorias WHERE id=?",id_categoria)
			datos_categorias = tabla.fetchall()
			nombre_categoria=datos_categorias[0][0]
			precio = "$"+str(dato[4])
			tabla_articulos.insert("",END,text=dato[0],values=(dato[2],nombre_categoria,dato[3],precio))
		tabla.close()

def articulos(frame_contenido):
	global frame_articulos, Gris_cálido_neutro, crear_ticket
	#frames
	frame_articulos = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_articulos.pack(fill=BOTH,expand=1)
	frame_buscador_articulos= ttk.Frame(frame_articulos,style='transparente.TFrame')
	frame_buscador_articulos.pack(side=LEFT,fill=BOTH,expand=1,padx=10,pady=10)
	frame_crud_articulos = ttk.Frame(frame_articulos,style='clientes.TFrame',relief=FLAT)
	frame_crud_articulos.pack(side=LEFT,fill=BOTH,expand=1,padx=10,pady=20)
	#Labels y Entrys 
	#Codigo
	label_codigo = ttk.Label(frame_crud_articulos,text="Codigo",style="entradasCrud.TLabel",anchor=CENTER)
	label_codigo.pack(anchor=W,padx=10,pady=10)
	entry_codigo = ttk.Entry(frame_crud_articulos,font=("Calibri",15))
	entry_codigo.config(state="readonly")
	entry_codigo.pack(anchor=W,padx=20,fill=X)
	#Categoria
	label_categoria = ttk.Label(frame_crud_articulos,text="Categoría",style="entradasCrud.TLabel",anchor=CENTER)
	label_categoria.pack(anchor=W,padx=10,pady=10)
	entry_categoria = ttk.Entry(frame_crud_articulos,font=("Calibri",15))
	entry_categoria.pack(anchor=W,padx=20,fill=X)
	#Detalle
	label_detalle = ttk.Label(frame_crud_articulos,text="Detalle",style="entradasCrud.TLabel",anchor=CENTER)
	label_detalle.pack(anchor=W,padx=10,pady=10)
	entry_detalle = ttk.Entry(frame_crud_articulos,font=("Calibri",15))
	entry_detalle.pack(anchor=W,padx=20,fill=X)
	#Stock
	label_stock = ttk.Label(frame_crud_articulos,text="Stock",style="entradasCrud.TLabel",anchor=CENTER)
	label_stock.pack(anchor=W,padx=10,pady=10)
	entry_stock = ttk.Entry(frame_crud_articulos,font=("Calibri",15))
	entry_stock.pack(anchor=W,padx=20,fill=X)
	#Precio
	label_precio = ttk.Label(frame_crud_articulos,text="Precio",style="entradasCrud.TLabel",anchor=CENTER)
	label_precio.pack(anchor=W,padx=10,pady=10)
	entry_precio = ttk.Entry(frame_crud_articulos,font=("Calibri",15))
	entry_precio.pack(anchor=W,padx=20,fill=X)
	# Cantidad
	label_cantidad = ttk.Label(frame_crud_articulos,text=" Cantidad",style="entradasCrud.TLabel")
	entry_cantidad = ttk.Entry(frame_crud_articulos,font=("Calibri",15))
	
	def validar_categoria(categoria):
		tabla = conexion.cursor()
		tabla.execute("SELECT nombre FROM categorias")
		categorias_existentes = [fila[0] for fila in tabla.fetchall()]
		tabla.close()
		return categoria in categorias_existentes
	def guardar_nuevo_articulo():
		global tabla_articulos
		#valores de los campos
		detalle = entry_detalle.get().upper()
		categoria = entry_categoria.get().upper()
		stock = entry_stock.get()
		precio = entry_precio.get()
		#validaciones
		if(detalle == "" or categoria == "" or stock == "" or precio == ""):
			messagebox.showerror("ERROR","Todos los campos son obligatorios")
		else:
			if validar_categoria(categoria):
				global tabla_articulos
				tabla = conexion.cursor()
				categoria = (entry_categoria.get().upper(),)
				tabla.execute("SELECT id FROM categorias WHERE nombre = ?",categoria)
				buscar_existente_categoria = tabla.fetchall()
				if(len(buscar_existente_categoria)<1):
					tabla.execute("INSERT INTO categorias(nombre) VALUES (?)",categoria)
				tabla.execute("SELECT id FROM categorias WHERE nombre=(?)",categoria)
				datos_categoria = tabla.fetchall()
				datos = (datos_categoria[0][0], entry_detalle.get().upper(),entry_stock.get(),entry_precio.get())
				tabla.execute("INSERT INTO articulos (categoria_id,detalle,stock,precio) VALUES(?,?,?,?)",datos)
				conexion.commit()
				tabla.close()
				borrar_entry_articulos()
				for fila in tabla_articulos.get_children():
					tabla_articulos.delete(fila)
				cargar_articulos()
				messagebox.showinfo("SV","Guardado correctamente")
			else:
				messagebox.showerror("Categoría inexistente", "La categoría no existe en la base de datos")
			
	def modificar_articulo():
		datos = (entry_detalle.get().upper(),entry_stock.get(),entry_precio.get(),entry_codigo.get())
		tabla = conexion.cursor()
		tabla.execute("UPDATE articulos SET detalle=?, stock=?, precio=? WHERE codigo=?",datos)
		conexion.commit()
		tabla.close()
		messagebox.showinfo("SV","Modificado correctamente")

	def eliminar_articulo():
		datos = (entry_codigo.get(),)
		tabla = conexion.cursor()
		tabla.execute("DELETE FROM articulos WHERE codigo=?",datos)
		conexion.commit()
		messagebox.showinfo(":)","Eliminado correctamente")
	def volver_nuevo_articulo():
		borrar_entry_articulos()
		entry_codigo.config(state="readonly")
		boton_nuevo_articulo.pack(side=BOTTOM,fill=X,pady=(0,40))
		boton_modificar_articulo.pack_forget()
		boton_eliminar_articulo.pack_forget()
		boton_volver_articulo.pack_forget()
		boton_agregar_carrito.pack_forget()
		entry_cantidad.pack_forget()
		label_cantidad.pack_forget()
	def agregar_carrito():
		#agruegar a la tabla carrito treeview
		tabla_carrito.insert("",END,text=entry_cantidad.get(),values=(entry_detalle.get(),entry_precio.get()))
		
		datos = (entry_codigo.get(),entry_detalle.get(),entry_stock.get(),entry_precio.get())
		tabla = conexion.cursor()
		tabla.execute("INSERT INTO carrito (codigo,detalle,stock,precio) VALUES(?,?,?,?)",datos)
		conexion.commit()
		tabla.close()
		messagebox.showinfo("SV","Agregado correctamente")
	#botones
	boton_nuevo_articulo = ttk.Button(frame_crud_articulos,text="Guardar nuevo articulo",command=guardar_nuevo_articulo,style='botonNavegacion.TButton')
	boton_nuevo_articulo.pack(side=BOTTOM,fill=X,pady=(0,40))
	boton_modificar_articulo = ttk.Button(frame_crud_articulos,text="Modificar articulo",command=modificar_articulo,style='botonNavegacion.TButton')
	boton_eliminar_articulo = ttk.Button(frame_crud_articulos,text="Eliminar articulo",command=eliminar_articulo,style='botonNavegacion.TButton')
	boton_volver_articulo = ttk.Button(frame_crud_articulos,text="Volver",command=volver_nuevo_articulo,style='botonNavegacion.TButton')
	boton_agregar_carrito = ttk.Button(frame_crud_articulos,text="Agregar al carrito",command=agregar_carrito,style='botonNavegacion.TButton')
	#buscador de articulos
	frame_entry_buscador = ttk.Frame(frame_buscador_articulos,style='transparente.TFrame')
	frame_entry_buscador.pack(fill=X,padx=10,pady=10)
	label_buscador = ttk.Label(frame_entry_buscador,text="Buscador",style="entradasCrud.TLabel")
	label_buscador.pack(anchor=W,pady=(10,0),padx=10)
	entry_buscador = ttk.Entry(frame_entry_buscador,width=40,font=("Calibri",15))
	entry_buscador.pack(anchor=W,pady=(0,10),padx=10)
	entry_buscador.configure(background='grey')
	#tabla de articulos
	tabla_articulos = ttk.Treeview(frame_buscador_articulos,style='tabla.Treeview')
	tabla_articulos.pack(fill=BOTH,expand=1,padx=10,pady=10)
	tabla_articulos["columns"] = ("detalle","categoria","stock","precio")
	tabla_articulos.heading("#0",text="Código")
	tabla_articulos.heading("detalle",text="Detalle")
	tabla_articulos.heading("categoria",text="Categoría")
	tabla_articulos.heading("stock",text="Stock")
	tabla_articulos.heading("precio",text="Precio")
	tabla_articulos.column("#0",width=20)
	tabla_articulos.column("precio",width=40)
	
	def refrescar_tabla():
		for fila in tabla_articulos.get_children():
			tabla_articulos.delete(fila)
		for dato in datos_articulos:
			id_categoria = (dato[1],)
			tabla.execute("SELECT nombre FROM categorias WHERE id=?",id_categoria)
			datos_categorias = tabla.fetchall()
			nombre_categoria = datos_categorias[0][0]
			precio = "$"+str(dato[4])
			detalle = dato[2]
			tabla_articulos.insert("",END,text=dato[0],values=(detalle,nombre_categoria,dato[3],precio))
		tabla.close()
	
	def buscarArticulo(evento):
		buscar = ('%'+entry_buscador.get()+'%','%'+entry_buscador.get()+'%')
		tabla = conexion.cursor()
		sql = "SELECT * FROM articulos WHERE detalle LIKE ? OR categoria_id LIKE (SELECT id FROM categorias WHERE nombre LIKE ?)"
		tabla.execute(sql,buscar)
		datos_articulos = tabla.fetchall()
		#borrar tabla
		for fila in tabla_articulos.get_children():
			tabla_articulos.delete(fila)
		for dato in datos_articulos:
			id_categoria = (dato[1],)
			tabla.execute("SELECT nombre FROM categorias WHERE id=?",id_categoria)
			datos_categorias = tabla.fetchall()
			nombre_categoria = datos_categorias[0][0]
			precio = "$"+str(dato[4])
			detalle = dato[2]
			tabla_articulos.insert("",END,text=dato[0],values=(detalle,nombre_categoria,dato[3],precio))
		tabla.close()
	entry_buscador.bind("<KeyRelease>",buscarArticulo)

	def borrar_entry_articulos():
		entry_codigo.delete(0,END)
		entry_detalle.delete(0,END)
		entry_categoria.delete(0,END)
		entry_stock.delete(0,END)
		entry_precio.delete(0,END)
	
	def seleccionarArticulo(evento):
		# Botones
		boton_nuevo_articulo.pack_forget()
		boton_volver_articulo.pack(side=BOTTOM,fill=X,pady=(0,40))
		boton_modificar_articulo.pack(side=BOTTOM,fill=X,pady=(0,10))
		boton_eliminar_articulo.pack(side=BOTTOM,fill=X,pady=(0,10))
		boton_agregar_carrito.pack(side=BOTTOM,fill=X,pady=(0,10))
		entry_cantidad.pack(anchor=W,padx=20,fill=X,side=BOTTOM,pady=(0,20))
		label_cantidad.pack(anchor=W,padx=10,pady=(50,10),side=BOTTOM)
		#Entry codigo y categoria normal
		entry_codigo.config(state="normal")	
		index = tabla_articulos.selection()
		fila = tabla_articulos.item(index)
		codigo = (fila["text"],)
		tabla = conexion.cursor()
		tabla.execute("SELECT * FROM articulos WHERE codigo=?",codigo)
		datos_articulos = tabla.fetchall()
		id_categoria = (datos_articulos[0][1],)
		tabla.execute("SELECT nombre FROM categorias WHERE id=?",id_categoria)
		datos_categorias = tabla.fetchall()
		nombre_categoria = datos_categorias[0][0]
		tabla.close()
		borrar_entry_articulos()
		entry_codigo.insert(END,datos_articulos[0][0])
		entry_categoria.insert(END,nombre_categoria)
		entry_detalle.insert(END,datos_articulos[0][2])
		entry_stock.insert(END,datos_articulos[0][3])
		entry_precio.insert(END,datos_articulos[0][4])
		
	tabla_articulos.bind("<<TreeviewSelect>>",seleccionarArticulo)
	
	def cargar_articulos():
		tabla = conexion.cursor()
		tabla.execute("SELECT * FROM articulos ")
		datos = tabla.fetchall()
		for dato in datos:
			id_categoria = (dato[1],)
			tabla.execute("SELECT nombre FROM categorias WHERE id=?",id_categoria)
			datos_categorias = tabla.fetchall()
			nombre_categoria=datos_categorias[0][0]
			precio = "$"+str(dato[4])
			tabla_articulos.insert("",END,text=dato[0],values=(dato[2],nombre_categoria,dato[3],precio))
		tabla.close()

	cargar_articulos()
	
def clientes(frame_contenido):
    global frame_clientes
    # Frame para el buscador y los botones
    frame_buscador_botones = ttk.Frame(frame_contenido, style='transparente.TFrame')
    frame_buscador_botones.pack(side=TOP, fill=X, padx=10, pady=10)

    label_buscador = ttk.Label(frame_buscador_botones, text="Buscar cliente:")
    label_buscador.pack(side=LEFT, padx=10)

    entry_buscador = ttk.Entry(frame_buscador_botones, width=40)
    entry_buscador.pack(side=LEFT, padx=10)

    boton_buscador = ttk.Button(frame_buscador_botones, text="Buscar")
    boton_buscador.pack(side=LEFT, padx=10)

    boton_agregar = ttk.Button(frame_buscador_botones, text="Agregar cliente", command=agregar_cliente)
    boton_agregar.pack(side=LEFT, padx=10)

    # Frame para la tabla
    frame_tabla = ttk.Frame(frame_contenido, style='clientes.TFrame')
    frame_tabla.pack(side=TOP, fill=BOTH, expand=1, padx=10, pady=10)

    tabla_clientes = ttk.Treeview(frame_tabla, style='tabla.Treeview', selectmode='browse')
    tabla_clientes.pack(fill=BOTH, expand=1, padx=10, pady=10)

    # Definir columnas
    tabla_clientes['columns'] = ('Nombre', 'Apellido', 'Teléfono', 'Correo')

    # Formatear columnas
    tabla_clientes.column('#0', width=0, stretch=NO)
    tabla_clientes.column('Nombre', anchor=W, width=120)
    tabla_clientes.column('Apellido', anchor=W, width=120)
    tabla_clientes.column('Teléfono', anchor=W, width=100)
    tabla_clientes.column('Correo', anchor=W, width=150)

    # Encabezados
    tabla_clientes.heading('#0', text='', anchor=W)
    tabla_clientes.heading('Nombre', text='Nombre', anchor=W)
    tabla_clientes.heading('Apellido', text='Apellido', anchor=W)
    tabla_clientes.heading('Teléfono', text='Teléfono', anchor=W)
    tabla_clientes.heading('Correo', text='Correo', anchor=W)
    
    def agregar_cliente():
        ventana_agregar= Toplevel()
        ventana_agregar.title("Agregar cliente")
        label_nombre = ttk.Label(ventana_agregar, text="Nombre:")
        label_nombre.pack(padx=10, pady=10)
        entry_nombre = ttk.Entry(ventana_agregar, width=40)
        entry_nombre.pack(padx=10, pady=10)
        label_apellido = ttk.Label(ventana_agregar, text="Apellido:")
        label_apellido.pack(padx=10, pady=10)
        entry_apellido = ttk.Entry(ventana_agregar, width=40)
        entry_apellido.pack(padx=10, pady=10)
        label_telefono = ttk.Label(ventana_agregar, text="Teléfono:")
        label_telefono.pack(padx=10, pady=10)
        entry_telefono = ttk.Entry(ventana_agregar, width=40)
        entry_telefono.pack(padx=10, pady=10)
        label_correo = ttk.Label(ventana_agregar, text="Correo:")
        label_correo.pack(padx=10, pady=10)
        entry_correo = ttk.Entry(ventana_agregar, width=40)
        entry_correo.pack(padx=10, pady=10)
        boton_guardar = ttk.Button(ventana_agregar, text="Guardar", command=lambda: guardar_cliente(entry_nombre.get(), entry_apellido.get(), entry_telefono.get(), entry_correo.get()))
        boton_guardar.pack(padx=10, pady=10)

def proveedores(frame_contenido):
	global frame_proveedores
	frame_proveedores = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_proveedores.pack(fill=BOTH,expand=1)
	label_proveedores = ttk.Label(frame_proveedores,text="Proveedores",style='titulo.TLabel')
	label_proveedores.pack()

def compras(frame_contenido):
	global frame_compras
	frame_compras = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_compras.pack(fill=BOTH,expand=1)
	label_compras = ttk.Label(frame_compras,text="Compras",style='titulo.TLabel')
	label_compras.pack()



def ventas(frame_contenido):
	global frame_ventas
	frame_ventas = ttk.Frame(frame_contenido,style='transparente.TFrame')
	frame_ventas.pack(fill=BOTH,expand=1)
	#Frame Encabezado
	frame_header = ttk.Frame(frame_ventas,style='transparente.TFrame')
	frame_header.pack(fill=X,ipady=50)
	label_ventas = ttk.Label(frame_header,text="Ventas",style='titulo.TLabel')
	label_ventas.pack()
	#Frame completo
	frame_body = ttk.Frame(frame_ventas,style='transparente.TFrame')
	frame_body.pack(fill=BOTH,expand=1)
	#Frames contenedores de las tablas
	frame_articulos_ventas = ttk.Frame(frame_body,style='clientes.TFrame')
	frame_articulos_ventas.pack(side=LEFT,fill=BOTH,expand=1,padx=(20,0),pady=10)
	frame_carrito = ttk.Frame(frame_body,style='clientes.TFrame')
	frame_carrito.pack(side=LEFT,fill=Y,ipadx=300,padx=20,pady=10)
	
	label_buscador_ventas = ttk.Label(frame_articulos_ventas,text="Buscador",style='entradasCrud.TLabel')
	label_buscador_ventas.pack(anchor=W,padx=10,pady=(10,0))
	entry_buscador_ventas = ttk.Entry(frame_articulos_ventas,width=40,font=("Calibri",15))
	entry_buscador_ventas.pack(anchor=W,padx=10,pady=(0,10))
	label_carrito_ventas = ttk.Label(frame_carrito,text="Carrito",style='entradasCrud.TLabel')
	label_carrito_ventas.pack(anchor=CENTER,padx=10,pady=(10,0))

	tabla_articulos_ventas = ttk.Treeview(frame_articulos_ventas,style='tabla.Treeview',)
	tabla_articulos_ventas["columns"] = ("Código", "nombre", "precio", "stock")
	tabla_articulos_ventas.column("#0", width=0, stretch=NO)
	tabla_articulos_ventas.column("Código", anchor=W, width=50)
	tabla_articulos_ventas.column("nombre", anchor=W, width=200)
	tabla_articulos_ventas.column("precio", anchor=W, width=100)
	tabla_articulos_ventas.column("stock", anchor=W, width=100)
	tabla_articulos_ventas.heading("#0", text="", anchor=W)
	tabla_articulos_ventas.heading("Código", text="Código", anchor=CENTER)
	tabla_articulos_ventas.heading("nombre", text="Nombre", anchor=CENTER)
	tabla_articulos_ventas.heading("precio", text="Precio", anchor=CENTER)
	tabla_articulos_ventas.heading("stock", text="Stock", anchor=CENTER)
	tabla_articulos_ventas.pack(fill=BOTH, expand=True,padx=10,pady=10)

	tabla_carrito_ventas = ttk.Treeview(frame_carrito,style='tabla.Treeview')
	tabla_carrito_ventas.pack(side=TOP,fill=BOTH,expand=True,pady=10,padx=10)
	tabla_carrito_ventas["columns"] = ( "nombre", "precio", "cantidad","Subtotal" )
	tabla_carrito_ventas.column("#0", width=0, stretch=NO)
	tabla_carrito_ventas.column("nombre", anchor=W, width=200)
	tabla_carrito_ventas.column("precio", anchor=W, width=100)
	tabla_carrito_ventas.column("cantidad", anchor=W, width=50)
	tabla_carrito_ventas.column("Subtotal", anchor=W, width=50)
	tabla_carrito_ventas.heading("#0", text="", anchor=W)
	tabla_carrito_ventas.heading("nombre", text="Nombre", anchor=CENTER)
	tabla_carrito_ventas.heading("precio", text="Precio U.", anchor=CENTER)
	tabla_carrito_ventas.heading("cantidad", text="Cantidad", anchor=CENTER)
	tabla_carrito_ventas.heading("Subtotal", text="Subtotal", anchor=CENTER)

	#Label y entry articulo seleccionado
	label_articulo_seleccionado = ttk.Label(frame_articulos_ventas,text="Artículo Seleccionado:",style='entradasCrud.TLabel')
	label_articulo_seleccionado.pack(side=LEFT,anchor=W,padx=10,pady=10)
	entry_articulo_seleccionado = ttk.Entry(frame_articulos_ventas,width=40,font=("Calibri",15),state="readonly")
	entry_articulo_seleccionado.config(state="readonly")
	entry_articulo_seleccionado.pack(side=LEFT,anchor=W,padx=10,pady=10)

	#Funcion para que se coloque el articulo seleccionado de la tabla en el entry
	entry_valor_cantidad = Entry(frame_carrito,width=20,font=("Calibri",15))
	fila= None
	entry_total = Entry(frame_carrito,width=20,font=("Calibri",15))
	
	def seleccionar_articulo_ventas(evento):
		index = tabla_articulos_ventas.selection()
		fila=tabla_articulos_ventas.item(index)
		entry_articulo_seleccionado.config(state="normal")
		entry_articulo_seleccionado.delete(0,END)
		entry_articulo_seleccionado.insert(0,fila["values"][1])
		entry_articulo_seleccionado.config(state="readonly")
	
	def borrar_entrys():
		entry_articulo_seleccionado.config(state="normal")
		entry_articulo_seleccionado.delete(0,END)
		entry_articulo_seleccionado.config(state="readonly")
		entry_valor_cantidad.delete(0,END)
	#ejecutamos la funcion con evento
	tabla_articulos_ventas.bind("<<TreeviewSelect>>",seleccionar_articulo_ventas)
	
	def determinar_cantidad():
		global total_venta, venta_cancelada
		venta_cancelada = False
		fila = tabla_articulos_ventas.selection()
		if fila:
			fila = tabla_articulos_ventas.item(fila)
			nombre = fila["values"][1]
			precio = fila["values"][2].replace("$","")
			cantidad = entry_valor_cantidad.get()
			if not cantidad.strip():
				cantidad = "1"  # Asignar el valor por defecto como 1
			elif float(cantidad) > float(fila["values"][3]):
				messagebox.showerror(title="STOCK INSUFICIENTE",
							message="NO se cargo el ARTICULO por falta de STOCK",
							detail=f"Por favor, ingrese una cantidad menor a {fila['values'][3]} ."
							)
				return
			subtotal = int(cantidad) * float(precio)
			cantidad = int(cantidad)
			precio = float(precio)
			subtotal = cantidad * precio
			# Verificar si el producto ya está en el carrito
			producto_encontrado = False
			for idx, producto in enumerate(carrito):
				if producto["nombre_carrito"] == nombre:
					# Actualizar cantidad y subtotal del producto existente
					cantidad_actual = int(producto["cantidad_carrito"]) 
					subtotal_actual = float(producto["subtotal_carrito"]) 
					# Actualizar cantidad y subtotal del producto existente
					nueva_cantidad = cantidad_actual + cantidad
					nuevo_subtotal = subtotal_actual + subtotal

					producto["cantidad_carrito"] = nueva_cantidad
					producto["subtotal_carrito"] = nuevo_subtotal
					
					# Actualizar la tabla
					item_id = tabla_carrito_ventas.get_children()[idx]
					tabla_carrito_ventas.item(item_id, values=(nombre,f"${precio:.2f}",nueva_cantidad,f"${nuevo_subtotal:.2f}"))
					
					producto_encontrado = True
					break

			if not producto_encontrado:
				# Si no está en el carrito, agregarlo como nuevo producto
				tabla_carrito_ventas.insert("", END, text=nombre, values=(nombre, f"${precio:.2f}", cantidad, f"${subtotal:.2f}"))
				carrito.append({
					"nombre_carrito": nombre,
					"precio_carrito": precio,
					"cantidad_carrito": cantidad,
					"subtotal_carrito": subtotal
				})

			total_venta += subtotal
			borrar_entrys()
			entry_total.configure(state="normal")
			entry_total.delete(0,END)
			entry_total.insert(0,f"{total_venta:.2f}")
			entry_total.configure(state="readonly")
	#Funcion para buscar articulos con verifdicar stock
	def buscar_articulos_ventas(evento):
		buscar = ('%'+entry_buscador_ventas.get()+'%','%'+entry_buscador_ventas.get()+'%')
		tabla = conexion.cursor()
		sql = "SELECT * FROM articulos WHERE detalle LIKE ? OR categoria_id LIKE (SELECT id FROM categorias WHERE nombre LIKE ?) AND stock >= 1"
		tabla.execute(sql,buscar)
		datos_articulos = tabla.fetchall()
		#borrar tabla
		for fila in tabla_articulos_ventas.get_children():
			tabla_articulos_ventas.delete(fila)
		for dato in datos_articulos:
			id_categoria = (dato[1],)
			tabla.execute("SELECT nombre FROM categorias WHERE id=?",id_categoria)
			datos_categorias = tabla.fetchall()
			precio = "$"+str(dato[4])
			detalle = dato[2]
			if int(dato[3]) > 0:
				tabla_articulos_ventas.insert("",END,text=dato[0],values=(dato[0],detalle,precio,dato[3]))
		tabla.close()
	entry_buscador_ventas.bind("<KeyRelease>",buscar_articulos_ventas)
		
	#Boton de Vender
	boton_vender = ttk.Button(frame_carrito,text="Vender",command=crear_ticket,style='botonNavegacion.TButton')
	boton_vender.pack(side=RIGHT,pady=10,padx=10)
	
	'''aca va el antry total'''
	entry_total.configure(state="readonly")
	entry_total.pack(side=RIGHT,pady=10,padx=10)
	total = ttk.Label(frame_carrito,text="Total: ",style='entradasCrud.TLabel')
	total.pack(side=RIGHT,pady=10,padx=10)

	def cancelar_cantidad():
		global venta_cancelada
		for fila in tabla_carrito_ventas.get_children():
			tabla_carrito_ventas.delete(fila)
		entry_total.configure(state="normal")
		entry_total.delete(0,END)
		entry_total.configure(state="readonly")
		carrito.clear()
		venta_cancelada = True
		total_venta = 0

	boton_cancelar_cantidad = ttk.Button(frame_carrito,text="Cancelar",command=cancelar_cantidad,style='botonNavegacion.TButton')
	boton_cancelar_cantidad.pack(side=RIGHT,pady=10,padx=(0,200))
	#Etiqueta, entry y boton de cantidad
	boton_agregar_cantidad = ttk.Button(frame_carrito,text="Agregar",command=determinar_cantidad,style='botonNavegacion.TButton')
	boton_agregar_cantidad.pack(side=RIGHT,pady=10,padx=(0,20))
	
	cantidad_articulos = ttk.Label(frame_carrito,text="Cantidad de articulos: ",style='entradasCrud.TLabel')
	cantidad_articulos.pack(anchor=W,padx=10,pady=(0,10))
	#
	entry_valor_cantidad.pack(anchor=W,padx=10,pady=(0,10))
	def cargar_articulos_ventas():
		tabla = conexion.cursor()
		tabla.execute("SELECT * FROM articulos ")
		datos = tabla.fetchall()
		for dato in datos:
			precio = "$" + str(dato[4])
			if int(dato[3]) > 0:
				tabla_articulos_ventas.insert("", END, text=dato[0], values=(dato[0],dato[2], precio, dato[3]))
		tabla.close()
	cargar_articulos_ventas()

#FUNCION para disminuir stock
def disminuir_stock():
	tabla = conexion.cursor()
	for producto in carrito:
		tabla.execute("UPDATE articulos SET stock = stock - ? WHERE detalle = ?", (producto["cantidad_carrito"], producto["nombre_carrito"]))
	conexion.commit()


def crear_ticket():
	global numero_factura,total_venta,venta_cancelada
	if venta_cancelada == True:
		messagebox.showerror(title="Venta CANCELDA",
							message="No se realizo la venta por cancelacion del carrito",
							detail="Por favor, inicie una nueva venta o verifique los datos del carrito."
							)
		total_venta = 0
		return
	#Informcacion de la Factura
	disminuir_stock()
	#Info Cliente
	nombre_cliente = "Pepe"
	cuit_cliente = "20-12345678-9"
	denominacion_cliente = "Consumidor Final"
	ubi_cliente = "Calle 432, Capital Federal"
	cel_cliente = "1234-1234"
	#info empresa
	nombre_empresa = "Electro A"
	cuit_empresa = "30-12345678-9"
	ubi_empresa = "Calle 123, Ciudad"
	cel_empresa = "4321-4321"
	#Info Factura
	numero_factura += 1
	hora_actual = time.strftime("%H%M%S")
	fecha_actual = time.strftime("%d%m%Y")
	fecha_factura = time.strftime("%d/%m/%Y")
	hora_factura = time.strftime("%H:%M:%S")
	nombre_archivo = f"ticket {fecha_actual} {hora_actual} {numero_factura}.pdf"
	#Obtener informacion de los articulos del carrito
	for fila in carrito:
		nombre_articulo = fila["nombre_carrito"] #0
		cantidad_articulo = fila["cantidad_carrito"] #1
		precio_articulo = fila["precio_carrito"] #2
		subtotal_articulo = fila["subtotal_carrito"] #3
	# Dibujar el PDF
	nuevo_pdf = canvas.Canvas(nombre_archivo,pagesize= A4)
	# lineas X
	nuevo_pdf.line(20,820,570,820)
	nuevo_pdf.line(20,20,570,20)
	nuevo_pdf.line(20,720,570,720) #linea divisora de encabezado
	nuevo_pdf.line(20,650,570,650) #Linea divisora de datos cliente
	nuevo_pdf.line(20,620,570,620) #Linea divisora de datos articulos
	nuevo_pdf.line(20,100,570,100) #Linea divisora de datos totales
	# lineas Y
	nuevo_pdf.line(20,20,20,820) #Linea izquierda
	nuevo_pdf.line(570,20,570,820) #Linea derecha
	nuevo_pdf.line(370,720,370,820) #Linea corte encabezado derecha	
	nuevo_pdf.line(235,720,235,820) #Linea corte encabezado izquierda
	#Lineas Y divisoras de articulos
	nuevo_pdf.line(80,650,80,130) #antidad y detalle
	nuevo_pdf.line(410,650,410,130) #detalle y precio
	nuevo_pdf.line(490,650,490,100) #precio y subtotal
	#linea x final articulos
	nuevo_pdf.line(20,130,570,130) #Linea final articulos
	
	#Titulo
	nuevo_pdf.setFont("Helvetica", 30)
	nuevo_pdf.drawString(250,790,"Factura")
	nuevo_pdf.drawString(290,740,"A")
	#Info Empresa
	nuevo_pdf.setFont("Helvetica", 15)
	nuevo_pdf.drawString(30,795,"Empresa: "+ nombre_empresa)
	nuevo_pdf.drawString(30,775,"Cuit: " + cuit_empresa)
	nuevo_pdf.drawString(30,755,"Ubicacion: " + ubi_empresa)
	nuevo_pdf.drawString(30,735,"Celular: " +cel_empresa)
	#Info Cliente
	nuevo_pdf.setFont("Helvetica", 11)
	nuevo_pdf.drawString(30,700,"Cliente: "+ nombre_cliente)	
	nuevo_pdf.drawString(30,680,"Cuit: "+ cuit_cliente)
	nuevo_pdf.drawString(30,660,"Denominacion: "+ denominacion_cliente)
	nuevo_pdf.drawString(300,700,"Ubicacion: "+ ubi_cliente)
	nuevo_pdf.drawString(300,680,"Celular: "+ cel_cliente)
	# Info Factura
	nuevo_pdf.drawString(380,795,"N°: "+ str(numero_factura))
	nuevo_pdf.drawString(380,775,"Fecha: "+ str(fecha_factura))
	nuevo_pdf.drawString(380,755,"Hora: " + str(hora_factura)+" hs")
	#Info Articulos
	nuevo_pdf.setFont("Helvetica", 12)
	nuevo_pdf.drawString(25,630,"Cantidad:")
	nuevo_pdf.drawString(85,630,"Detalle:")
	nuevo_pdf.drawString(420,630,"Precio U.:")
	nuevo_pdf.drawString(500,630,"Subtotal:")
	y = 600
	for producto in carrito:
		nuevo_pdf.drawString(25,y, str(producto["cantidad_carrito"]))
		nuevo_pdf.drawString(85,y, str(producto["nombre_carrito"]))
		#sacamos el iva del producto
		producto["precio_carrito"] = float(producto["precio_carrito"])
		precio_sin_iva = producto["precio_carrito"] / 1.21
		nuevo_pdf.drawString(420,y, str(f"$ {precio_sin_iva:.2f}"))
		#sacamos el iva del subtotal
		producto["subtotal_carrito"] = float(producto["subtotal_carrito"])
		subtotal_sin_iva = producto["subtotal_carrito"] / 1.21
		nuevo_pdf.drawString(500,y, str(f"$ {subtotal_sin_iva:.2f}"))
		y -= 20
		
	#Final Factura
	nuevo_pdf.drawString(440,110,"Subtotal:")
	nuevo_pdf.drawString(500,110,"$ "+ str(f"{total_venta/1.21:.2f}")) #valor subtotal
	nuevo_pdf.drawString(420,80,"I.V.A. (21%):")
	nuevo_pdf.drawString(500,80,"$ "+ str(f"{(total_venta/1.21)*0.21:.2f}")) #valor iva
	nuevo_pdf.drawString(412,60,"Percepciones:")
	nuevo_pdf.drawString(500,60,"$ 000.00") #valor percepciones
	nuevo_pdf.setFont("Helvetica-Bold", 12,)
	nuevo_pdf.drawString(458,30,"Total:")
	nuevo_pdf.drawString(500,30,"$ "+ str(f"{total_venta:.2f}")) #valor total
	
	#Limpiar tabla carrito
	carrito.clear()
	total_venta = 0

	print(carrito)
	print(total_venta)

	# carpeta_destino = "D:\TrabajosImportantes\Programa Electro A\Facturas"
	# ruta_archivo = os.path.join(carpeta_destino, nombre_archivo)
	nuevo_pdf.save()
	os.startfile( f"{nombre_archivo}")
	

ventana = Tk()
misEstilos()
login()
ventana.mainloop()

