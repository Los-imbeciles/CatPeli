import sqlite3
from datetime import datetime

DB_NAME = "herramientas_informatica.db"

def init_db(self):
	global DB_NAME

	"""Inicializa la base de datos y crea la tabla si no existe"""
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute(f'''
		CREATE TABLE IF NOT EXISTS herramientas (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			titulo TEXT NOT NULL,
			tipo TEXT CHECK(tipo IN ('Película', 'Serie')),
			descripcion TEXT NOT NULL,
			genero TEXT NOT NULL,
			director TEXT NOT NULL,
			ano_estreno INT CHECK(ano_estreno >= 1900 ano_estreno <= {datetime.now().year}),
			calificacion INT CHECK(ano_estreno >= 0 ano_estreno <= 10),
			estado TEXT CHECK(estado IN ('sin ver', 'ver mas tarde', 'viendo', 'visto', 'para re-ver'))
		)
	''')

	conn.commit()
	conn.close()
	print("Base de datos inicializada correctamente")


def crear_herramienta(self, nombre, categoria, marca=None, modelo=None, precio=None, cantidad=1, descripcion=None, estado='Disponible'):
	global DB_NAME
	
	try:
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
	
		cursor.execute('''
			INSERT INTO herramientas
			(nombre, categoria, marca, modelo, precio, cantidad, descripcion, fecha_adquisicion, estado)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
		''', (nombre, categoria, marca, modelo, precio, cantidad, descripcion, datetime.now().date(), estado))
	
		conn.commit()
		herramienta_id = cursor.lastrowid
		conn.close()
	
		print(f"Herramienta '{nombre}' creada con ID: {herramienta_id}")
		return herramienta_id
	
	except sqlite3.Error as e:
		print(f"Error al crear herramienta: {e}")
		return None
		
def leer_herramientas(self, filtro=None, valor=None):
	global DB_NAME
	
	try:
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
	
		if filtro and valor:
			cursor.execute(f'''
				SELECT * FROM herramientas WHERE {filtro} LIKE ?
			''', (f'%{valor}%',))
		else:
			cursor.execute('SELECT * FROM herramientas')
	
		herramientas = cursor.fetchall()
		conn.close()
	
		return herramientas
	
	except sqlite3.Error as e:
		print(f"Error al leer herramientas: {e}")
		return []
		
def actualizar_herramienta(self, herramienta_id, **kwargs):
	global DB_NAME
	
	try:
		if not kwargs:
			print("No se proporcionaron campos para actualizar")
			return False
		
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
	
		# Construir la consulta dinámicamente
		set_clause = ', '.join([f"{key} = ?" for key in kwargs.keys()])
		valores = list(kwargs.values())
		valores.append(herramienta_id)
	
		cursor.execute(f'''
			UPDATE herramientas
			SET {set_clause}
			WHERE id = ?
		''', valores)
	
		conn.commit()
		filas_afectadas = cursor.rowcount
		conn.close()
	
		if filas_afectadas > 0:
			print(f"Herramienta ID {herramienta_id} actualizada correctamente")
			return True
		else:
			print(f"No se encontró la herramienta con ID {herramienta_id}")
			return False
		
	except sqlite3.Error as e:
		print(f"Error al actualizar herramienta: {e}")
		return False

def eliminar_herramienta(self, herramienta_id):
	global DB_NAME

	try:
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
	
		cursor.execute('DELETE FROM herramientas WHERE id = ?', (herramienta_id,))
	
		conn.commit()
		filas_afectadas = cursor.rowcount
		conn.close()
	
		if filas_afectadas > 0:
			print(f"Herramienta ID {herramienta_id} eliminada correctamente")
			return True
		else:
			print(f"No se encontró la herramienta con ID {herramienta_id}")
			return False
		
	except sqlite3.Error as e:
		print(f"Error al eliminar herramienta: {e}")
		return False

def mostrar_herramientas(self, herramientas=None):
	if herramientas is None:
		herramientas = self.leer_herramientas()
	
	if not herramientas:
		print("No hay herramientas en la base de datos")
		return
	
	print("\n" + "="*100)
	print(f"{'ID':<3} {'Nombre':<20} {'Categoría':<15} {'Marca':<12} {'Modelo':<15} {'Precio':<8} {'Cant':<4} {'Estado':<12}")
	print("-"*100)

	for herramienta in herramientas:
		print(f"{herramienta[0]:<3} {herramienta[1]:<20} {herramienta[2]:<15} {herramienta[3] or 'N/A':<12} "
			f"{herramienta[4] or 'N/A':<15} ${herramienta[5] or 0:<7} {herramienta[6]:<4} {herramienta[8]:<12}")

def buscar_herramientas(self, criterio, valor):
	global DB_NAME
	
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

def generar_reporte_inventario(self):
	global DB_NAME
	
	try:
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
	
		# Total de herramientas
		cursor.execute('SELECT COUNT(*), SUM(cantidad) FROM herramientas')
		total_herramientas, total_unidades = cursor.fetchone()
	
		# Herramientas por categoría
		cursor.execute('''
			SELECT categoria, COUNT(*), SUM(cantidad)
			FROM herramientas
			GROUP BY categoria
		''')
		por_categoria = cursor.fetchall()
	
		# Herramientas por estado
		cursor.execute('''
			SELECT estado, COUNT(*), SUM(cantidad)
			FROM herramientas
			GROUP BY estado
		''')
		por_estado = cursor.fetchall()
	
		conn.close()
	
		print("\n" + "="*50)
		print("REPORTE DE INVENTARIO")
		print("="*50)
		print(f"Total de tipos de herramientas: {total_herramientas}")
		print(f"Total de unidades: {total_unidades or 0}")
	
		print("\nPor categoría:")
		for categoria, count, unidades in por_categoria:
			print(f"  {categoria}: {count} tipos, {unidades} unidades")
		
		print("\nPor estado:")
		for estado, count, unidades in por_estado:
			print(f"  {estado}: {count} tipos, {unidades} unidades")
		
	except sqlite3.Error as e:
		print(f"Error al generar reporte: {e}")
