#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
import os
import cgi,cgitb
import mysql.connector as mariadb
import logging
import datetime
import random

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

with open('../userconfig.json') as data_file:    
    data = json.load(data_file)
mariadb_connection = mariadb.connect(user = data["username"], password = data["password"], database = data["database"], charset='utf8')
cursor = mariadb_connection.cursor(buffered=True)

data = cgi.FieldStorage()
data = json.loads(data.value)

def update():
	cursor.execute('SELECT id, vote FROM rating WHERE projectId="%s"' % projectId)
	rating = 0
	for id, vote in cursor:
		rating += vote
	
	return rating

session = cgi.escape(data["session"])
projectId =  cgi.escape(data["projectId"])
value = data["value"]

print ("Content-type: application/json \r\n\r\n")
#Ask validation of user
cursor.execute('SELECT id, login, username FROM userTable where session="%s"' % session)
#If true remember login and username
if cursor.rowcount:
	for id, login, username in cursor:
		login = login
		username = username
	#Find votes in project
	cursor.execute('SELECT id, vote FROM rating WHERE projectId="%s" and login="%s"' % (projectId, login))
	#If yes, check status of vote
	if cursor.rowcount:
			for id, vote in cursor:
				vote = vote
			#If different, then update	
			if (vote + value) == 0:
				cursor.execute('DELETE FROM rating WHERE projectId="%s" and login="%s"' % (projectId, login))
				mariadb_connection.commit()
				print json.dumps({"status": "true", "rating" : update()})
			else:
				print json.dumps({"status": "false"})
	#If not found vote, then add it to database
	else:
		cursor.execute('INSERT INTO rating (login, username, projectId, vote) VALUES ("%s","%s","%s","%s")' % (login, username, projectId, value))
		mariadb_connection.commit()
		#Ask fresh data by project
		print json.dumps({"status": "true", "rating" : update()})
else:
	print json.dumps({"status": "false"})

mariadb_connection.close()