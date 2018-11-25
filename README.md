# Software Guide

```
how to run app
--------------
1. cd to correct folder in directory

2. activate virtual environment
  
  pc command: venvwin\Scripts\activate
  mac command: . venv/bin/activate

3. run app w/ local web server (2 ways)
  
  1st way:
     
    pc/mac command: python main.py
  
  2nd way: 
    
    pc commands: set FLASK_APP=main.py 
                 set FLASK_ENV=development
                 flask run
                 
    mac commands: export FLASK_APP=main.py
                  export FLASK_DEBUG=1
                  flask run

4. to see website
	
  open your internet browser
  web address: http://localhost:5000/

5. to stop web server

  pc/mac command: ctrl-c

6. to deactivate virtual environment

  pc/mac command: deactivate

```

