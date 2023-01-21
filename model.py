"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# I want my class to inherit everything that exists in db.Model 
# (db = the SQLAlch. object) -- this is the magic behind the scenes
class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    ratings = db.relationship("Rating", back_populates="user")

    def __repr__(self):
        """Show useful info about user."""
        return f'<User user_id={self.user_id} email={self.email}>'
    

class Movie(db.Model):
    """"Movie"""
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.DateTime)
    poster_path = db.Column(db.String)

    ratings = db.relationship("Rating", back_populates="movie")
    
    def __repr__(self):
        return f"<Movie id: {self.movie_id} Title: {self.title}>"



class Rating(db.Model):
    """A Rating"""
    __tablename__ = "ratings"

    rating_id = db.Column(db.Integer, autoincrement= True, primary_key=True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


    movie = db.relationship("Movie", back_populates="ratings")
    user = db.relationship("User", back_populates="ratings")


    def __repr__(self):
     """Show userful info about rating"""
     return f'<Rating rating_id={self.rating_id} Score={self.score}>'


def connect_to_db(flask_app, db_uri="postgresql:///ratings", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # overwhelming this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False) #<- this can be deleted later if we want it 
    # to return to echo = true so it prints out a ton more info
