from flask import  Blueprint
# from . import db


auth = Blueprint("auth" , __name__)

@auth.route('/login')
def login():
    return "LOGIN"

@auth.route('/signup')
def signup():
    return "SignUP"

@auth.route('/logout')
def logout():
    return "LOGOUT"