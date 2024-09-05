from app import app, db
from datetime import datetime
from app.models import User, Task

# create a test context
with app.app_context():
	# Create  the tables if they don't exist
	db.create_all()

	# Test adding user
	user1 = User(username='abdulnirr',
		email='adu@gmail.com')
	user1.set_password("audu")
	db.session.add(user1)
	db.session.commit()

	# Checks if the user was added
	user = User.query.filter_by(username='abdulnirr').first()
	if user:
		print(f"User {user.username} was added to the database")
	else:
		print("failed to add user to the database")

	# Test adding tasks
	task1 = Task(title='A test',
		description='Just testing the database',
		due_date=datetime.utcnow(), 
		user_id=user1.id,
		completed=True,
		user_email=user1.email
	)
	db.session.add(task1)
	db.session.commit()

	# Checks if task was added
	task = Task.query.filter_by(title='A test').first()
	if task:
		print(f"Task {task.title} was added to the database")
	else:
		print("Failed to add task to the database")

	def test_password_hashing():
	    user = User(username="testuser")
	    
	    # Set the password
	    user.set_password("my_secure_password")
	    
	    # Print out the hashed password
	    print("Hashed Password:", user.password_hash)
	    
	    # Check if the password matches the hash
	    assert user.check_password("my_secure_password") == True, "Password check failed!"
	    assert user.check_password("wrong_password") == False, "Password check should have failed but passed!"

	    print("Password hashing test passed!")
	# Run the test
	test_password_hashing()


