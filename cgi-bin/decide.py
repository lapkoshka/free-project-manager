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

session = cgi.escape( data["session"]) 
projectId = cgi.escape(data["id"]) 
decision = data["decision"]

if decision:
	decision = 1
else:
	decision = 0
	
print ("Content-type: application/json \r\n\r\n")
cursor.execute('SELECT id, login, username, priveleges FROM userTable WHERE session="%s"' % session)
if cursor.rowcount:
	for id, login, username, priveleges in cursor:
		caller = login
		priveleges = priveleges
		judge = username

	if priveleges == 1:
		cursor.execute('UPDATE projects SET solved="%s", judgeLogin="%s", judgeName="%s" WHERE id="%s"' % (decision, caller, judge, projectId))
		mariadb_connection.commit()
		mariadb_connection.close()

		print json.dumps({"status": "true"})
	else:
		print json.dumps({"status": "No access"})
else:
	print json.dumps({"status": "Authenticated failed"})
