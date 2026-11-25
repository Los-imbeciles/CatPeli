import modelo

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
		"Genero": "genero",
		"Director": "director",
		"Año": "ano_estreno",
		"Calificación": "calificacion"
	}
	if (busqueda != None and busqueda != "" and busq_tipo != None and busq_tipo != ""):
		filtro.append(columnas[busq_tipo])
		valor.append(busqueda)

	obras = modelo.leer(filtro=filtro,valor=valor)
	
	if not obras:
		print("No hay herramientas en la base de datos")
	
	return obras

def buscar_herramientas(self, criterio, valor):	
	criterios_validos = ['nombre', 'categoria', 'marca', 'modelo', 'estado']

	if criterio not in criterios_validos:
		print(f"Criterio no válido. Use uno de: {', '.join(criterios_validos)}")
		return []
	
	herramientas = self.leer_herramientas(criterio, valor)

	if herramientas:
		print(f"\nResultados de búsqueda para {criterio}='{valor}':")
		self.mostrar_herramientas(herramientas)
	else:
		print(f"No se encontraron herramientas con {criterio}='{valor}'")
	
	return herramientas