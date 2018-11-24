from flask import Flask, render_template, url_for, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
import datetime

class Temperature:
	def __init__(self, data_val_temp, id_temp):
		self.id_temp = id_temp
		self.data_val_temp = data_val_temp

class CarbonDioxide:
	def __init__(self, data_val_CO2, id_CO2):
		self.id_CO2 = id_CO2
		self.data_val_CO2 = data_val_CO2

class CarbonMonoxide:
	def __init__(self, data_valCO, id_CO):
		self.id_CO = id_CO
		self.data_valCO = data_valCO

class Humidity:
	def __init__(self, data_val_hum, id_hum):
		self.id_hum = id_hum
		self.data_val_hum = data_val_hum	
					
app = Flask(__name__)

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
	return "Got data"

if __name__ == '__main__':
	app.run(debug=True)

