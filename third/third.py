from flask import Blueprint, render_template, url_for, current_app, g
from .database import get_db

third = Blueprint('third', __name__, static_folder='static', template_folder='templates')

@third.teardown_app_request
def close_db(error):
    if hasattr(g, 'third_db'):
        g.third_db.close()

@third.route("/", methods=['GET', 'POST'])
def home():
    message = 'This home page is from the third module'
    return render_template('third/home.html', message=message)

# this example opens a db and reads some stuff
@third.route('/hello', methods=['GET', 'POST'])
def hello():
    message = 'This message was from the view'
    db = get_db()
    cur = db.cursor()
    sql = 'select id, firstname, surname, email, phone, notes from users'
    cur.execute(sql)
    data = cur.fetchall()
    return render_template('third/hello.html', message=message, users=data)

@third.route('/data', methods=['GET', 'POST'])
def data():
    message = 'This message is from the data module in the <b>THIRD</b> module'
    message += '<br />Youll notice that all the data has a google email'
    db = get_db()
    cur = db.cursor()
    sql = "select id, firstname, surname, email, phone, notes from users where email like '%google%'"
    cur.execute(sql)
    data = cur.fetchall()
    return render_template('third/hello.html', message=message, users=data)