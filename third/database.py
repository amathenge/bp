from flask import g
import sqlite3

def connect_db():
    sql = sqlite3.connect('third/third.db')
    sql.row_factory = sqlite3.Row
    return sql

def get_db():
    if not hasattr(g, 'third_db'):
        g.third_db = connect_db()

    return g.third_db

