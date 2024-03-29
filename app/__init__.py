from flask import Flask
from config import Config
from .auth.routes import auth
from .survey.routes import surveyed
from .models import db, login
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap



app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth)
app.register_blueprint(surveyed)



db.init_app(app)
migrate = Migrate(app, db)
Bootstrap(app)
login.init_app(app)
login.login_view = 'auth.login'
login.login_message = 'Please log in to view this page.'
login.login_message_category = 'danger'




from . import routes

