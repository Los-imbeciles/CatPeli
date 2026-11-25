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

viendo_pagina = 0
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
paginas_disp = 0
ancho_peli = math.floor(ancho_libreria / cols_peli)
alto_peli = math.floor(alto_libreria / rows_peli)
pelis = []
peli_lab = []
peli_img = []
peli_img_inst = [] #instancias de las imagenes bug d tkinter
lab_pag = ""
fil_buscar=""

LISTA = []
def agregar_pelicula ():
	nombre = nombre_pelicula.get().strip()
	
def ventana_menu_peli ():
	ventana2 = Toplevel()
	ventana2.title("Añadir película o serie:")

	btn_agregar = Button(ventana2, text="Agregar al catálogo", command = agregar_pelicula)
	btn_agregar.pack()
	
	nomb_peli = Label(ventana2, text = "")
	nomb_peli.pack()
	nombre_pelicula = Entry(ventana2, width=30)
	nombre_pelicula.grid(row = 0, column = 1)
	opciones_estado = ["Vista", "Sin ver", "Viendo", "Ver más tarde", "Para re-ver"]
	estado_elegido = StringVar()
	estado = tkx.SelectBox(ventana2, opciones_estado, estado_elegido)
	estado.pack()





def ventana_principal():
	global tipo_de_busqueda, elg_estado, elg_tipo, font, root, pelis, peli_lab, peli_img, peli_img_inst, viendo_pagina, alto_libreria, ancho_libreria, cols_peli, rows_peli, total_pelis, ancho_peli, alto_peli, lab_pag, fil_buscar
	
	root = Tk()
	root.title("Registro de películas y series")
	font = tkFont.Font(family="Inter", size=12)
	
	# BARRA DE BUSQUEDA
	topbar = Frame(root)
	
	busq_cont = Frame(topbar, padx=40)
	busq_cont.grid(column=2,row=0)
	
	btn_buscar = Button(busq_cont, text="Buscar", font=font, command=actualizar_y_listar_peliculas)
	btn_buscar.grid(column=0, row=0)
	
	fil_buscar = Entry(busq_cont, font=font, width=20)
	fil_buscar.grid(column=1,row=0)

	tipo_de_busqueda = StringVar(root)
	sel_tipo_buscar = tkx.SelectBox(busq_cont, ["Título", "Descripcion", "Genero", "Director", "Año", "Calificación"], tipo_de_busqueda)
	sel_tipo_buscar.grid(column=2,row=0)
	
	
	
	btn_anadir = Button(topbar, text="+ Añadir al catálogo", bg="blue", fg="white", font=font, command = ventana_menu_peli)
	btn_anadir.grid(column=3,row=0)
	
	
	
	pag_cont = Frame(topbar, padx=40)
	pag_cont.grid(column=4, row=0)
	
	btn_ant = Button(pag_cont, text="<", font=font, command=prev_pag)
	btn_ant.grid(column=0,row=0)
	btn_sig = Button(pag_cont, text=">", font=font, command=sig_pag)
	btn_sig.grid(column=2,row=0)
	lab_pag = Label(pag_cont, text="1/4", font=font)
	lab_pag.grid(column=1,row=0)
	
	
	
	elg_estado = StringVar(root)
	sel_estado = tkx.SelectBox(topbar, ["Todos", "Sin ver", "Ver más tarde", "Viendo", "Visto", "Para re-ver"], elg_estado)
	sel_estado.bind("<<OptionMenuChanged>>", lambda _ : actualizar_y_listar_peliculas())
	sel_estado.grid(column=1,row=0)
	
	pad = Frame(topbar, padx=40)
	pad.grid(column=0, row=0)
	elg_tipo = StringVar(root)
	sel_tipo = tkx.SelectBox(pad, ["Películas y series", "Solo películas", "Solo series"], elg_tipo)
	sel_tipo.bind("<<OptionMenuChanged>>", lambda _ : actualizar_y_listar_peliculas())
	sel_tipo.pack()
	
	
	
	#### LIBRERIA ####)
	libr = Frame(root)

	for y in range(rows_peli):
		libr.rowconfigure(y, weight=1)

	for x in range(cols_peli):
		libr.columnconfigure(x, weight=1)

	index = 0
	for y in range(rows_peli):
		for x in range(cols_peli):
			pelis.append(Frame(libr, width=ancho_peli, height=alto_peli))
			peli_lab.append(Label(pelis[index], text=f"Peli{index}"))
			peli_lab[index].config(font=font)
			peli_img_inst.append(PhotoImage(file="oveja.png").subsample(2, 2))
			peli_img.append(Button(pelis[index], image=peli_img_inst[index], width=ancho_peli, height=alto_peli-10))
			peli_img[index].grid(row=0)
			peli_lab[index].grid(row=1)
			pelis[index].grid(column=x, row=y)
			index += 1
	
	topbar.pack()
	libr.pack(fill="both")

	actualizar_y_listar_peliculas()
	root.mainloop()



def listar_peliculas():
	global tipo_de_busqueda, elg_estado, elg_tipo, font, root, pelis, peli_lab, peli_img, peli_img_inst, viendo_pagina, alto_libreria, ancho_libreria, cols_peli, rows_peli, total_pelis, ancho_peli, alto_peli, LISTA

	lab_pag.config(text=" "+str(viendo_pagina+1)+"/"+str(paginas_disp+1)+" ")
	
	for i in range(total_pelis):
		# ignoren los errores, creo que igual deberia funcionar
		leyendo = i + (total_pelis * viendo_pagina)
		
		if leyendo < len(LISTA):
			item = LISTA[leyendo]
			peli_img_inst[i]=PhotoImage(file=item[9])
			peli_img[i].config(image=peli_img_inst[i])
			peli_lab[i].config(text=item[1])
			peli_img[i].grid(row=0)
		else:
			peli_img_inst[i]=""
			peli_lab[i].config(text="")
			peli_img[i].grid_forget()



def actualizar_y_listar_peliculas():
	global LISTA, paginas_disp, viendo_pagina
	viendo_pagina = 0
	LISTA = controlador.mostrar(elg_tipo.get(), elg_estado.get(), fil_buscar.get(), tipo_de_busqueda.get())
	paginas_disp = math.ceil(len(LISTA)/total_pelis)-1
	listar_peliculas()

def sig_pag():
	global viendo_pagina
	viendo_pagina += 1
	viendo_pagina=min(viendo_pagina,paginas_disp)
	listar_peliculas()

def prev_pag():
	global viendo_pagina
	viendo_pagina -= 1
	viendo_pagina=max(viendo_pagina,0)
	listar_peliculas()