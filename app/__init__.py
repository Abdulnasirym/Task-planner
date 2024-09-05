from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager, UserMixin

# Create an Instance of Flask
app = Flask(__name__)
app.config.from_object('config.Config')
app.config['Debug'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# initialize the mail extension
from flask_mail import Mail
mail = Mail(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

if __name__ == "__main__":
	app.run()

from app import routes