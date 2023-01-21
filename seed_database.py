
"""Script to seed database."""

#This is a module from Python’s standard library. It contains code related to 
# working with your computer’s operating system.

# You’ll need to import json to load the data in data/movies.json.
import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb ratings")
os.system("createdb ratings")

model.connect_to_db(server.app)
model.db.create_all()

# Load movie data from JSON file
with open('data/movies.json') as file:
    movie_data = json.loads(file.read())


# Create movies, store them in list so we can use them
# to create fake ratings later
movies_in_db = []
for movie in movie_data:
   
    title = movie["title"],
    overview = movie["overview"],
    poster_path = movie["poster_path"],
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")
    # what's in the dictionary currently is '2019-09-20'
    # Y = Year with century as a decimal number.
    # m = Month as a zero-padded decimal number.
    # d = Day of the month as a zero-padded decimal number.
    # We're giving the "translation" for how to interpret what is currently in the dict. 
    
    movie_to_add = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(movie_to_add)

#for every dict in the list from .json, put data through function from crud.py to create movie objects

#if you want to add a list, you need to have .add_all. Session.add can only take an object. 
# you must tell it to pull db from model, or it doesn't know what db is. 
model.db.session.add_all(movies_in_db)
model.db.session.commit()

for n in range(10):
    email = f"user{n}@test.com"
    password = "pass"

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for num in range(10):
        random_movie_choice = choice(movies_in_db)
        random_score = randint(1, 5)
        random_rating = crud.create_rating(user, random_movie_choice, random_score)
        model.db.session.add(random_rating)

model.db.session.commit()


# Get the first rating from the database --> 
    # rating = Rating.query.first()

# Make sure you can access the rating’s user and movie attributes
    # rating.user 
    # rating.movie 

# Print the scores of all the ratings that rating.user has made
###last step might be to assign rating to a variable###