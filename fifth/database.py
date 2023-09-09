from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('fifth/fifth.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'fifth_db'):
        g.fifth_db = connect_db()

    return g.fifth_db
