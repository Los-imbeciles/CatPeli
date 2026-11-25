from tkinter import *
import tkinter.font as tkFont
import TKinterExtra as tkx
import math
import controlador

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

viendo_pagina = 1
tipo_de_busqueda = ""
elg_estado = ""
elg_tipo = ""
font = ""
root:Tk

#cuadricula
alto_libreria = 800
ancho_libreria = 1400
cols_peli = 6
rows_peli = 2
total_pelis = cols_peli * rows_peli
ancho_peli = math.floor(ancho_libreria / cols_peli)
alto_peli = math.floor(alto_libreria / rows_peli)

LISTA = []
#def agregar_pelicula ():
# 	
def ventana_menu_peli ():
	ventana2 = Toplevel()
	ventana2.title("Añadir película o serie:")
	#btn_agregar = Button(ventana2, text="Agregar al catálogo", command = agregar)
	
	nombre_pelicula = Entry(ventana2, ) 
	opciones_estado = ["Vista", "Sin ver", "Viendo", "Ver más tarde", "Para re-ver"]
	estado_elegido = StringVar()
	estado = tkx.SelectBox(ventana2, opciones_estado, estado_elegido)
	estado.pack()





def ventana_principal():
	global tipo_de_busqueda, elg_estado, elg_tipo, font, root, peli_lab, peli_img, viendo_pagina, alto_libreria, ancho_libreria, cols_peli, rows_peli, total_pelis, ancho_peli, alto_peli
	
	root = Tk()
	root.title("Registro de películas y series")
	font = tkFont.Font(family="Inter", size=12)
	
	# BARRA DE BUSQUEDA
	topbar = Frame(root)
	
	busq_cont = Frame(topbar, padx=40)
	busq_cont.grid(column=2,row=0)
	
	btn_buscar = Button(busq_cont, text="Buscar", font=font)
	btn_buscar.grid(column=0, row=0)
	
	fil_buscar = Entry(busq_cont, font=font, width=20)
	fil_buscar.grid(column=1,row=0)

	tipo_de_busqueda = StringVar(root)
	sel_tipo_buscar = tkx.SelectBox(busq_cont, ["Título", "Tipo", "Descripcion", "Genero", "Director", "Año", "Calificación"], tipo_de_busqueda)
	sel_tipo_buscar.grid(column=2,row=0)
	
	
	
	btn_anadir = Button(topbar, text="+ Añadir al catálogo", bg="blue", fg="white", font=font, command = ventana_menu_peli)
	btn_anadir.grid(column=3,row=0)
	
	
	
	pag_cont = Frame(topbar, padx=80)
	pag_cont.grid(column=4, row=0)
	
	btn_sig = Button(pag_cont, text="<", font=font)
	btn_sig.grid(column=0,row=0)
	btn_ant = Button(pag_cont, text=">", font=font)
	btn_ant.grid(column=2,row=0)
	lab_pag = Label(pag_cont, text="1/4", font=font)
	lab_pag.grid(column=1,row=0)
	
	
	
	elg_estado = StringVar(root)
	sel_estado = tkx.SelectBox(topbar, ["Todos", "Sin ver", "Ver más tarde", "Visto"], elg_estado)  # creeria que en este caso tendría sentido que ver más tarde y rever sean considerado lo mismo
	sel_estado.grid(column=1,row=0)
	sel_estado.bind("<<ComboboxSelected>>", lambda _ : actualizar_y_listar_peliculas())
	
	
	elg_tipo = StringVar(root)
	sel_tipo = tkx.SelectBox(topbar, ["Películas y series", "Solo películas", "Solo series"], elg_tipo)
	sel_tipo.grid(column=0,row=0)
	sel_tipo.bind("<<ComboboxSelected>>", lambda _ : actualizar_y_listar_peliculas())
	
	
	
	
	
	#### LIBRERIA ####)
	libr = Frame(root)
	image = PhotoImage(file = "oveja.png").subsample(2, 2)

	for y in range(rows_peli):
		libr.rowconfigure(y, weight=1)

	for x in range(cols_peli):
		libr.columnconfigure(x, weight=1)

	index = 0
	pelis = []
	peli_lab = []
	peli_img = []
	for y in range(rows_peli):
		for x in range(cols_peli):
			pelis.append(Frame(libr, width=ancho_peli, height=alto_peli))
			peli_lab.append(Label(pelis[index], text=f"Peli{index}"))
			peli_lab[index].config(font=font)
			peli_img.append(Button(pelis[index], image=image, width=ancho_peli, height=alto_peli-10))
			peli_img[index].pack()
			peli_lab[index].pack()
			pelis[index].grid(column=x, row=y)
			index += 1
	
	topbar.pack()
	libr.pack(fill="both")

	actualizar_y_listar_peliculas()
	root.mainloop()



def listar_peliculas():
	global tipo_de_busqueda, elg_estado, elg_tipo, font, root, peli_lab, peli_img, viendo_pagina, alto_libreria, ancho_libreria, cols_peli, rows_peli, total_pelis, ancho_peli, alto_peli, LISTA
	
	for i in range(total_pelis):
		# ignoren los errores, creo que igual deberia funcionar
		leyendo = i + total_pelis * viendo_pagina
		
		if leyendo < len(LISTA):
			item = LISTA[leyendo]
			timg = PhotoImage(file = item["imagen"]).subsample(2, 2)
			peli_img[i].config(image=timg)
			peli_lab[i].config(text=item["titulo"])
		else:
			peli_img[i].config(image=PhotoImage(file="punto.png"))
			peli_lab[i].config(text="")



def actualizar_y_listar_peliculas():
	global LISTA
	LISTA = controlador.mostrar()
	listar_peliculas()