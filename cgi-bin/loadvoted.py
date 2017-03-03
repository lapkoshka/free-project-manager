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

projectId = data["id"]
	
print ("Content-type: application/json \r\n\r\n")
cursor.execute('SELECT id, username, vote FROM rating WHERE projectId="%s"' % projectId)
if cursor.rowcount:
	data = {}
	for id, username, vote in cursor:
		currentRecord = {}
		currentRecord["id"] = id
		currentRecord["username"] = username
		currentRecord["vote"] = vote
		data[id] = currentRecord
	print json.dumps(data)
else:
	print json.dumps({"status": "false"})