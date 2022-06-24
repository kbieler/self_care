from flask import Blueprint, render_template, request, redirect, url_for, flash, Flask
from .surveyform import ScForm
from app.models import Surveys, db
from flask_login import login_required, current_user



surveyed = Blueprint('survey', __name__, template_folder='srv_templates', url_prefix='/survey', static_folder='srv_static')

@surveyed.route('/survey', methods=['GET', 'POST'])
@login_required
def survey():
    sform = ScForm()
    if sform.validate_on_submit():
        stress = request.form['stress']
        sleep = request.form['sleep']
        diet = request.form['diet']
        exercise = request.form['exercise']
        outdoors = request.form['outdoors']
        social = request.form['social']
        spirit = request.form['spirit']

        record = Surveys(stress, sleep, diet, exercise, outdoors, social, spirit)
        db.session.add(record)
        db.session.commit()

        message = "Thank you! Your input has been submitted."
        return render_template('survey.html', message=message)
    
    else:
        for field, errors in sform.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(sform, field).label.text,
                    error
                ), 'error')
        return render_template('survey.html', sform=sform)
