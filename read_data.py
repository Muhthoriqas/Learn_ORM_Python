from schema import db,Movie
from datetime import date

db.connect()
template = "{movie.title} ({movie.release_date}) | Rating: {movie.rating}/10"

print("*" * 50 + "\n")
print(" All titles\n")
for movie in Movie.select():
    print(template.format(movie=movie))

print("-" * 40)
print('\n1. Start with "Blade" \n')
for movie in Movie.select().where(Movie.title.startswith("Blade")):
    print(template.format(movie=movie))

print("-" * 40)
print ("\n2. Released after 1971 \n ")
for movie in Movie.select().where(Movie.release_date > date ( 1971 ,1, 1 )):
    print ( template.format ( movie=movie ) )

print ("-" * 40)
print ("\n3. Sorted by name  \n ")
for movie in Movie.select ().order_by(Movie.title.asc()) :
    print (template.format (movie=movie ))

print ( "-" * 40 )
print ( "\n4. Sorted by highest rating \n " )
for movie in Movie.select().order_by(Movie.rating.desc()):
    print ( template.format ( movie=movie ))

print ( "-" * 40 )
print ( "\n4. Sorted by lowest rating \n " )
for movie in Movie.select().order_by( Movie.rating.asc() ):
    print ( template.format ( movie=movie ))

print("\n" + "*" * 50 + "\n")
