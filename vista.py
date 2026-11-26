from email import message
from multiprocessing.process import parent_process
from tkinter import *
import tkinter.font as tkFont
from tkinter import scrolledtext as st
from turtle import title
import TKinterExtra as tkx
import math
import controlador
from tkinter import filedialog
from tkinter import messagebox as msg
import shutil

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
ruta_imagen_seleccionada = ""
imagen_editando = ""
btn_img = ""
LISTA = []

######################
#### VISTA ANADIR ####
######################
id_revisando = -99
cargado = False

def abrir_explorador_imagen(ventana_menu):
	global ruta_imagen_seleccionada, imagen_editando, btn_img
	
	ruta = filedialog.askopenfilename(
		parent = ventana_menu,
		title = "Seleccionar imagen de portada",
		filetypes = [("Imágenes", "*.png")]
	)
	
	if ruta:
		ruta_imagen_seleccionada = "./imgs/"+ruta.split("/")[-1]
		shutil.copyfile(ruta, ruta_imagen_seleccionada)
		print (f"Imagen sleeccionada: {ruta}, {ruta_imagen_seleccionada}")
		imagen_editando = PhotoImage(file=ruta_imagen_seleccionada)
		btn_img.config(image=imagen_editando)
	
def cerrar_ventana():
	global id_revisando, cargado
	id_revisando = -99
	cargado = False

def ventana_nueva(id = -1):
	global id_revisando, cargado
	id_revisando = id
	ventana_subir_obra()
	if (id > -1):
		id_revisando = LISTA[id + (total_pelis * viendo_pagina)][0]
		cargar_datos()
	cargado = True

def eliminar_obra():
	global ventana2, id_revisando
	if (msg.Message(ventana2, parent=ventana2, type=msg.OKCANCEL, title="ADVERTENCIA", message="¿Deseas borrar esta obra?", detail="Esta acción no se puede deshacer.", icon=msg.WARNING).show() == msg.OK):
		controlador.eliminar(id_revisando)
		ventana2.destroy()
		actualizar_y_listar_peliculas()

def ventana_subir_obra ():
	global id_revisando, font, nombre_obra, director, genero, tipo_elegido, ano, estado_elegido, calificacion, descrip, imagen_editando, btn_img, ventana2, ruta_imagen_seleccionada, imagen_editando

	if(cargado): return
	
	ventana2 = Toplevel()
	ventana2.title("Añadir película o serie")
	ventana2.geometry("+500+100")
	ventana2.bind('<Destroy>', lambda _ : cerrar_ventana())

	ventana2.lift()

	ventana2.focus_force()
	ventana2.transient(root)
	
	split_v = Frame(ventana2)
	split_v.pack()

	topbar = Frame(split_v, pady=10, padx=20)
	topbar.pack()
	if (id_revisando >= 0):
		#### TOPBAR editar ####
		btn_agregar = Button(topbar, text="Editar", command = agregar_obra, bg="blue", fg="white", font=font)
		btn_agregar.grid(column=2, row=0)
		
		btn_eliminar = Button(topbar, text="Eliminar", command = eliminar_obra, bg="red", fg="white", font=font)
		btn_eliminar.grid(column=1, row=0)
	else:
		#### TOPBAR anadir ####
		btn_agregar = Button(topbar, text="Añadir", command = agregar_obra, bg="blue", fg="white", font=font)
		btn_agregar.pack()

	#### DATOS ####
	split_h = Frame(split_v)
	split_h.pack()

	ruta_imagen_seleccionada = ""
	imagen_editando = PhotoImage()
	btn_img  = Button(split_h, width=ancho_peli, height=alto_peli, text="Click para cargar imagen", image=imagen_editando, command = lambda: abrir_explorador_imagen(ventana2), bg="black")
	btn_img.grid(column=1, row=0)

	frm_info = Frame(split_h, width=30, padx=10)
	frm_info.grid(column=0, row=0)

	#TITULO
	frm_titulo = Frame(frm_info, pady=10, width=20)
	frm_titulo.pack()
	titulo_obra = Label(frm_titulo, text = "Título:", font=font)
	titulo_obra.pack()
	nombre_obra = Entry(frm_titulo, font=font)
	nombre_obra.pack()

	#director
	frm_direct = Frame(frm_info, pady=10)
	frm_direct.pack()
	direct_lab = Label(frm_direct, text = "Director:", font = font)
	direct_lab.pack()
	director = Entry(frm_direct, font = font)
	director.pack()

	#GENERO
	frm_genero = Frame(frm_info, pady=10)
	frm_genero.pack()
	genero_obra = Label(frm_genero, text = "Género:", font = font)
	genero_obra.pack()
	genero = Entry(frm_genero, font = font)
	genero.pack()
	
	
	#### QUAD ####
	quad = Frame(frm_info)
	quad.pack()

	#MENÚ TIPO DE OBRA
	frm_tipo = Frame(quad, pady=10)
	frm_tipo.grid(row=0,column=0)
	tipo_obra = Label(frm_tipo, text = "Tipo:", font=font)
	tipo_obra.pack()
	opciones_tipo = ["Película", "Serie"]
	tipo_elegido = StringVar(name="tipo")
	tipo = tkx.SelectBox(frm_tipo, opciones_tipo, tipo_elegido)
	tipo.pack()

	#AÑO DE ESTRENO
	frm_ano = Frame(quad, pady=10)
	frm_ano.grid(row=0, column=1)
	ano_estreno = Label(frm_ano, text = "Año:", font = font)
	ano_estreno.pack()
	ano = Entry(frm_ano, font = font)
	ano.pack()
	
	#ESTADO
	frm_estado = Frame(quad, pady=10)
	frm_estado.grid(row=1, column=0)
	lab_estado = Label(frm_estado, text = "Estado:", font = font)
	lab_estado.pack()
	opciones_estado = ["Sin ver", "Ver más tarde", "Viendo", "Visto", "Para re-ver"]
	estado_elegido = StringVar(name = "estado")
	estado = tkx.SelectBox(frm_estado, opciones_estado, estado_elegido)
	estado.pack()

	#Calificación
	frm_califi = Frame(quad, pady=10)
	frm_califi.grid(row=1, column=1)
	califi_lab = Label(frm_califi, text = "Calificación:", font = font)
	califi_lab.pack()
	calificacion = Entry(frm_califi, font = font)
	calificacion.pack()

	#DESCRIPCION
	frm_descripcion = Frame(split_v, pady=10)
	frm_descripcion.pack()
	descripcion_obra = Label(frm_descripcion, text = "Descripción:", font = font)
	descripcion_obra.pack()
	descrip = st.ScrolledText(frm_descripcion, width=60, font=font, height=10, wrap=WORD)
	descrip.pack()



