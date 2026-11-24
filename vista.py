from tkinter import *
import tkinter.font as tkFont


#  
# lista = []
# wind = tk.Tk()
# t1 = tk.Label(wind,text="Ingrese una herramienta: ").pack()
# input = tk.Entry(wind)
# input.pack()
# t2 = tk.Label(wind,text="[]")
# t3 = tk.Label(wind,text="",fg="red")
# 
# def mostrar_herramientas():
# 	global t2
# 	global t3
# 
# 	t2.pack_forget()
# 	t2 = tk.Label(wind,text=str(lista))
# 	t2.pack()
# 	t3.pack_forget()
# 	t3 = tk.Label(wind,text="")
# 	t3.pack()
# 
# def ingresar():
# 	global lista
# 	global input
# 	lista.append(input.get())
# 	mostrar_herramientas()
# 
# def eliminar():
# 	global lista
# 	global input
# 	global t3
# 	if input.get() in lista:
# 		lista.remove(input.get())
# 		mostrar_herramientas()
# 	else:
# 		t3.pack_forget()
# 		t3 = tk.Label(wind,text="ERROR: Ese elemento no existe")
# 		t3.pack()
# 
# boton1 = tk.Button(wind,text="Ingresar",padx=20,pady=5,command=ingresar).pack()
# boton2 = tk.Button(wind,text="Eliminar",padx=20,pady=5,command=eliminar).pack()
# t2.pack()
# t3.pack()
# 
# wind.mainloop()

tipo_de_busqueda = ""
font = ""

def ventana_principal():
	global tipo_de_busqueda, font

	root = Tk()
	font = tkFont.Font(family="Inter", size=14)

	# BARRA DE BUSQUEDA
	topbar = Frame(root)

	busq_cont = Frame(topbar, padx=80)
	busq_cont.grid(column=0,row=0)

	btn_buscar = Button(busq_cont, text="Buscar", font=font)
	btn_buscar.grid(column=0, row=0)

	fil_buscar = Entry(busq_cont, font=font, width=30)
	fil_buscar.grid(column=1,row=0)
	
	optiones_busq = ["Título", "Tipo", "Descripcion", "Genero", "Director", "Año", "Calificación"]
	resul = StringVar(root)
	resul.set("Título")
	com_tipo_buscar = OptionMenu(busq_cont, resul, *optiones_busq)
	com_tipo_buscar.config(font=font)
	tipo_de_busqueda = resul
	com_tipo_buscar.grid(column=2,row=0)
	tmenu = root.nametowidget(com_tipo_buscar.menuname)
	tmenu.config(font=font)



	btn_anadir = Button(topbar, text="+ Añadir al catálogo", bg="blue", fg="white", font=font)
	btn_anadir.grid(column=1,row=0)



	pag_cont = Frame(topbar, padx=80)
	pag_cont.grid(column=2, row=0)
	
	btn_sig = Button(pag_cont, text="<", font=font)
	btn_sig.grid(column=0,row=0)
	btn_ant = Button(pag_cont, text=">", font=font)
	btn_ant.grid(column=2,row=0)
	lab_pag = Label(pag_cont, text="1/4", font=font)
	lab_pag.grid(column=1,row=0)





#### LIBRERIA ####
	libr = Frame(root, width="500", height="500")
	libr.rowconfigure(0, weight=1)
	#image = tk.PhotoImage
	libr.rowconfigure(1, weight=1)
	libr.rowconfigure(2, weight=1)
	libr.columnconfigure(0, weight=1)
	libr.columnconfigure(1, weight=1)
	libr.columnconfigure(2, weight=1)
	libr.columnconfigure(3, weight=1)
	libr.columnconfigure(4, weight=1)
	libr.columnconfigure(5, weight=1)
	libr.columnconfigure(6, weight=1)

	# image = PhotoImage(file="hijosdeputa.png")
	# label = Label(root,image=image)
	# label.pack()
	
	topbar.pack()
	libr.pack()
	 
	# 
 #    selected_item = combo_box.get()
 #    label.config(text="Selected Item: " + selected_item)
	# 
	# root = tk.Tk()
	# root.title("Combobox Example")
	# 
	# label = tk.Label(root, text="Selected Item:")
	# label.pack(pady=10)
	# 
	# # Create a Combobox widget
	# combo_box = ttk.Combobox(
 #    root,
 #    values=["Option 1", "Option 2", "Option 3"],
 #    state="readonly"
	# )
	# combo_box.pack(pady=5)
	# 
	# combo_box.set("Option 1")
	# 
	# combo_box.bind("<<ComboboxSelected>>", select)
	
	root.mainloop()