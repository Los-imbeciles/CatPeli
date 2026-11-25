from tkinter import *
import vista

def SelectBox (master, opciones, elegido):
	elegido.set(opciones[0])
	sel = OptionMenu(master, elegido, *opciones)
	sel.config(font=vista.font)
	tmenu = vista.root.nametowidget(sel.menuname)
	tmenu.config(font=vista.font)

	def create_virtual_event(_varname, _idx, _mode):
		sel.event_generate("<<OptionMenuChanged>>")
	elegido.trace_add(("write", "unset"), create_virtual_event)
	return sel