from flask import Blueprint, render_template, url_for, current_app, g
from .database import get_db

fourth = Blueprint('fourth', __name__, static_folder='static', template_folder='templates')

@fourth.teardown_app_request
def close_db(error):
    if hasattr(g, 'fourth_db'):
        g.fourth_db.close()

@fourth.route("/", methods=['GET', 'POST'])
def home():
    message = 'This home page is from the fourth module'
    return render_template('fourth/home.html', message=message)

# this example opens a db and reads some stuff
@fourth.route('/hello', methods=['GET', 'POST'])
def hello():
    message = 'This message was from the view'
    db = get_db()
    cur = db.cursor()
    sql = 'select id, firstname, surname, email, datejoined, locked from users'
    cur.execute(sql)
    data = cur.fetchall()
    return render_template('fourth/hello.html', message=message, users=data)