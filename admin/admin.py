from flask import Flask ,Blueprint

admin = Blueprint('admin',__name__)

@admin.route('/login')
def login():
    return 'login page'

@admin.route('/register')
def register():
    return 'register page'