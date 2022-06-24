from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, HiddenField, StringField
from wtforms.validators import InputRequired


class ScForm(FlaskForm):
    id_field = HiddenField()
    stress = SelectField('Your average daily stress level', [InputRequired()],
        choices = [ (1, '1'), (2, '2'), (3, '3'),
        (4, '4'), (5, '5'), (6, '6'), (7, '7'), 
        (8, '8'), (9, '9'), (10, '10')])
    sleep = SelectField('Your quality of sleep', [InputRequired()],
        choices = [ (1, '1'), (2, '2'), (3, '3'),
        (4, '4'), (5, '5'), (6, '6'), (7, '7'), 
        (8, '8'), (9, '9'), (10, '10')])
    diet = SelectField('How well balanced is your diet?', [InputRequired()],
        choices = [ (1, '1'), (2, '2'), (3, '3'),
        (4, '4'), (5, '5'), (6, '6'), (7, '7'), 
        (8, '8'), (9, '9'), (10, '10')])
    exercise = SelectField('Regularity of physical activity/exercise', [InputRequired()],
        choices = [ (1, '1'), (2, '2'), (3, '3'),
        (4, '4'), (5, '5'), (6, '6'), (7, '7'), 
        (8, '8'), (9, '9'), (10, '10')])
    outdoors = SelectField('Regularity of time spent outdoors', [InputRequired()],
        choices = [ (1, '1'), (2, '2'), (3, '3'),
        (4, '4'), (5, '5'), (6, '6'), (7, '7'), 
        (8, '8'), (9, '9'), (10, '10')])
    social = SelectField('Your level of satisfaction with social interactions', [InputRequired()],
        choices = [ (1, '1'), (2, '2'), (3, '3'),
        (4, '4'), (5, '5'), (6, '6'), (7, '7'), 
        (8, '8'), (9, '9'), (10, '10')])
    spirit = SelectField('Participation in a spiritual practice', [InputRequired()],
        choices = [ (1, '1'), (2, '2'), (3, '3'),
        (4, '4'), (5, '5'), (6, '6'), (7, '7'), 
        (8, '8'), (9, '9'), (10, '10')])
    submit = SubmitField('Submit')
    
    