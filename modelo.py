import sqlite3
from datetime import datetime

DB_NAME = "catalogo.db"

def init_db():
	global DB_NAME

	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute(f'''
		CREATE TABLE IF NOT EXISTS catalogo (
			id INTEGER PRIMARY KEY AUTOINCREMENT,
			titulo TEXT NOT NULL,
			tipo TEXT CHECK(tipo IN ('Película', 'Serie')),
			descripcion TEXT NOT NULL,
			genero TEXT NOT NULL,
			director TEXT NOT NULL,
			ano_estreno INT CHECK(ano_estreno >= 1900 AND ano_estreno <= {datetime.now().year}),
			calificacion INT CHECK(calificacion >= 0 AND calificacion <= 10),
			estado TEXT CHECK(estado IN ('sin ver', 'ver mas tarde', 'viendo', 'visto', 'para re-ver'))
		)
	''')

	conn.commit()
	conn.close()
	print("Base de datos inicializada correctamente")



def crear(titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado = ''):
	global DB_NAME
	
	try:
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
	
		cursor.execute('''
			INSERT INTO catalogo
			(titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado)
			VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
		''', (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado))
	
		conn.commit()
		conn.close()
	
		print(f"Película '{titulo}' añadida.")
	
	except sqlite3.Error as e:
		print(f"Error al crear herramienta: {e}")




def leer(filtro=None, valor=None):
	global DB_NAME
	
	try:
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
	
		if filtro and valor:
			cursor.execute(f'''
				SELECT * FROM catalogo WHERE {filtro} LIKE ?
			''', (f'%{valor}%',))
		else:
			cursor.execute('SELECT * FROM catalogo')
	
		leer = cursor.fetchall()
		conn.close()
	
		return leer
	
	except sqlite3.Error as e:
		print(f"Error al leer catalogo: {e}")
		return []



def actualizar(l_id, **kwargs):
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
		valores.append(l_id)
	
		cursor.execute(f'''
			UPDATE catalogo
			SET {set_clause}
			WHERE id = ?
		''', valores)
	
		conn.commit()
		filas_afectadas = cursor.rowcount
		conn.close()
	
		if filas_afectadas > 0:
			print("Obra actualizada correctamente.")
			return True
		else:
			print("No se encontró ninguna obra")
			return False
		
	except sqlite3.Error as e:
		print(f"Error al actualizar herramienta: {e}")
		return False



def eliminar(self, l_id):
	global DB_NAME

	try:
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
	
		cursor.execute('DELETE FROM catalogo WHERE id = ?', (l_id,))
	
		conn.commit()
		filas_afectadas = cursor.rowcount
		conn.close()
	
		if filas_afectadas > 0:
			print("Obra eliminada correctamente.")
			return True
		else:
			print("No se encontró la obra")
			return False
		
	except sqlite3.Error as e:
		print(f"Error al eliminar herramienta: {e}")
		return False