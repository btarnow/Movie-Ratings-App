"""Models for movie ratings app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#I want my class to inherit everything that exists in db.Model 
# (db = the SQLAlch. object) -- this is the magic behind the scenes
class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __repr__(self):
        """Show useful info about user."""
        return f'<User user_id={self.user_id} email={self.email}>'
    

class Movie(db.Model):
    """"Movie"""
    __tablename__ = "movies"

    movie_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String)
    overview = db.Column(db.Text)
    release_date = db.Column(db.Date------:LKJLKSDJFLSjdfk???)

    

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
    # TOOOOOO ANNOYINGGGGG this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app, echo=False) #<- this can be deleted later if we want it to return to echo = true so it prints out a ton more info
