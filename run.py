from flask import Flask,render_template,url_for

app=Flask(__name__)

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

if __name__=='__main__':
	app.run(debug=True)