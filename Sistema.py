from Libraries.validaciones import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3
import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import time
from datetime import datetime
#pillow(imagenes)
#reportlab(pdfs)
#cerberus(validaciones)
NOMBRE_PROGRAMA = "Electro A"
carrito = []
conexion = sqlite3.connect("BaseElectroA.db")

#Paleta Colores 1
Naranja_intenso= '#FF6F00'
Gris_oscuro_con_tono_anaranjado= '#5D4037'
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
	estilos.configure('tabla.Treeview.Heading', background=color_navegacion,foreground= "snow",font = ("Calibri",12),)
	estilos.map('tabla.Treeview.Heading', background=[('selected', color_fondo),('active', color_fondo)])
	#Buscador
	# estilos.configure('buscador.Entrey',background=Gris_cálido_neutro)

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

def articulos(frame_contenido):
	global frame_articulos, Gris_cálido_neutro
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
	#menus desplegable
	# opciones_categorias = StringVar()
	# opciones_categorias.set("Escoge una categoría")
	# categorias = ('Iluminación','Aceites','Refrigeración')
	# menu = OptionMenu(frame_crud_articulos, opciones_categorias, *categorias,command=lambda x: seleccionar_opcion(x))
	# menu.pack(anchor=CENTER,padx=10)
	entry_categoria = ttk.Entry(frame_crud_articulos,font=("Calibri",15))
	# entry_categoria.config(state="readonly")
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
	frame_ventas = ttk.Frame(frame_contenido,style='fondo.TFrame')
	frame_ventas.pack(fill=BOTH,expand=1)

	frame_header = ttk.Frame(frame_ventas,style='transparente.TFrame')
	frame_header.pack(fill=X,ipady=50)
	frame_body = ttk.Frame(frame_ventas,style='transparente.TFrame')
	frame_body.pack(fill=BOTH,expand=1)

	frame_articulos = ttk.Frame(frame_body,style='blanco.TFrame')
	frame_articulos.pack(side=LEFT,fill=BOTH,expand=1,padx=(40,0),pady=10)
	frame_carrito = ttk.Frame(frame_body,style='blanco.TFrame')
	frame_carrito.pack(side=LEFT,fill=Y,ipadx=200,padx=40,pady=10)
	global tabla_carrito
	tabla_carrito = ttk.Treeview(frame_carrito,style='carrito.Treeview')
	tabla_carrito.pack(side=TOP,fill=BOTH,expand=1)
	tabla_carrito["columns"] = ("detalle","precio")
	tabla_carrito.column("#0",width=100)
	tabla_carrito.column("detalle",width=200,stretch=False)
	tabla_carrito.column("precio",width=100,stretch=False)
	tabla_carrito.heading("#0",text="cantidad")
	tabla_carrito.heading("detalle",text="detalle")
	tabla_carrito.heading("precio",text="precio")
	def vender():
		for articulo in carrito:
			print(articulo)
	boton_vender = Button(frame_carrito,text="Vender",command=vender)
	boton_vender.pack(side=BOTTOM,pady=10,padx=10)
		

def crear_ticket():
	hora_actual = time.strftime("%H:%M:%S")
	fecha_actual = time.strftime("%d/%m/%Y")
	nombre_archivo = f"ticket {fecha_actual} {hora_actual}.pdf"
	nuevo_pdf = canvas.Canvas(nombre_archivo,pagesize= A4)
	# lineas X
	nuevo_pdf.line(20,820,570,820)
	nuevo_pdf.line(20,20,570,20)
	nuevo_pdf.line(20,720,570,720)
	# lineas Y
	nuevo_pdf.line(20,20,20,820)
	nuevo_pdf.line(570,20,570,820)
	nuevo_pdf.line(480,720,480,820)
	
	nuevo_pdf.setFont('Times-Roman', 20)
	nuevo_pdf.drawString(50, 780, "Ticket")

	nuevo_pdf.save()
	pass

ventana = Tk()
misEstilos()
login()
ventana.mainloop()

