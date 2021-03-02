from datetime import datetime
from flask import current_app, abort, render_template


# @app.route("/")
def home_page():
    today = datetime.today()
    day_name = today.strftime("%A")
    return render_template("home.html", day = day_name)

# @app.route("/movies", endpoint="movies_endpoint")
def movies_page():
    db = current_app.config["db"]
    movies = db.get_movies()
    return render_template("movies.html", movies=sorted(movies))

def movie_page(movie_key):
    """use the movie key to get the movie from the database and send to the template."""
    db = current_app.config["db"]
    movie = db.get_movie(movie_key)
    if movie is None:
        abort(404)
    return render_template("movie.html", movie=movie)
