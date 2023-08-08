from flask import render_template,url_for
from flask_portfolio import app

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/works')
def works():
	return render_template('works.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')