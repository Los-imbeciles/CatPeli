import modelo
import sqlite3 # para que pueda comprender los tipos de errores del sql, jamas se comunica con la base de datos directamente

def mostrar(tipo = None, estado = None, busqueda = None, busq_tipo = None):
	filtro = []
	valor = []
	tipos = {
		"Películas y series": "",
		"Solo películas": "Película",
		"Solo series": "Serie"
	}
	if (tipo != None and tipo != "Películas y series"):
		filtro.append('tipo')
		valor.append(tipos[tipo])

	
	estados = {
		"Todos": "",
		"Sin ver": "sin ver",
		"Ver más tarde": "ver mas tarde",
		"Viendo": "viendo",
		"Visto": "visto",
		"Para re-ver": "para re-ver"
	}
	if (estado != None and estado != "Todos"):
		filtro.append('estado')
		valor.append(estados[estado])

	columnas = {
		"Título": "titulo",
		"Descripcion": "descripcion",
		"Género": "genero",
		"Director": "director",
		"Año": "ano_estreno",
		"Calificación": "calificacion"
	}
	if (busqueda != None and busqueda != "" and busq_tipo != None and busq_tipo != ""):
		filtro.append(columnas[busq_tipo])
		valor.append(busqueda)

	try:
		obras = modelo.leer(filtro=filtro,valor=valor)
		return obras
	except sqlite3.Error as e:
		print(f"Error al leer obra: {e}")
		return []





def anadir(titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen, id=0):
	prev_lista = mostrar()
	se_encontro = False
	for i in prev_lista:
		if (id >= 0):
			if (i[0] == id):
				se_encontro = True
		else:
			if i[1] == titulo:
				return "ERROR: No se pueden añadir dos obras con el mismo título, considere añadir un detalle que la diferencie (como el año o el director) entre parentesís."
		

	if titulo == "" or tipo == "" or descripcion == "" or genero == "" or director == "" or ano_estreno == "" or calificacion == "" or estado == "" or imagen == "":
		return "ERROR: Debe añadir toda la informacion de la obra"

	
	estados = {
		"Sin ver": "sin ver",
		"Ver más tarde": "ver mas tarde",
		"Viendo": "viendo",
		"Visto": "visto",
		"Para re-ver": "para re-ver"
	}

	#QUE LA CALIFICACION Y EL AÑO DE ESTRENO NO SEAN NI FLOTANTES, NI TAMPOCO TEXTO
	if not(ano_estreno.isdecimal() and calificacion.isdecimal()):
		return "ERROR: El año de estreno y la calificación deben ser enteros"

	if (not (tipo=="Película" or tipo=="Serie")):
		return "ERROR: Esta obra debe ser una película o una serie."

	if (int(ano_estreno)<1900):
		return "ERROR: Esta obra es demasiado vieja para existir."
	if (int(ano_estreno)>2026):
		return "ERROR: Esta obra todavia no ha salido."
	
	if (int(calificacion) < 0 or int(calificacion) > 10):
		return "ERROR: La calificación no es válida."

	est = estados[estado]
	if (not (est=="sin ver" or est=="ver mas tarde" or est=="viendo" or est=="visto" or est=="para re-ver")):
		return "ERROR: El estado no es válido."

	if ((not(est=="visto" or est=="para re-ver")) and (int(calificacion) != 0)):
		return "ERROR: Debe haber visto la obra para poder dar una calificacion que no sea 0."

	try:
		if (id > 0):
			if (not se_encontro):
				return "ERROR: No se encontró la obra a editar"
			modelo.actualizar(id, titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, est, imagen)
		else:
			modelo.crear(titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, est, imagen)
		return ""
	except sqlite3.Error as e:
		return f"ERROR: {e}"





def eliminar(id):
	prev_lista = mostrar()
	for i in prev_lista:
		if i[0] == id:
			try:
				modelo.eliminar(id)
				return ""
			except sqlite3.Error as e:
				return f"ERROR: {e}"

	return "ERROR: No se encontró la obra."



def ver(id):
	try:
		obra = modelo.ver1(id)[0]
		return obra
	except sqlite3.Error as e:
		print(f"Error al leer la película o serie: {e}")
		return []