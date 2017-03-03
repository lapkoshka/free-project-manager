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

commentId = data["id"]
text = cgi.escape(data["text"])
session = cgi.escape(data["session"])

print ("Content-type: application/json \r\n\r\n")
#Remember who called UPDATE as caller
cursor.execute('SELECT id, login from userTable WHERE session="%s"' % session)
if cursor.rowcount:
	for id, login in cursor:
		caller = login
	#Find comment, if yes, remember login who created
	cursor.execute('SELECT id, login FROM comments WHERE id="%s"' % commentId)
	if cursor.rowcount:
		for id, login in cursor:
			login = login
		#UPDATE
		if caller == login:
			cursor.execute('UPDATE comments SET comment="%s" WHERE id="%s"' % (text, commentId))
			mariadb_connection.commit()
			mariadb_connection.close()
			
			print json.dumps({"status":"true", "text": text})

		else:
			print json.dumps({"status":"Authenticated failed"})
		
	else:
		json.dumps({"status":"Not found comment"})
	
else:
	print json.dumps({"status":"Authenticated failed"})