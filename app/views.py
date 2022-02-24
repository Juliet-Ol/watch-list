from flask import render_template
from app import app
from .request import get_movies

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    popular_movies = get_movies('popular')
    # print(popular_movies)
    # message = 'Hello world' #new variable
    # return render_template('index.html', message = message)
    # popular_movies = get_movies('popular')
    upcoming_movie = get_movies('upcoming')
    title = 'Home - Welcome to the best Movie Review website online'
    return render_template('index.html', title = title, popular = popular_movies, upcoming = upcoming_movie)

@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View movie page function that returns the movie detail page and its data
    '''
    return render_template('movie.html', id = movie_id)