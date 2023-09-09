from flask import Blueprint, render_template, url_for 

second = Blueprint('second', __name__, static_folder='static', template_folder='templates')

@second.route("/", methods=['GET', 'POST'])
def home():
    message = 'This home page is from the second module'
    return render_template('second/home.html', message=message)

@second.route('/hello', methods=['GET', 'POST'])
def hello():
    message = 'This message was from the view'
    return render_template('second/hello.html', message=message)