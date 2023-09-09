from flask import Blueprint, render_template, url_for 

first = Blueprint('first', __name__, static_folder='static', template_folder='templates')

@first.route("/", methods=['GET', 'POST'])
def home():
    message = 'This home page is from the first module'
    return render_template('first/home.html', message=message)

@first.route('/hello', methods=['GET', 'POST'])
def hello():
    message = 'This message was from the view'
    return render_template('first/hello.html', message=message)