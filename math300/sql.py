#!/usr/bin/python
#have to do chmod 700 - owner can read write and execute but nobody else. 

#SQL - Structured Query Language 
#before it was SEQL and structured english query language 
#it's all about database managment system 
# 

# Database - a collection of tables 
# Table - a collection of data organized by rows and columns 
# Columns - named structures that contain certain kinds of data. 
# Records - a row of a table 
# field is one cell of the data. 

#free and good is mySQL 
#nobody really ever talks to databases directly and usually use a GUI or API 

#API - application programming interface. 
#we're going to use an API for python to get at mySQL. 
#k.cooper used to ODBC or some dam thing. 

import MySQLdb as m

#now we have to signup 

#db means database. 
db = m.connect(host='mathlab.math.wsu.edu', user='m300', passwd='4cougs', db='M300')

#now make a "cursor" to hold output from our database queries.. 

crs = db.cursor()

#We can use the cursor to iterate through our results 
#it is customary to put SQL commands in ALL CAPS (or keywords) 
#query = "SELECT * FROM class;"

#query = "INSERT into class (name, color, animal, sport, percent, favdate) values ('johnny', 'red','tiger', 'motogp', '22', '2000-01-01');"

#query = " DELETE FROM class WHERE name='Cooper' AND animal='dog';"

#query = "SELECT * FROM class WHERE animal='cat' AND color='red';"

#can use the percent(%) as a wildcard 
#query = "SELECT * FROM class WHERE animal LIKE 'cat%' AND color='red';"

#can change an entry or field in the list with this. 
#query = "UPDATE class SET animal='lion' WHERE animal='elephant';"


#optimized compiled code in mySQL vs python is interpreted and SLOW!!1 
query = "SELECT c.name,  a.dangerous from class c , animals a WHERE c.color='red' AND a.animal=c.animal order by c.name;" 

#showing off greater than or equal to. 
query = "SELECT * FROM class WHERE favdate >= '2000-01-01';"

crs.execute(query)

#Now go through the results:
records = crs.fetchall() 

for rec in records: 
	print("{0} loves the color {1}".format(rec[0],rec[1])) 
	
#want to minimize the processing that you do in python and stuff. 
 




db.close()






