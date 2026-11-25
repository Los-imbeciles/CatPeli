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
		INSERT INTO catalogo (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen) VALUES(
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
		INSERT INTO catalogo (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen) VALUES(
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
		INSERT INTO catalogo (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen) VALUES(
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
		INSERT INTO catalogo (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen) VALUES(
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
		INSERT INTO catalogo (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen) VALUES(
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
		INSERT INTO catalogo (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen) VALUES(
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
		INSERT INTO catalogo (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen) VALUES(
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

	cursor.execute('''
		INSERT INTO catalogo (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen) VALUES(
			"Como entrenar a tu dragón",
			'Pelicula',
			'Un desventurado joven vikingo, que aspira a cazar dragones, se convierte en el improbable amigo de un joven dragón, y aprende que puede haber más en las criaturas de lo que suponía.',
			'Acción',
			'Dean DeBlois - Chris Sanders',
			2010,
			'8',
			'visto',
			'imgs/como entrenar a tu dragon.png'
		)
	''')

	cursor.execute('''
		INSERT INTO catalogo VALUES(
			9,
			"Como entrenar a tu dragón 2",
			'Pelicula',
			'Cuando Hipo y Chimuelo descubren una cueva de hielo que alberga a cientos de nuevos dragones salvajes y al misterioso Jinete del Dragón, los dos amigos se encuentran en el centro de una batalla para proteger la paz.',
			'Acción',
			'Dean DeBlois',
			2014,
			'7',
			'visto',
			'imgs/como entrenar a tu dragon.png'
		)
	''')
	conn.commit()
	conn.close()



def crear(titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen):
	global DB_NAME
	
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute('''
		INSERT INTO catalogo
		(titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen)
		VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
	''', (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen))

	conn.commit()
	conn.close()




def leer(filtro = [], valor= []):
	global DB_NAME
	
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



def actualizar(l_id, titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen):
	global DB_NAME
	
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute('''
		UPDATE catalogo SET
		titulo = ?,
		tipo = ?,
		descripcion = ?,
		genero = ?,
		director = ?,
		ano_estreno = ?,
		calificacion = ?,
		estado ?,
		imagen ?
		WHERE id = ?
	''', (l_id, titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen))

	conn.commit()
	conn.close()



def eliminar(l_id):
	global DB_NAME
	
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute('DELETE FROM catalogo WHERE id = ?', (l_id,))

	conn.commit()
	conn.close()