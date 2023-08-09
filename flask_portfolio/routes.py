from flask import render_template,url_for,redirect,request
from flask_portfolio import app
from flask_portfolio.forms import ContactForm

@app.route('/')
@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/works')
def works():
	return render_template('works.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
	form=ContactForm()
	if request.method=='POST':
		username=form.username.data
		email=form.email.data
		text=form.text.data
		return redirect(url_for('home'))
	return render_template('contact.html',form=form)