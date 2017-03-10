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

text = cgi.escape(data["text"]).replace('"', '\\"')
text = text.replace('\n', "<br>")
session = cgi.escape( data["session"]) 
projectId = cgi.escape(data["projectId"]) 

print ("Content-type: application/json \r\n\r\n")
cursor.execute('SELECT id, username, login FROM userTable where session="%s"' % session)
if cursor.rowcount:
	for id, username, login in cursor:
		author = username
		login = login
	cursor.execute('INSERT INTO comments (projectId, author, login, comment, ip) VALUES ("%s","%s","%s","%s","%s")' % (projectId, author, login, text, os.environ["REMOTE_ADDR"]))
	print json.dumps({"status": "true"})
else:
	print json.dumps({"status": "false"})

mariadb_connection.commit()
mariadb_connection.close()