from app import app
import urllib.request,json
from .models import movie

Movie = movie.Movie

# getting api key

api_key = app.config['MOVIE_API_KEY']

# getting the movie base url
base_url = app.config['MOVIRE_API_BASE_URL']

def get_movies(category):
    '''
    Function that gets json response to our url request
    '''
    get_movies_url = base_url.format(category,api_key) # method that replaces {} placeholder in the api url with my api key

    with urllib.request.urlopen(get_movies_url) as url: #function that sends a request as a url
        get_movies_data = url.read() # reads the response and stores it in a variable
        get_movies_response = json.loads(get_movies_data) # converts the json reponse to a python dictionary

        movie_results = None

        if get_movies_response['results']:
            movie_results_list = get_movies_response['results']
            movie_results = process_results(movie_results_list)

def process_results(movie_list):
    '''
    Function that processes the movies result and transform them to a list of objects
    Args:
        movie_results: A list of dictionaries that contain movie details

    Returns: 
        movie_results: A list of movie objects
    '''
    movie_results = [] # dictionary that stores new created objects
    for movies_item in movie_list: # loop through the list 
        id = movies_item.get('id')
        title = movies_item.get('original_title')
        overview = movies_item.get('overview')
        poster = movies_item.get('poster_path')
        vote_average = movie_list.get('vote_average')
        vote_count = movies_item.get('vote_count')

        if poster:
            movie_object = Movie(id, title, overview, poster, vote_average, vote_count)
            movie_results.append(movie_object)

    return movie_results