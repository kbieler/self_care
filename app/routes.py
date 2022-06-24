from app import app
from flask import render_template, Blueprint, request, redirect, url_for, flash
import requests as r
from flask_login import login_required, current_user
from .templates.services import getQuote, ParkForm, graph_db
from googlesearch import search


@app.route('/')
def home():
    context = getQuote()
    return render_template('index.html', **context)


@app.route('/about', methods=['GET', 'POST'])
def about():
    pform = ParkForm()
    if request.method == 'POST':
        if pform.validate_on_submit():
            local = ('public parks near ' + pform.location.data)
            for p in search(local, tld="co.in", num=5, stop=5, pause=2):
                print(p)
        flash('Sorry, there was an issue with the search.')
        return render_template('about.html', form=pform, parks=p)
    return render_template('about.html', form=pform)

@app.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    #context = graph_db()
    return render_template('results.html')#, **context)

   