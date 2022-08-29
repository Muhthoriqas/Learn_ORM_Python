from datetime import date
from schema import Movie

template = "{movie.title} ({movie.release_date}) {movie.rating} /10"
Movie.create(title = "The Matrix", release_date= date ( 1999 , 3 , 31) ,rating= 5)

bad_movie= Movie.create(title = "Mortal Kombat : Annihilation", release_date= date( 1997 ,1 , 21 ), rating = 9)

print ( "-" *  40 )
print ("Sorted by rating why is The Matrix so low and MK : A so high ?")

for movie in Movie.select ().order_by ( Movie.rating.desc () ) :
    print (template.format ( movie=movie ) )

Movie.update(rating= 10).where(Movie.title == "The Matrix").execute()
bad_movie.rating = 5
bad_movie.save()

print ("-"* 40 )
print ("\nSorted by rating ( better ! ) \n " )
for movie in Movie.select ( ).order_by( Movie.rating.desc ( ) ) :
    print ( template.format (movie=movie) )