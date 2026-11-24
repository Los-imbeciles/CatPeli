import modelo

def mostrar():
	obras = modelo.leer()
	
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