# terminal command to test and send data to app
# curl --request POST --url https://go-environment.herokuapp.com/_stuff --data "Temperature=1&Humidity=2&Co=3&Co2=4&Smoke=5&Pressure=6"
# curl --request POST --url localhost:5000/_stuff --data "Temperature=4.5555&Humidity=2&Co=3&Co2=4&Smoke=5&Pressure=6"

from flask import Flask, render_template, url_for, jsonify, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from random import sample
import datetime, json
import sqlite3

class Temperature:
	def __init__(self, data_val_temp):
		self.data_val_temp = data_val_temp

class CarbonDioxide:
	def __init__(self, data_val_CO2):
		self.data_val_CO2 = data_val_CO2

class CarbonMonoxide:
	def __init__(self, data_valCO):
		self.data_valCO = data_valCO

class Humidity:
	def __init__(self, data_val_hum):
		self.data_val_hum = data_val_hum

class Pressure_C:
	def __init__(self, data_val_pres):
		self.data_val_pres = data_val_pres

class Smoke_C:
	def __init__(self, data_val_smo):
		self.data_val_smo = data_val_smo

global temp, humi, co, co2, smoke, pressure, POS, test
POS = 0
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
	global temp, humi, co, co2, smoke, pressure, POS

	if request.method == 'POST':
		conn = sqlite3.connect('data.db') 
		c = conn.cursor()
		temp = request.form['Temperature']
		c.execute("INSERT INTO temperature VALUES (:reading, NULL)", {'reading': float(temp)})
		humi = request.form['Humidity']
		c.execute("INSERT INTO humidity VALUES (:reading, NULL)", {'reading': float(humi)})
		co = request.form['Co']
		c.execute("INSERT INTO carbonMonoxide VALUES (:reading, NULL)", {'reading': float(co)})
		co2 = request.form['Co2']
		c.execute("INSERT INTO carbonDioxide VALUES (:reading, NULL)", {'reading': float(co2)})
		smoke = request.form['Smoke']
		c.execute("INSERT INTO smoke_table VALUES (:reading, NULL)", {'reading': float(smoke)})
		pressure = request.form['Pressure']
		c.execute("INSERT INTO pressure_table VALUES (:reading, NULL)", {'reading': float(pressure)})
		if POS > 10:
			c.execute("DELETE FROM temperature")
			c.execute("DELETE FROM humidity")
			c.execute("DELETE FROM smoke_table")
			c.execute("DELETE FROM carbonDioxide")
			c.execute("DELETE FROM carbonMonoxide")
			c.execute("DELETE FROM pressure_table")
			POS = 0
		POS += 1
		conn.commit()
		conn.close()
		return jsonify(result=temp)
		#return "Posted!"
	elif request.method == 'GET':
		
		return jsonify(result=temp, result1=humi, result2=pressure, result3=co2, result4=co, result5=smoke)  


@app.route('/save-get',methods=['POST', 'GET'])
def saveget():
    if request.method=='GET':
       a=request.args.get('Temperature', '')
       b=request.args.get('Humidity', '')
       return "Temperature : "+a+" ,  Humidity :  "+a
    else:
        return "Not get method"

@app.route('/chart')
def chart():
	return render_template('chart.html')

@app.route('/data')
def data():

	# return jsonify({'results' : sample(range(1,11), 10)})

	conn = sqlite3.connect('data.db') 

	c = conn.cursor()

	#if blah then select data from certain table

	c.execute("SELECT data_val FROM temperature")

	test = c.fetchall() 

	chart_data = []

	for x in range(len(test)):

		testing1 = str(test[x])[1:-4]

		testing = float(testing1)

		chart_data.append(testing)

	conn.close()

	return jsonify(chart_temp=chart_data)

#-----------------------

if __name__ == '__main__':
	app.run(debug=True)
