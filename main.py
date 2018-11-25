from flask import Flask, render_template, url_for, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
import datetime, json

class Temperature:
	def __init__(self, data_val_temp, type_temp, id_temp):
		self.id_temp = id_temp
		self.type_temp = type_temp
		self.data_val_temp = data_val_temp

class CarbonDioxide:
	def __init__(self, data_val_CO2, type_CO2, id_CO2):
		self.id_CO2 = id_CO2
		self.type_CO2 = type_CO2
		self.data_val_CO2 = data_val_CO2

class CarbonMonoxide:
	def __init__(self, data_valCO, type_CO, id_CO):
		self.id_CO = id_CO
		self.type_CO = type_CO
		self.data_valCO = data_valCO

class Humidity:
	def __init__(self, data_val_hum, type_hum, id_hum):
		self.id_hum = id_hum
		self.type_hum = type_hum
		self.data_val_hum = data_val_hum

global temp, humi, co, co2, smoke, pressure
temp = 0
humi = 0
co = 0
co2 = 0
smoke = 0
pressure = 0

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/datasheets')
def datasheets():
	return render_template('datasheets.html', title='Datasheet')

@app.route('/details', methods = ['POST', 'GET'])
def details():

	if request.method == 'POST':
		temp = request.form['Temperature']
		humi = request.form['Humidity']
		return render_template('details.html', title='Details', value=temp)
	elif request.method == 'GET':
		return render_template('details.html', title='Details')

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
		return"humidity high!"

#Test Stuff-----

@app.route('/_stuff', methods = ['POST', 'GET'])
def stuff():
    #return jsonify(result=time.time())
	global temp, humi, co, co2, smoke, pressure

	if request.method == 'POST':
		temp = request.form['Temperature']
		humi = request.form['Humidity']
		co = request.form['Co']
		co2 = request.form['Co2']
		smoke = request.form['Smoke']
		pressure = request.form['Pressure']
		return jsonify(result=temp)
		#return "Posted!"
	elif request.method == 'GET':
		
		return jsonify(result=temp, result1=humi, result2=pressure, result3=co2, result4=smoke, result5=co)  


@app.route('/save-get',methods=['POST', 'GET'])
def saveget():
    if request.method=='GET':
       a=request.args.get('Temperature', '')
       b=request.args.get('Humidity', '')
       return "Temperature : "+a+" ,  Humidity :  "+a
    else:
        return "Not get method"
#-----------------------

if __name__ == '__main__':
	app.run(debug=True)

