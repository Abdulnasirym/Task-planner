from dotenv import load_dotenv
import os

load_dotenv()

class Config:
	# Database configurations
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'its-a-secret'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	#Email configurations
	MAIL_SERVER = 'smtp.office365.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USE_SSL = False
	MAIL_USERNAME = os.environ.get('OUTLOOK_EMAIL')
	MAIL_PASSWORD = os.environ.get('OUTLOOK_PASSWORD')
	MAIL_DEFAULT_SENDER = os.environ.get('OUTLOOK_EMAIL')

