from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('fourth/fourth.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'fourth_db'):
        g.fourth_db = connect_db()

    return g.fourth_db

