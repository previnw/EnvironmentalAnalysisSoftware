### software guide
[github repository](https://github.com/previnw/EnvironmentalAnalysisSoftware) 
`(https://github.com/previnw/EnvironmentalAnalysisSoftware)`<br />
[website](https://go-environment.herokuapp.com/)
`(https://go-environment.herokuapp.com/) `
```
code structure
--------------
front-end: 
  python
  flask microframework
  skeleton boilerplate
  html & css
  javascript

back-end:
  sqlite3
  python
  json

setup/build instructions
------------------------
1. clone repo & cd to the correct directory

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

5. run app w/ local web server (2 ways)
  
  1st way:
     
    pc/mac command: python main.py
  
  2nd way: 
    
    pc commands: set FLASK_APP=main.py 
                 set FLASK_ENV=development
                 flask run
                 
    mac commands: export FLASK_APP=main.py
                  export FLASK_DEBUG=1
                  flask run

6. to see website
	
  open your internet browser
  web address: http://localhost:5000/

7. to stop web server

  pc/mac command: ctrl-c

8. to deactivate virtual environment

  pc/mac command: deactivate

```

