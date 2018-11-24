import sqlite3
from index import Temperature, CarbonMonoxide, CarbonDioxide, Humidity

conn = sqlite3.connect('data.db')   #change this to file name to for application

c = conn.cursor()

c.execute("""CREATE TABLE temperature (
			data_val integer,
			id integer
			)""")

c.execute("""CREATE TABLE carbonDioxide (
			data_val integer,
			id integer
			)""")

c.execute("""CREATE TABLE carbonMonoxide (
			data_val integer,
			id integer
			)""")

c.execute("""CREATE TABLE humidity (
			data_val integer,
			id integer
			)""")

temp_write = Temperature(200,1)

#c.execute("INSERT INTO temperature VALUES (:id, :reading)", {'id': temp_write.id_temp, 'reading': temp_write.data_val_temp})

conn.commit()

c.execute("SELECT * FROM temperature WHERE id>0")

print(c.fetchall())

conn.commit()

conn.close()