# Udacity-Movie-Trailer-Website

This is the final project of the course Programming Foundations With Python in Udacity. The goal of this project is to create a website that displays your favorite movies and play its trailer upon a click.

A python module tmdb3 is used in this project to get data (link: https://pypi.python.org/pypi/tmdb3/). 
To install, download the package and type python setup.py install in your command line from its path
To use it, you must register in this website https://www.themoviedb.org/documentation/api and get your key to access the movie database. 

##Custom Classes and Modules:

###media.py
Contains class Movie() with title, storyline, poster and youtube-trailer-url as parameters for the constructor of the class and contains show_trailer() method to display the trailer of the movie

###fresh_tomatoes.py
Contains the method open_movies_page() method that takes list of instances of class Movie() as a parameter. Also generates required html. 

Once you set up the api key, insert it in project.py and run the application. fresh_tomatoes.html will open displaying the movies and trailers will play upon clicking any movie. 
You are free to use other features of tmdb3 to get movies by person, director, name etc., 
