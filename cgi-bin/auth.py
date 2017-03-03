#!/usr/bin/python
#-*- coding: utf-8 -*-

import json
import os
import cgi,cgitb
import mysql.connector as mariadb
import logging
import datetime

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

with open('../userconfig.json') as data_file:    
    data = json.load(data_file)
mariadb_connection = mariadb.connect(user = data["username"], password = data["password"], database = data["database"], charset='utf8')
cursor = mariadb_connection.cursor(buffered=True)

data = cgi.FieldStorage()
data = json.loads(data.value)
hash = cgi.escape(data["hash"])

cursor.execute('SELECT username FROM userTable WHERE session="%s"' % (hash))
print ("Content-type: application/json \r\n\r\n")

if cursor.rowcount:
 	for username in cursor:
 		currentUsername = username
 	print json.dumps({"status": "true", "username": currentUsername})
else:
 	print json.dumps({"status": "false"})
