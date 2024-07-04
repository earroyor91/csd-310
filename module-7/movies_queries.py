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

cursor.execute("SELECT * FROM studio")

studios = cursor.fetchall()

print("\n-- DISPLAYING Studio RECORDS --")

for studio in studios:
	print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))

cursor.execute("SELECT * FROM genre")

genres = cursor.fetchall()

print("-- DISPLAYING Genre RECORDS --")

for genre in genres:
	print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))

cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <120")

films = cursor.fetchall()

print("-- DISPLAYING Short Film RECORDS --")

for film in films:
	print("Film Name: {}\nRuntime: {}\n".format(film[0], film[1]))

cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

directors = cursor.fetchall()

print("-- DISPLAYING Director RECORDS in Order --")

for director in directors:
	print("Film Name: {}\nDirector: {}\n".format(director[0], director[1]))

db.close()