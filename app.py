from flask import Flask, render_template
import requests
import tmdb_client
from random import randrange



app = Flask(__name__)


@app.route('/')
def homepage():
    rnd = randrange(20)
    movies = tmdb_client.get_movies(rnd)
    return render_template("homepage.html", movies=movies)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    return render_template("movie_details.html")


if __name__ == '__main__':
    app.run(debug=True)