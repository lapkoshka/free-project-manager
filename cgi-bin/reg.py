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
password = cgi.escape(data["password"]).replace('"', '\\"')
email = cgi.escape(data["email"]).replace('"', '\\"')

cursor.execute('SELECT * FROM userTable WHERE login="%s" OR username="%s"' % (email, name))
print ("Content-type: application/json \r\n\r\n")

if cursor.rowcount:
	print json.dumps({"status": "false"})
else:
	hash = random.getrandbits(128)
	hash = "%032x" % hash
	cursor.execute('INSERT INTO userTable (username, login, password, session, ip) VALUES ("%s","%s","%s","%s","%s")' % (name, email, password, hash, os.environ["REMOTE_ADDR"]))
	mariadb_connection.commit()
	mariadb_connection.close()
	print json.dumps({"status": "true", "hash": hash})


