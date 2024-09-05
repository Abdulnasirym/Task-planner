from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model, UserMixin):
	__tablename__ = 'user'

	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password_hash = db.Column(db.String(120), nullable=False)
	created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	updated_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)

	# Establishing one to many relationship
	tasks = db.relationship('Task', backref='owner', lazy=True)

	# def set_password(self, password):
	# 	self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return f'<user {self.username}>'


class Task(db.Model):
	__tablename__ = 'tasks'

	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(500), nullable=False)
	start_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	due_date = db.Column(db.DateTime)
	completed = db.Column(db.Boolean, default=False)
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f'<Task {self.title}>'
