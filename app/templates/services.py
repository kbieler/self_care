import requests as r
import mysql.connector
import numpy as np
import matplotlib.pyplot as plt
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from config import Config


class Quote:
    def __init__(self, apidict):
        self.quoted = apidict['q']
        self.author = apidict['a']
        self.formatted = apidict['h']

def getQuote():
    data = r.get('https://zenquotes.io/api/random')
    if data.status_code == 200:
        data = data.json()
    else:
        return 'invalid api request'      

    api_quotes = data
    for q in api_quotes:
        quotes = Quote(q)

    return {
        'daily_quote': quotes.quoted,
        'credit': quotes.author
    }

class ParkForm(FlaskForm):
    location = StringField('In what city, state are you located?', validators=[DataRequired()])
    submit = SubmitField()


def graph_db():

    mycursor = Config.mydb.cursor()

    mycursor.execute("select stress, sleep, diet, exercise, outdoors, social, spirit from surveys")
    result= mycursor.fetchall

    stress = []
    sleep = []
    diet = []
    exercise = []
    outdoors = []
    social = []
    spirit = []

    for i in mycursor:
        stress.append(i[0])
        sleep.append(i[1])
        diet.append(i[2])
        exercise.append(i[3])
        outdoors.append(i[4])
        social.append(i[5])
        spirit.append(i[6])

    print("Stress = ", stress)
    print("Sleep = ", sleep)
    print("Diet = ", diet)
    print("Exercise = ", exercise)
    print("Outdoors = ", outdoors)
    print("Social = ", social)
    print("Spiritual = ", spirit)

    plt.bar(stress, sleep, diet, exercise, outdoors, social, spirit)
    plt.ylim(0, 10)
    plt.xlabel("Self-Care Categories")
    plt.ylabel("Ratings")
    plt.title("Self-Care Survey Results")
    
    return { 'graph': plt.show() }




