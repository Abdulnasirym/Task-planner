from flask_wtf import FlaskForm
from datetime import datetime
from wtforms import StringField, PasswordField, TextAreaField, DateTimeField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class TaskForm(FlaskForm):
	title = StringField('Title', validators=[DataRequired(), Length(max=100)])
	description = TextAreaField('Description', validators=[Length(max=500)])
	start_date = DateTimeField('Start Date', format='%Y-%m-%d', validators=[DataRequired()])
	due_date = DateTimeField('Due Date', format='%Y-%m-%d', validators=[DataRequired()])
	completed= BooleanField('completed')
	submit = SubmitField('Add Task')

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired(), Length(min=5, max=25)])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign up')

class LoginForm(FlaskForm):
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField('Password', validators=[DataRequired()])
	submit = SubmitField('Login')