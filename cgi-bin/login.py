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
login = cgi.escape(data["login"])
password = cgi.escape(data["password"])

cursor.execute('SELECT id, username FROM userTable WHERE login="%s" AND password="%s"' % (login, password))
print ("Content-type: application/json \r\n\r\n")

if cursor.rowcount:
	for id, username in cursor:
		currentId = id

	hash = random.getrandbits(128)
	hash = "%032x" % hash
	cursor.execute('UPDATE userTable SET session="%s", ip="%s" WHERE id="%s"' % (hash, os.environ["REMOTE_ADDR"], currentId))

	print json.dumps({"status": "true", "hash": hash})
else:
	print json.dumps({"status": "false"})

mariadb_connection.commit()
mariadb_connection.close()