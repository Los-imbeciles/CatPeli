from tkinter import *
import vista

def SelectBox (master, opciones, elegido):
	elegido.set(opciones[0])
	sel = OptionMenu(master, elegido, *opciones)
	sel.config(font=vista.font)
	tmenu = vista.root.nametowidget(sel.menuname)
	tmenu.config(font=vista.font)
	return sel