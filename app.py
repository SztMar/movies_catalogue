from flask import Flask, render_template, url_for, request, redirect
import requests
import tmdb_client
import random
from random import randrange




app = Flask(__name__)
movie_list= ['now_playing', 'popular','top_rated', 'upcoming']

@app.route('/')
def homepage():
    rnd = randrange(8,30)
    selected_list = request.args.get('list_type', "popular")
    
    if selected_list in movie_list:
        movies = tmdb_client.get_movies(how_many=rnd, list_type=selected_list )    
        return render_template("homepage.html", movies=movies, current_list=selected_list, movie_list=movie_list)
    
    else:
        return redirect("/")   

    

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images['backdrops'])
    return render_template("movie_details.html", cast = cast_details['cast'], movie = details, selected_backdrop=selected_backdrop)


if __name__ == '__main__':
    app.run(debug=True)