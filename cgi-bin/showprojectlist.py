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
innerCursor = mariadb_connection.cursor(buffered=True)

def getLoginBySession(session):
	cursor.execute('SELECT id, login FROM userTable WHERE session="%s"' % session)
	if cursor.rowcount:
		for id, login in cursor:
			return login

def getPrivelegesBySession(session):
	cursor.execute('SELECT id, priveleges FROM userTable WHERE session="%s"' % session)
	if cursor.rowcount:
		for id, priveleges in cursor:
			return priveleges or "User"

def getProjects ():
	cursor.execute('SELECT id, name, description, author, solved, createTime FROM projects ORDER BY id DESC')
	projects = {}
	k = 0
	for id, name, description, author, solved, createTime in cursor:
		currentRecord = {}
		currentRecord['id'] = id
		currentRecord['name'] = name
		currentRecord['description'] = description
		currentRecord['author'] = author
		currentRecord['solved'] = solved
		currentRecord['createTime'] = createTime.strftime("%d.%m.%Y")
		currentRecord['rating'] = getRating(id)
		currentRecord['answers'] = getCommentsCount(id)
		currentRecord['views'] = getViews(id)
		#currentRecord['createTime'] = createTime.strftime("%Y-%m-%d %H:%M:%S")
		projects[k] = currentRecord
		k += 1
	return projects

def getRating(projectId):
	innerCursor.execute('SELECT id, vote FROM rating WHERE projectId="%s"' % projectId)
	rating = 0
	if innerCursor.rowcount:
		for id, vote in innerCursor:
			rating += vote
	
	return rating

def getCommentsCount (projectId):
	innerCursor.execute('SELECT id, author FROM comments WHERE projectId="%s"' % projectId)
	return innerCursor.rowcount

def getViews(projectId):
	innerCursor.execute('SELECT id, login FROM watch WHERE projectId="%s"' % projectId)
	return innerCursor.rowcount or 0

def getPostContent (id, caller, priveleges):
	cursor.execute('SELECT id, vote FROM rating WHERE projectId="%s"' % id)
	rating = 0
	if cursor.rowcount:
		for idR, vote in cursor:
			rating += vote
		
	cursor.execute('SELECT name, description, author, judgeName FROM projects WHERE id="%s"' % id)
	content = {}
	for name, description, author, judgeName in cursor:
		content["name"] = name
		content["description"] = description
		content["author"] = author
		content['rating'] = rating
		content['judgeName'] = judgeName
		content['priveleges'] = priveleges
	
	cursor.execute('SELECT id, author, login, comment, createTime FROM comments WHERE projectId="%s"' % id)
	comments = {}
	for id, author, login, comment, createTime in cursor:
		currentRecord = {}
		currentRecord['id'] = id
		currentRecord['author'] = author
		if login == caller: 
			currentRecord['owner'] = True
		currentRecord['comment'] = comment
		currentRecord['createTime'] = createTime.strftime("%d.%m.%Y")
		comments[id] = currentRecord
		
	
	content["comments"] = comments
	return content

if os.environ["REQUEST_METHOD"] == "GET":  
	print ("Content-type: application/json \r\n\r\n")
	print json.dumps(getProjects())
if os.environ["REQUEST_METHOD"] == "POST":  
 	print ("Content-type: application/json \r\n\r\n")
	data = cgi.FieldStorage()
	data = json.loads(data.value)
	id = data["id"]
	session = data["session"]
	caller = getLoginBySession(session)
	priveleges = getPrivelegesBySession(session)
	print json.dumps(getPostContent(id, caller, priveleges))
