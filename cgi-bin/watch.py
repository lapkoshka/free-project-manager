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

session = cgi.escape(data["session"])
projectId =  cgi.escape(data["id"])

print ("Content-type: application/json \r\n\r\n")
cursor.execute('SELECT id, login FROM userTable where session="%s"' % session)
if cursor.rowcount:
	for id, login in cursor:
		login = login
	cursor.execute('SELECT id, login FROM watch WHERE projectId="%s" AND login="%s"' % (projectId, login))
	if cursor.rowcount:
		print json.dumps({"status":"already watched"})
	else:
		cursor.execute('INSERT INTO watch (login, projectId) VALUES ("%s","%s")' % (login, projectId))
		mariadb_connection.commit()
		mariadb_connection.close()
		print json.dumps({"status":"true"})
else:
	print json.dumps({"status": "false"})