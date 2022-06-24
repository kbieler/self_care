from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import LoginManager, UserMixin
from uuid import uuid4
from werkzeug.security import generate_password_hash

db = SQLAlchemy()

login = LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)

class User(db.Model, UserMixin):
    id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    created = db.Column(db.DateTime, default=datetime.utcnow())
    api_token = db.Column(db.String(100))
   
    def __init__(self, username, email, password, first_name='', last_name= ''):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())
        self.password = generate_password_hash(password)


class Surveys(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stress = db.Column(db.Integer, nullable=False)
    sleep = db.Column(db.Integer, nullable=False)
    diet = db.Column(db.Integer, nullable=False)
    exercise = db.Column(db.Integer, nullable=False)
    outdoors = db.Column(db.Integer, nullable=False)
    social = db.Column(db.Integer, nullable=False)
    spirit = db.Column(db.Integer, nullable=False)

    def __init__(self, stress, sleep, diet, exercise, outdoors, social, spirit):
        self.stress = stress
        self.sleep = sleep
        self.diet = diet
        self.exercise = exercise
        self.outdoors = outdoors
        self.social = social
        self.spirit = spirit


