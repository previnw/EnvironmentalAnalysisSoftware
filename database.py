import sqlite3
from flask import request
from main import Temperature, CarbonMonoxide, CarbonDioxide, Humidity, Pressure_C, Smoke_C

conn = sqlite3.connect('data.db')   #change this to :memory: for testing
									#change to data.db for application, will add file into directory
c = conn.cursor()
 
# c.execute("""CREATE TABLE temperature (
# 			data_val real,
# 			id integer primary key
# 			)""")

# c.execute("""CREATE TABLE carbonDioxide (
# 			data_val real,
# 			id integer primary key
# 			)""")

# c.execute("""CREATE TABLE carbonMonoxide (
# 			data_val real,
# 			id integer primary key
# 			)""")

# c.execute("""CREATE TABLE humidity (
# 			data_val real,
# 			id integer primary key
# 			)""")

# c.execute("""CREATE TABLE smoke_table (
# 			data_val real,
# 			id integer primary key
# 			)""")

# c.execute("""CREATE TABLE pressure_table (
# 			data_val real,
# 			id integer primary key
# 			)""")

# #temp_write = Temperature(float(request.form['Temperature']))

# temp_write = Temperature(float(temp))

# c.execute("INSERT INTO temperature VALUES (:reading, NULL)", {'reading': temp})

# conn.commit()

# c.execute("SELECT data_val FROM temperature")

# test = c.fetchall()

# for test in test:
# 	print(test)
	
c.execute("DELETE FROM temperature")
c.execute("DELETE FROM humidity")
c.execute("DELETE FROM smoke_table")
c.execute("DELETE FROM carbonDioxide")
c.execute("DELETE FROM carbonMonoxide")
c.execute("DELETE FROM pressure_table")

conn.commit()

conn.close()