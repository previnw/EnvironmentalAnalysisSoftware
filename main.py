from flask import Flask, render_template, url_for, jsonify, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
import datetime, json

app = Flask(__name__)

class data(FlaskForm):
	sensorName = StringField('sensorName')
	reading = DecimalField('reading')


posts = [
	{
		'author': 'Previn Wong',
		'title': 'Blog Post 1',
		'content': 'First post content',
		'date_posted': 'September 17, 2018'
	},
	{
		'author': 'Dan P',
		'title': 'Blog Post 2',
		'content': 'Second post content',
		'date_posted': 'September 18, 2018'
	},
	{
		'author': 'Mike Lee',
		'title': 'Blog Post 3',
		'content': 'Third post content',
		'date_posted': 'September 19, 2018'
	},
	{
		'author': 'Conrad',
		'title': 'Blog Post 4',	
		'content': 'Forth post content',
		'date_posted': 'September 20, 2018'
	},
	{
		'author': 'Josh',
		'title': 'Blog Post 5',
		'content': 'Fifth post content',
		'date_posted': 'September 21, 2018'
	}
]

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/datasheets')
def datasheets():
	return render_template('datasheets.html', title='Datasheet')

@app.route('/details')
def details():
	return render_template('details.html', posts=posts, title='Details')

@app.route('/about')
def about():
	return render_template('about.html', title='About')

@app.route('/jsontest', methods = ['POST', 'GET'])
def jsontest():
	temp = request.form['Temperature']
	humi = request.form['Humidity']

	if humi=="100":
		
		return "humidity fine"
	elif humi=="200":
		return "humidity high!"

if __name__ == '__main__':
	app.run(debug=True)

