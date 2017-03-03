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

name = cgi.escape(data["name"]).replace('"', '\\"')
description = cgi.escape(data["description"]).replace('"', '\\"')
session = cgi.escape(data["session"])

print ("Content-type: application/json \r\n\r\n")
cursor.execute('SELECT id, username FROM userTable where session="%s"' % session)
if cursor.rowcount:
	author = ""
	for id, username in cursor:
		author = username

	cursor.execute('SELECT * FROM projects WHERE name="%s"' % name)
	if cursor.rowcount:
		print json.dumps({"status": "Name already exist"})
	else:
		cursor.execute('INSERT INTO projects (name, description, author, ip) VALUES ("%s","%s","%s","%s")' % (name, description, author, os.environ["REMOTE_ADDR"]))
		mariadb_connection.commit()
		mariadb_connection.close()

		print json.dumps({"status": "true"})
else:
	print json.dumps({"status": "User does not authenticated"})