def cargar_datos():
	global id_revisando, nombre_obra, director, genero, tipo_elegido, ano, estado_elegido, calificacion, descrip, imagen_editando, btn_img, ruta_imagen_seleccionada

	if(cargado): return

	datos = controlador.ver(id_revisando)
	print(id_revisando)
	print(datos)

	
	estados = {
		"Todos": "",
		"sin ver": "Sin ver",
		"ver mas tarde": "Ver más tarde",
		"viendo": "Viendo",
		"visto": "Visto",
		"para re-ver": "Para re-ver"
	}
	
	nombre_obra.insert(0, datos[1])
	root.setvar("tipo", value=datos[2])
	descrip.insert(INSERT, datos[3])
	genero.insert(0, datos[4])
	director.insert(0, datos[5])
	ano.insert(0, datos[6])
	calificacion.insert(0, datos[7])
	root.setvar("estado", value=estados[datos[8]])
	imagen_editando = PhotoImage(file=datos[9])
	ruta_imagen_seleccionada = datos[9]
	btn_img.config(image=imagen_editando)



def agregar_obra ():
	global id_revisando, font, nombre_obra, director, genero, tipo_elegido, ano, estado_elegido, calificacion, descrip, ruta_imagen_seleccionada, ventana2

	error = controlador.anadir(nombre_obra.get(), tipo_elegido.get(), descrip.get('1.0', END), genero.get(), director.get(), ano.get(), calificacion.get(), estado_elegido.get(),  ruta_imagen_seleccionada, id_revisando)
	
	if (error != ""):
		msg.Message(ventana2, parent=ventana2, message=error, icon=msg.ERROR).show()
	else:
		ventana2.destroy()
		actualizar_y_listar_peliculas()



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
	sel_tipo_buscar = tkx.SelectBox(busq_cont, ["Título", "Descripcion", "Género", "Director", "Año", "Calificación"], tipo_de_busqueda)
	sel_tipo_buscar.grid(column=2,row=0)
	
	
	
	btn_anadir = Button(topbar, text="+ Añadir al catálogo", bg="blue", fg="white", font=font, command=ventana_nueva)
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
			peli_img_inst.append(PhotoImage())
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
			match i: # ESTO ES UN CRIMEN, LO SABEMOS PERO NO SE NOS OCURRE NADA MEJOR
				case 0: peli_img[i].config(command=peli0)
				case 1: peli_img[i].config(command=peli1)
				case 2: peli_img[i].config(command=peli2)
				case 3: peli_img[i].config(command=peli3)
				case 4: peli_img[i].config(command=peli4)
				case 5: peli_img[i].config(command=peli5)
				case 6: peli_img[i].config(command=peli6)
				case 7: peli_img[i].config(command=peli7)
				case 8: peli_img[i].config(command=peli8)
				case 9: peli_img[i].config(command=peli9)
				case 10: peli_img[i].config(command=peli10)
				case 11: peli_img[i].config(command=peli11)
		else:
			peli_img_inst[i]=""
			peli_lab[i].config(text="")
			peli_img[i].grid_forget()

def peli0(): ventana_nueva(0)
def peli1(): ventana_nueva(1)
def peli2(): ventana_nueva(2)
def peli3(): ventana_nueva(3)
def peli4(): ventana_nueva(4)
def peli5(): ventana_nueva(5)
def peli6(): ventana_nueva(6)
def peli7(): ventana_nueva(7)
def peli8(): ventana_nueva(8)
def peli9(): ventana_nueva(9)
def peli10(): ventana_nueva(10)
def peli11(): ventana_nueva(11)


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