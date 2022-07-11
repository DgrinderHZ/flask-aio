
import os
from flask import Flask
import flask_login

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager



app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

# create the database and the db table

uri = os.getenv("DATABASE_URL")
# or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
    app.config['SQLALCHEMY_DATABASE_URI'] = uri

db.create_all()

#############
### APPS  ###
#############

from project.auth.views import bp as auth_bp, login
app.register_blueprint(auth_bp)

from project.home.views import bp as home_bp
app.register_blueprint(home_bp)

#############
### LOGIN  ##
#############

login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    from project.models import User
    
    return User.query.get(user_id)