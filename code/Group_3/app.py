'''
A simple JSON-based database that can be used with Flask.
Usage:
'''
from flask import Flask, render_template
from jsondb import JsonDB
db = JsonDB('db.json')
db.load()
x = db.get('todos', 0)
x.append(x[0])
db.set('todos', x)
db.save()