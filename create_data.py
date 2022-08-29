import os
from platform import release
from turtle import title

os.remove('movies.db')

from datetime import date
from schema import db, Movie

db.connect()
db.create_tables([Movie])

blade_runner = Movie.create(title="Blade Runner",release_date = date(1982,6,25))
blade_runner.rating = 10

blade_runner.save()

movies = (
    ( "Blade Runner 2049" , 2018 , 9 ) ,
    ( "2001 : a space odyssey " , 1968 , 10 ) ,
    ( "Godzilla vs. Hedorah " , 1968 , 6 ) ,
    ( "Silent Running " , 1972 , 8 ) ,
)

for movie in movies:

    Movie.create(title = movie[0],release_date=date(movie[1],1,1),rating=movie[2])