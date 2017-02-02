import media
from tmdb3 import set_key
from tmdb3 import set_cache
from tmdb3 import Movie as Movie_db
import os
import fresh_tomatoes

set_key('XXX') #Insert API key for TMDB3 website
set_cache('null')

list_of_movies = [] 
for i in range(11,23): 
    
    #Taking 12 movies from Movie_db and storing the data in list_of movies
    
    curr_movie = Movie_db(i) 
    
    title = (curr_movie.title)
    story_line = (curr_movie.overview)
    poster = (curr_movie.poster.geturl())
    trailer = (curr_movie.youtube_trailers[0].geturl())
    movie_instance = media.Movie(title,story_line,poster,trailer) 
    
    list_of_movies.append(movie_instance) #adding instances of Movie() class to list_of_movies
    
os.chdir(r"C:\Users\venkata.pushpak\Documents\Udacity\FSD\Project 1")
fresh_tomatoes.open_movies_page(list_of_movies)