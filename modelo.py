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
			"Cómo entrenar a tu dragón 2",
			'Película',
			'Cuando Hipo y Chimuelo descubren una cueva de hielo que alberga a cientos de nuevos dragones salvajes y al misterioso Jinete del Dragón, los dos amigos se encuentran en el centro de una batalla para proteger la paz.',
			'Acción',
			'Dean DeBlois',
			'2014',
			'7',
			'visto',
			'imgs/como entrenar a tu dragon 2.png'
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
			0,
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
			0,
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
			0,
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
			"Cómo entrenar a tu dragón",
			'Película',
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
			"Cómo entrenar a tu dragón 3",
			'Película',
			'Cuando Hipo descubre que Chimuelo no es el único Furia Nocturna, deberá encontrar el Mundo Perdido antes de que el tirano Grimmel lo encuentre primero.',
			'Acción - Comedia - Aventura - Drama',
			'Dean DeBlois',
			2019,
			0,
			'sin ver',
			'imgs/como entrenar a tu dragon 3.png'
		)
	''')
	cursor.execute('''
		INSERT INTO catalogo VALUES(
			10,
			"Vengadores:Endgame",
			'Película',
			'Después de que Thanos haya aniquilado a la mitad del universo, los Vengadores supervivientes deben hacer todo lo posible por deshacer tal atrocidad.',
			'Ciencia ficción',
			'Anthony Russo - Joe Russo',
			2019,
			0,
			'sin ver',
			'imgs/endgame.png'
		)
	''')
	cursor.execute('''
		INSERT INTO catalogo VALUES(
			11,
			"Spider-Man: Cruzando el multiverso",
			'Película',
			'Miles Morales conoce a un nuevo equipo de Spider-People formado por héroes de diferentes dimensiones. Pero cuando los héroes se enfrentan sobre cómo hacer frente a una nueva amenaza, Miles se encuentra en una encrucijada.',
			'Ciencia ficción - Familia',
			'Joaquim Dos Santos - Kemp Powers - Justin K. Thompson',
			2023,
			0,
			'viendo',
			'imgs/miles morales.png'
		)
	''')
	cursor.execute('''
		INSERT INTO catalogo VALUES(
			12,
			"Spider-Man: Lejos de casa",
			'Película',
			'Tras los acontecimientos de "Vengadores: Endgame", Spider-Man debe enfrentarse a nuevas amenazas en un mundo que ha cambiado para siempre.',
			'Aventura - Acción',
			'Jon Watts',
			2019,
			'7',
			'visto',
			'imgs/spiderman lejos de casa.png'
		)
	''')
	cursor.execute('''
		INSERT INTO catalogo VALUES(
			13,
			"The Quintessential Quintuplets",
			'Película',
			'El tutor adolescente Fuutaro Uesugi debe elegir finalmente entre las 5 hermanas Nakano, que tienen sentimientos por él, en el próximo festival cultural de la escuela; el evento que le llevará a casarse con una de ellas en un Flash-Forward.',
			'Comedia - Drama',
			'Masato Jinbô',
			2022,
			0,
			'sin ver',
			'imgs/las quintillizas.png'
		)
	''')
	cursor.execute('''
		INSERT INTO catalogo VALUES(
			14,
			"Jujutsu Kaisen 0",
			'Película',
			'Rika, amiga de la infancia de Yuuta Okkotsu, murió en un accidente automovilístico. Su espíritu permanece con él, más ya no es la dulce niña que él conocía. Se manifiesta como una entidad monstruosa y poderosa que lo protege ferozmente.',
			'Acción - Fantasía',
			'Sunghoo Park',
			2021,
			'8',
			'para re-ver',
			'imgs/jjk 0.png'
		)
	''')
	cursor.execute('''
		INSERT INTO catalogo VALUES(
			15,
			"My Hero Academia: Heroes Rising",
			'Película',
			'Un grupo de jóvenes que aspiran a convertirse en superhéroes profesionales, luchan en un mundo lleno de personas con habilidades peculiaridades.',
			'Acción - Fantasía',
			'Kenji Nagasaki',
			2019,
			'8',
			'visto',
			'imgs/mha heroes rising.png'
		)
	''')
	cursor.execute('''
		INSERT INTO catalogo VALUES(
			16,
			"My Hero Academia: You're Next",
			'Película',
			'Izuku Midoriya, un estudiante del instituto U.A. que aspira a ser el mejor héroe posible, se enfrenta al villano que imita al héroe que una vez admiró.',
			'Acción - Aventura - Ciencia ficción',
			'Tensa Okamura',
			2024,
			0,
			'ver mas tarde',
			'imgs/mha you are next.png'
		)
	''')
	cursor.execute('''
		INSERT INTO catalogo VALUES(
			17,
			"Mob Psycho 100",
			'Serie',
			'Un joven con poderes psíquicos intenta llevar una vida normal y mantener a raya sus poderes, sin embargo no puede evitar meterse en problemas constantemente.',
			'Acción - Drama',
			'Yuzuru Tachikawa - Katsuya Shigehara',
			2016,
			0,
			'viendo',
			'imgs/mob 100.png'
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

def ver1 (id):
	global DB_NAME

	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()
	cursor.execute(f"SELECT * FROM catalogo WHERE id = {id} LIMIT 1")
	ver = cursor.fetchall()
	conn.close()
	
	return ver

def actualizar(l_id, titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen):
	global DB_NAME
	
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute('''
		UPDATE catalogo
		SET titulo = ?,
		tipo = ?,
		descripcion = ?,
		genero = ?,
		director = ?,
		ano_estreno = ?,
		calificacion = ?,
		estado = ?,
		imagen = ?
		WHERE id = ?
	''', (titulo, tipo, descripcion, genero, director, ano_estreno, calificacion, estado, imagen, l_id))

	conn.commit()
	conn.close()



def eliminar(l_id):
	global DB_NAME
	
	conn = sqlite3.connect(DB_NAME)
	cursor = conn.cursor()

	cursor.execute('DELETE FROM catalogo WHERE id = ?', (l_id,))

	conn.commit()
	conn.close()