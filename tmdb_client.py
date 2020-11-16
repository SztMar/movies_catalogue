import requests
import json


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular/"
    api_token = "115d54b112f4215ade3207a23244732e"
    full_url = f'{endpoint}?api_key={api_token}'
    headers = {
        "Authorization": f"{api_token}"
    }
    response = requests.get(full_url)
    
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
   
    return data["results"][:how_many]


