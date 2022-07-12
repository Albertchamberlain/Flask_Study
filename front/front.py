from flask import Flask ,Blueprint

front = Blueprint('front',__name__)

@front.route('/index')
def index():
    return 'index page'

@front.route('/add')
def add():
    return 'add page'

@front.route('/delete')
def delete():
    return 'delete page'
