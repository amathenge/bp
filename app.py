from flask import Flask, Blueprint, render_template, url_for, g
from first.first import first
from second.second import second
from third.third import third
from fourth.fourth import fourth
from fifth.fifth import fifth

app = Flask(__name__)
app.register_blueprint(first, url_prefix="/first")
app.register_blueprint(second, url_prefix="/second")
app.register_blueprint(third, url_prefix="/third")
app.register_blueprint(fourth, url_prefix="/fourth")
app.register_blueprint(fifth, url_prefix="/fifth")

@app.route('/', methods=['GET', 'POST'])
def home():
    message = 'This is a variable passed from the home page'
    return render_template('home.html', message=message)

