import requests
import json


API_TOKEN = "115d54b112f4215ade3207a23244732e"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular/"
    full_url = f'{endpoint}?api_key={API_TOKEN}'
    response = requests.get(full_url)
    
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}/"
    full_url = f'{endpoint}?api_key={API_TOKEN}'
    response = requests.get(full_url)
    response.raise_for_status()
    return response.json()


def get_poster_url(poster_api_path, size="w324"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    full_url = f'{endpoint}?api_key={API_TOKEN}'
    response = requests.get(full_url)
    
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    full_url = f'{endpoint}?api_key={API_TOKEN}'
    response = requests.get(full_url)
    
    return response.json()["cast"]

def get_movies(how_many, list_type='popular'):
    data = get_movies_list(list_type)
   
    return data["results"][:how_many]

def get_movie_images(movie_id):
     endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
     full_url = f'{endpoint}?api_key={API_TOKEN}'
     response = requests.get(full_url)
     

     return response.json()

