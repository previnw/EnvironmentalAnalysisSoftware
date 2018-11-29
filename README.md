### user setup & guide
[github repository](https://github.com/previnw/EnvironmentalAnalysisSoftware) 
`(https://github.com/previnw/EnvironmentalAnalysisSoftware)`<br />
[website](https://go-environment.herokuapp.com/)
`(https://go-environment.herokuapp.com/) `

#### software information
```
code structure
--------------
front-end: 

  python3.7
  flask microframework
  skeleton boilerplate
  html & css
  javascript
  jQuery

back-end:

  sqlite3
  python
  json

setup/build instructions
------------------------
1. clone repo & cd to the correct directory

  pc/mac command to clone: git clone https://github.com/previnw/EnvironmentalAnalysisSoftware.git

2. setup python

  install python3 or higher (python3.7 recommended) using: https://www.python.org/downloads/
  
  pc command to ensure python3 or higher is running: python
  mac command to ensure python3 or higher is running: python -V

  *** if pip doesn't work follow this guide: https://pip.pypa.io/en/stable/installing/

3. activate virtual environment
  
  pc command: venvwin\Scripts\activate
  mac command: . venv/bin/activate

  *** if there are virtual environment issues follow this guide: http://flask.pocoo.org/docs/1.0/installation/#virtual-environments

4. install flask

  follow this installation guide: http://flask.pocoo.org/docs/1.0/installation/#install-flask

5. install additional libraries

  pc/mac commands: pip install Flask-WTF
                   pip install WTForms

6. run app w/ local web server (2 ways)
  
  1st way:
     
    pc/mac command: python main.py
  
  2nd way: 
    
    pc commands: set FLASK_APP=main.py 
                 set FLASK_ENV=development
                 flask run
                 
    mac commands: export FLASK_APP=main.py
                  export FLASK_DEBUG=1
                  flask run

7. to see website
	
  open your internet browser
  web address: http://localhost:5000/

8. to stop web server

  pc/mac command: ctrl-c

9. to deactivate virtual environment

  pc/mac command: deactivate
```
#### hardware information
```

code structure
--------------
C++
Arduino Libraries


hardware
--------
arduino mega 2560
esp8266 nodemcu wifi module
6 different sensors


setup/build instructions
------------------------
1. hardware

  hook up the sensor as is shown in the diagram in the report and use the that is stored within the github.

2. nodemcu wifi module

  the wifi module is setup to connect to the webapp already and just needs to be connected as is shown in the diagram

3. arduino

  if you want to push new code to the arduino, the sensor libraries must be added to your ide through the manage libraries tool.  simply search the sensor names and press the install button
  <Adafruit_BMP085.h>
  <SoftwareSerial.h>
  <Adafruit_Sensor.h>
```


