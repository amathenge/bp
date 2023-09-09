from flask import Blueprint, render_template, url_for, current_app, g, request, redirect
from .database import get_db
from werkzeug.security import generate_password_hash, check_password_hash

sixth = Blueprint('sixth', __name__, static_folder='static', template_folder='templates')

@sixth.teardown_app_request
def close_db(error):
    if hasattr(g, 'sixth_db'):
        g.sixth_db.close()

@sixth.route("/", methods=['GET', 'POST'])
def home():
    message = 'This home page is from the sixth module'
    return render_template('sixth/home.html', message=message)

# login form.
@sixth.route('/login', methods=['GET', 'POST'])
def login():
    db = get_db()
    cur = db.cursor()

    if request.method == 'POST':
        # collect field values and update.
        user = {
            'email': request.form['email'].lower(),
            'password': request.form['password']
        }
        sql = 'select id, email, password, firstname, lastname from users where email = ?'
        cur.execute(sql, [user['email']])
        data = cur.fetchone()
        if data is None:
            return render_template('sixth/failure.html')

        pwd_hash = check_password_hash(data['password'], user['password'])
        if not pwd_hash:
            return render_template('sixth/failure.html')
        
        # if we get here, then all is OK.
        user['id'] = data['id']
        user['firstname'] = data['firstname']
        user['lastname'] = data['lastname'] 

        return render_template('sixth/success.html', user=user)


    return render_template('sixth/login.html')
