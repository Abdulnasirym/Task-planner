from app import app, db
from flask import render_template, request, flash, redirect, url_for, session
from app.models import Task, User
from app.email import send_email
from app.forms import TaskForm, RegistrationForm, LoginForm
from flask_login import current_user, login_required, login_user
from werkzeug.security import generate_password_hash, check_password_hash

# Routes for task management

# Viewing tasks
@app.route('/')
@app.route('/task')
def view_tasks():
	tasks = Task.query.all()
	return render_template('tasks.html', tasks=tasks)

# Adding task
@login_required
@app.route('/task/new', methods=['GET', 'POST'])
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            title=form.title.data,
            description=form.description.data,
            start_date=form.start_date.data,
            due_date=form.due_date.data,
            completed=form.completed.data,
            user_id=current_user.id
        )
        db.session.add(task)
        db.session.commit()
        flash('Your task has been created!', 'success')
        return redirect(url_for('index'))  # This should redirect to the home or task list
    return render_template('task_form.html', form=form)

# updating task
@app.route('/task/<int:task_id>/update', methods=['GET','POST'])
def update_task(task_id):
	task = Task.query.get_or_404(task_id)
	if request.method == 'POST':
		task.title = request.form['title']
		task.description = request.form['description']
		task.due_date = request.form['due_date']
		task.completed = 'completed' in request.form
		db.session.commit()
		return redirect(url_for('view_tasks'))
	return render_template('update_task.html', task=task)

# Delete individual task
@app.route('/task/<int:task_id>/delete', methods=['POST', 'GET'])
def delete_task(task_id):
	task =Task.query.get_or_404(task_id)
	db.session.delete(task)
	db.session.commit()
	return redirect(url_for('view_tasks'))

# User registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = generate_password_hash(form.password.data)
		user = User(username=form.username.data,
			email=form.email.data,
			password_hash=hashed_password
		)
		try:
		    db.session.add(user)
		    db.session.commit()
		except Exception as e:
		    db.session.rollback()
		    flash(f'Error: {e}', 'danger')
		    return redirect(url_for('view_tasks'))
	return render_template('register.html', form=form)

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user and user.check_password(form.password.data):
			login_user(user)
			flash('Login successful!', 'success')
			return redirect(url_for('view_tasks'))
		else:
			flash('Login unsuccessful.Please check email and password', 'danger')
	return render_template('login.html', form=form)

# Logout route
@login_required
@app.route('/logout')
def logout():
	session.pop('user.id', None)
	flash('You have been logged out')
	return redirect(url_for('login'))

# sending email
@app.route('/send-email')
def send_test_email():
	send_email(
		subject="Test Email",
		recipients=["abdulnasiry05@gmail.com"],
		body="This is a test email sent from flask."
		)
	return "Email sent!"
