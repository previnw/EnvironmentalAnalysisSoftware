# terminal command to test and send data to app
# curl --request POST --url https://go-environment.herokuapp.com/_stuff --data "Temperature=1&Humidity=2&Co=3&Co2=4&Smoke=5&Pressure=6"
# curl --request POST --url localhost:5000/_stuff --data "Temperature=1&Humidity=2&Co=3&Co2=4&Smoke=5&Pressure=6"

from flask import Flask, render_template, url_for, jsonify, request, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField
from random import sample
import datetime, json

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
	return jsonify({'results' : sample(range(1,10), 5)})

#-----------------------

if __name__ == '__main__':
	app.run(debug=True)
