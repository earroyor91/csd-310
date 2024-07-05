import mysql.connector
        
config = {
	"user": "root",
	"password": "ezacess1!",
	"host": "127.0.0.1",
	"database": "movies",
	"raise_on_warnings": True
}

db = mysql.connector.connect(**config)

cursor = db.cursor()

def show_films(cursor, title):
    cursor = db.cursor()

    cursor.execute("""SELECT film_name as Name, film_director as Director, genre_name as Genre, 
                   studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id = genre.genre_ID 
                   INNER JOIN studio ON film.studio_ID = studio.studio_id""")
    
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

show_films(cursor, "DISPLAYING FILMS")

sql_INSERT = ("""INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
       VALUES ('Planet of the Apes', '2001', '120', 'Tim Burton', 1, 2)""")

cursor.execute(sql_INSERT)

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

sql_UPDATE = ("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")

cursor.execute(sql_UPDATE)

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER UPDATE - Changed Alien to Horror")

sql_DELETE = ("DELETE FROM film WHERE film_name = 'Gladiator'")

cursor.execute(sql_DELETE)

db.commit()

show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

db.close()