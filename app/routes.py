from app import app

@app.route('/')
def home():
	return "hello abdulnasir na Aminatu"

@app.route('/<name>')
def page(name):
	return f"hello {name}"