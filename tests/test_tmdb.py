import tmdb_client
from unittest.mock import Mock
import app
from app import app
import pytest

test_list = "top_rated"

def test_get_poster_url_uses_default_size():
   # Przygotowanie danych
   poster_api_path = "some-poster-path"
   expected_default_size = 'w324'
   # Wywołanie kodu, który testujemy
   poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path)
   # Porównanie wyników
   assert expected_default_size in poster_url
   #assert poster_url == "https://image.tmdb.org/t/p/w324/some-poster-path"

def test_get_movies_list(monkeypatch):
   # Lista, którą będzie zwracać przysłonięte "zapytanie do API"
   mock_movies_list = ['Movie 1', 'Movie 2']

   requests_mock = Mock()
   # Wynik wywołania zapytania do API
   response = requests_mock.return_value
   # Przysłaniamy wynik wywołania metody .json()
   response.json.return_value = mock_movies_list
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)


   movies_list = tmdb_client.get_movies_list(list_type="popular")
   assert movies_list == mock_movies_list

def test_get_single_movie_id(monkeypatch):
   mock_movie_id = 1

   requests_mock = Mock()  
   response = requests_mock.return_value   
   response.json.return_value = mock_movie_id
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movie_id = tmdb_client.get_single_movie(movie_id=1)
   assert movie_id == mock_movie_id

def test_get_movie_images_id(monkeypatch):
   mock_movie_id = 1

   requests_mock = Mock()  
   response = requests_mock.return_value   
   response.json.return_value = mock_movie_id
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movie_id = tmdb_client.get_movie_images(movie_id=1)
   assert movie_id == mock_movie_id

def test_get_single_movie_cast_id(monkeypatch):
   mock_movie_id = 1

   requests_mock = Mock()  
   response = requests_mock.return_value   
   response.json.return_value = mock_movie_id
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)

   movie_id = tmdb_client.get_single_movie(movie_id=1)
   assert movie_id == mock_movie_id

def test_get_movies_by_default_movies():
   # Przygotowanie danych
   how_many = 1
   adult = False

   # Wywołanie kodu, który testujemy
   data = tmdb_client.get_movies(how_many= how_many, list_type="upcoming")
   assert data[0]['adult'] == adult

@pytest.mark.parametrize("test_input",['now_playing', 'popular','top_rated', 'upcoming'])
def test_homepage_movie_list(monkeypatch, test_input):
   
   api_mock = Mock()
   api_mock.return_value={'results': []}
   monkeypatch.setattr("tmdb_client.call_tmdb_api", api_mock)

   with app.test_client() as client:
       print(test_input)
       response = client.get(f'/?list_type={test_input}')
       assert response.status_code == 200
       api_mock.assert_called_once_with(f'movie/{test_input}')

