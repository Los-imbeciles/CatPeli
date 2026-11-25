import sqlite3
from datetime import datetime

DB_NAME = "catalogo.db"

def init_db():
	global DB_NAME

	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute("DROP TABLE catalogo")
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
			estado TEXT CHECK(estado IN ('sin ver', 'ver mas tarde', 'viendo', 'visto', 'para re-ver')),
			imagen TEXT
		)
	''')
	cursor.execute('''
		INSERT INTO catalogo VALUES(
			1,
			"Burns para una temporada",
			'Película',
			'descripcion',
			'Imitacion barata',
			'Steven Spilbergo',
			'1999',
			'0',
			'visto',
			'oveja.png'
		)
	''')

	cursor.execute('''
		INSERT INTO catalogo VALUES(
			2,
			"Avergers:Doomsday",
			'Película',
			'Héroes icónicos de tres universos diferentes se encuentran en un curso de colisión mortal y enfrentan una amenaza existencial como nunca antes han visto.',
			'Ciencia ficción - Acción',
			'Anthony Russo - Joe Russo',
			'2026',
			8,
			'sin ver',
			'imgs/doomsday.png'
		)
	''')

	cursor.execute('''
		INSERT INTO catalogo VALUES(
			3,
			"Titanes del pacifico",
			'Película',
			'Mientras la guerra entre la humanidad y las criaturas marinas monstruosas avanza, un antiguo piloto y un aprendiz se unen para conducir un arma aparentemente obsoleta en un esfuerzo desesperado por salvar al mundo del apocalipsis.',
			'Ciencia ficción - Acción - Aventura',
			'Guillermo del Toro',
			'2013',
			'7',
			'visto',
			'imgs/titanes del pacifico.png'
		)
	''')

	cursor.execute('''
		INSERT INTO catalogo VALUES(
			4,
			"101 dálmatas",
			'Película',
			'Cuando una camada de cachorros dálmatas es secuestrada por los secuaces de Cruella de Vil, los padres deben encontrarlos antes de que los utilice para una diabólica colección de moda.',
			'Aventura - Comedia - Familia',
			'Clyde Geronimi - Hamilton Luske - Wolfgang Reitherman',
			1961,
			7,
			'visto',
			'imgs/101 dálmatas.png'
		)
	''')

	cursor.execute('''
		INSERT INTO catalogo VALUES(
			5,
			"La dama y el vagabundo",
			'Película',
			'La historia romántica de un perro cocker spaniel de una familia de clase alta y un perro callejero.',
			'Musica - Familia - Comedia - Aventura',
			'Clyde Geronimi - Hamilton Luske - Wilfred Jackson',
			1955,
			'7',
			'sin ver',
			'imgs/la dama y el vagabundo.png'
		)
	''')

	cursor.execute('''
		INSERT INTO catalogo VALUES(
			6,
			"Los ojos de Wakanda",
			'Serie',
			'Guerreros wakandeses que, a lo largo de la historia, han recorrido el mundo para recuperar peligrosos artefactos de vibranium.',
			'Ciencia ficción - Aventura',
			'John Fang - Todd Harris',
			2025,
			'6',
			'sin ver',
			'imgs/eyes of wakanda.png'
		)
	''')

	cursor.execute('''
		INSERT INTO catalogo VALUES(
			7,
			"Sherlock",
			'Serie',
			'El famoso detective Sherlock Holmes y su compañero el Dr. Watson resuelven crímenes en el Londres del siglo XXI.',
			'Misterio',
			'Paul McGuigan',
			2010,
			'9',
			'para re-ver',
			'imgs/sherlock.png'
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




def leer(filtro = [], valor= []):
	global DB_NAME
	
	try:
		conn = sqlite3.connect(DB_NAME)
		cursor = conn.cursor()
		sql = "SELECT * FROM catalogo"
		for i in range(len(filtro)):
			if i == 0: sql += " WHERE "
			else: sql += " AND "
			sql += f"{filtro[i]} LIKE '%{valor[i]}%'"
		cursor.execute(sql)
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



def eliminar(l_id):
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