from flask import  Blueprint, render_template, redirect , url_for , request, flash
from werkzeug.security import generate_password_hash, check_password_hash
# from .models import User
from . import db


auth = Blueprint("auth" , __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('name')
    password = request.form.get('password')


    db_cur = db.cursor()
    username_check = "SELECT * FROM users WHERE username=%s"
    db_cur.execute(username_check, (str(username).lower(),))
    res = db_cur.fetchall()
    # return str(len(res))
    if len(res) == 0:
        sql = "INSERT INTO users (username , psssword, email) VALUES (%s , %s, %s)"
        val = (str(username).lower() , str(password).lower(), str(email).lower() )
        db_cur.execute(sql,val)
        db.commit()
        # return " %s is added. %s" % (username ,res)
        flash("The username is added.")
        return  redirect(url_for('auth.login'))

    else:
        # return " %s is exists. %s" % (username , res)
        flash("The username is already created.")
        return redirect(url_for('auth.signup'))





    # user = User.query.filter_by(
    #     email=email).first()  # if this returns a user, then the email already exists in database
    #
    # if user:  # if a user is found, we want to redirect back to signup page so user can try again
    #     return redirect(url_for('auth.signup'))

    # new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    # db.session.add(new_user)
    # db.session.commit()

    # return user
    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return "LOGOUT"