"""Server for movie ratings app."""

# Flask redirect is defined as a function or utility in Flask which allows 
# developers to redirect users to a specified URL and assign a specified status 
# code. Syntax --> flask.redirect(<location>,<status-code>, <response> )

from flask import Flask, request, render_template, flash, session, redirect
# In order to connect to the database, you need to...
from model import connect_to_db, db
import crud 

# You’ll also want to import something from jinja2 called StrictUndefined. 
# You’ll use it to configure a Jinja2 setting to make it throw errors for 
# undefined variables (by default it fails silently — without showing you an
# error message! yuck!)
from jinja2 import StrictUndefined



app = Flask(__name__)
# Need to configure the Flask instance. It’ll need a secret key (otherwise, 
# flash and session won’t work). Jinja2 also needs configured here as well:
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Return homepage"""

    return render_template("homepage.html")


@app.route('/movies')
def show_movies():
    """View all movies"""

    movies = crud.get_all_movies()

    return render_template("movies.html", movies=movies)


@app.route('/movies/<movie_id>')
def show_movie_detials(movie_id):
    """Displays the movie title, overview, and movie poster"""

    movie = crud.get_movie_by_id(movie_id) 

    return render_template("movie_details.html", movie = movie)


@app.route('/users')
def show_users():
    """View all users"""

    users = crud.get_all_users()

    return render_template("users.html", users = users)


@app.route('/users/<user_id>')
def show_user_detials(user_id):
    """Currently displays the user email. Later I may add the functionality to 
    show the user's rating"""

    user = crud.get_user_by_id(user_id) 

    return render_template("user_details.html", user = user)



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
