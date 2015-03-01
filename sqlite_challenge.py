
import sqlite3 as lite
import pandas as pd

# Connect to the database
con = lite.connect('getting_started.db')

# Create the cities and weather tables (HINT: first pass the statement DROP TABLE IF EXISTS <table_name>; to remove the table before you execute the CREATE TABLE ... statement)
with con:
  cur = con.cursor()    
  cur.execute('DROP TABLE IF EXISTS weather')
  cur.execute('DROP TABLE IF EXISTS cities')
  cur.execute('CREATE TABLE weather (city text, year int, warmest text, cold_month text, average_temp int)')
  cur.execute('CREATE TABLE cities (name text, state text)')
  # Insert data into the two tables
  cities = (("New York City", "NY"), ("Boston", "MA"), ("Chicago", "IL"), ("Miami", "FL"), ("Dallas", "TX"), ("Seattle", "WA"), ("Portland", "OR"), ("San Francisco", "CA"), ("Los Angeles", "CA"))
  cur.executemany('INSERT INTO cities VALUES(?,?)', cities)

  weather = (("New York City", 2013, "July", "January", 62), ("Boston", 2013, "July", "January", 59), ("Chicago", 2013, "July", "January", 59), ("Miami", 2013, "August", "January", 84), ("Dallas", 2013, "July", "January", 77), ("Seattle", 2013, "July", "January", 61), ("Portland", 2013, "July", "December", 63), ("San Francisco", 2013, "September", "December", 64), ("Los Angeles", 2013, "September", "December", 75)) 
  cur.executemany('INSERT INTO weather VALUES(?,?,?,?,?)', weather)

  # Join Data Togatehr 
  cur.execute('SELECT * FROM cities INNER JOIN weather ON name = city')

  #Load into a pandas DataFrame
  rows = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(rows, columns=cols)

# Print out the resulting city and state in a full sentence. For example: "The cities that are warmest in July are: Las Vegas, NV, Atlanta, GA..."
JulyCities = []
for row in df.iterrows():
	if row[1][4] == 'July':
		JulyCities.append(row[1][2])

printStr = 'The cities that are warmest in July are: '
for city in JulyCities:
	printStr += city + ', '

print str(printStr[:-2])



