'''
	frame_entry_buscador = ttk.Frame(frame_buscador_articulos,style='oscuro.TFrame')
	frame_entry_buscador.pack(fill=X,padx=10,pady=10)
	label_buscador = ttk.Label(frame_entry_buscador,text="Buscador",style='entradasCrud.TLabel')
	label_buscador.pack(anchor=W,padx=10,pady=(10,0))
	entry_buscador = ttk.Entry(frame_entry_buscador,width=40, font=("Calibri",15))
	entry_buscador.configure(background='#D7CCC8', foreground='Black',width=35 ,borderwidth=0)
	entry_buscador.pack(anchor=W,padx=10,pady=(0,10))

	global tabla_articulos_ventas
	tabla_articulos_ventas = ttk.Treeview(frame_buscador_articulos,style='tabla.Treeview')
	tabla_articulos_ventas.pack(fill=BOTH,expand=1,padx=10,pady=10)
	tabla_articulos_ventas["columns"] = ("codigo","categoria","detalle","precio")
	tabla_articulos_ventas.column("#0",width=100)
	tabla_articulos_ventas.column("codigo",width=100,stretch=False)	
	tabla_articulos_ventas.column("categoria",width=100,stretch=False)	
	tabla_articulos_ventas.column("detalle",width=200,stretch=False)	
	tabla_articulos_ventas.column("precio",width=100,stretch=False)
	tabla_articulos_ventas.heading("#0",text="cantidad")
	tabla_articulos_ventas.heading("codigo",text="codigo")
	tabla_articulos_ventas.heading("categoria",text="categoria")
	tabla_articulos_ventas.heading("detalle",text="detalle")
	tabla_articulos_ventas.heading("precio",text="precio")






	def determinar_cantidad():
		global tabla_carrito_ventas,entry_valor_cantidad
		cantidad = entry_valor_cantidad.get()
		precio = fila["values"][2]
		subtotal = int(cantidad) * int(precio)
		total = int(entry_total.get()) + subtotal
		entry_total.config(state="normal")
		entry_total.delete(0, END)
		entry_total.insert(0, total)
		entry_total.config(state="readonly")
		# Insertar datos en la tabla de carrito
		tabla_carrito_ventas.insert("", END, text=fila["values"][1], values=(["values"][1],cantidad, precio, subtotal))




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
	tabla_carrito_ventas.heading("precio", text="Precio", anchor=CENTER)
	tabla_carrito_ventas.heading("cantidad", text="Cantidad", anchor=CENTER)
	tabla_carrito_ventas.heading("Subtotal", text="Subtotal", anchor=CENTER)

	'''


    nuevo_pdf.setFont("Times-Roman",20,"bold")
	nuevo_pdf.drawString(250, 810, "Factura")
	nuevo_pdf.setFont("Times-Roman",12,"normal" )
	nuevo_pdf.drawString(50, 800, "electro a" )
	nuevo_pdf.setFont("Times-Roman",12,"normal")
	nuevo_pdf.drawString(50, 780, "Calle 123, Ciudad")
	nuevo_pdf.setFont("Times-Roman",12,"normal")
	nuevo_pdf.drawString(50, 760, "Cuit: 30-12345678-9")
	nuevo_pdf.setFont("Times-Roman",12,"normal")
	nuevo_pdf.drawString(50, 740, "Telefono: 4321-4321")
	nuevo_pdf.setFont("Times-Roman",12,"normal")
	nuevo_pdf.drawString(460, 800, fecha_actual)
	
	nuevo_pdf.setFont('Times-Roman', 20)
	nuevo_pdf.drawString(50, 560, "Cliente")
	nuevo_pdf.setFont('Times-Roman', 20)
	nuevo_pdf.drawString(50, 540, "Pepe")
	nuevo_pdf.setFont('Times-Roman', 20)
	nuevo_pdf.drawString(50, 520, "Calle 432, Capital Federal")
	nuevo_pdf.setFont('Times-Roman', 20)
	nuevo_pdf.drawString(50, 500, "Cuit: 20-12345678-9")
	nuevo_pdf.setFont('Times-Roman', 20)
	nuevo_pdf.drawString(50, 480, "Telefono: 1234-1234")
	
	nuevo_pdf.setFont('Times-Roman', 20)
	nuevo_pdf.drawString(50, 360, "Articulos")
