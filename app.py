# This is an example program on how to use Flask blueprints
# Blueprints allow you to break a larger program into smaller pieces.
# The smaller modules are easier to manage and can then also be copied from
# App to App (e.g., a module that handles database connections)

from flask import Flask, Blueprint, render_template, url_for, g
from first.first import first
from second.second import second
from third.third import third
from fourth.fourth import fourth
from fifth.fifth import fifth
from sixth.sixth import sixth

app = Flask(__name__)
app.register_blueprint(first, url_prefix="/first")
app.register_blueprint(second, url_prefix="/second")
app.register_blueprint(third, url_prefix="/third")
app.register_blueprint(fourth, url_prefix="/fourth")
app.register_blueprint(fifth, url_prefix="/fifth")
app.register_blueprint(sixth, url_prefix="/sixth")

# import helper templates (e.g., chang  e '\n' to '<br>'...)
from access import *

@app.route('/', methods=['GET', 'POST'])
def app_home():
    message = 'You are on the HOME page. <br>This is a variable passed from the home page'
    return render_template('home.html', message=message)

