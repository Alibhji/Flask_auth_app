from flask import  Blueprint, render_template, redirect , url_for , request, flash , session
from werkzeug.security import generate_password_hash, check_password_hash
# from .models import User
from . import db , get_data__from_sql
from .models import UserModel
from flask_login import login_user ,current_user, logout_user
import gc


auth = Blueprint("auth" , __name__)

@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')

    uid = get_data__from_sql(db, "uid", "email", email)


    # remember = False if request.form.get('remember') is None else True
    remember = [True ,False][request.form.get('remember') is None]


    if uid is None:
        flash({'msg':"The Username dosen't exist. Please Register.", 'type':"danger"})
        return redirect(url_for('auth.login'))
    else:
        # flash({'msg': "Successfully Login!", 'type': "success"})
        dbpass = get_data__from_sql(db, "psssword", "uid", uid)

        if str(dbpass )== password:
            login_user(UserModel(uid))
            return redirect(url_for('main.profile'))
        else:
            flash({'msg': "Wrong Username or password", 'type': "danger"})
            return redirect(url_for('auth.login'))



@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    username = request.form.get('name')
    password = request.form.get('password')


    res_umane = get_data__from_sql(db, 'username' ,'username', username)
    res_email = get_data__from_sql(db, 'email', 'email',email)
    # return str(res)
    db_cur = db.cursor()

    if (res_umane is None) and (res_email is None):
        sql = "INSERT INTO users (username , psssword, email) VALUES (%s , %s, %s)"
        val = (str(username).lower() , str(password).lower(), str(email).lower() )
        db_cur.execute(sql,val)
        db.commit()

        flash({'msg':"The username is added.", 'type':"success"})

        db_cur.close()
        return  redirect(url_for('auth.login'))

    else:
        flash({'msg': "The username or email is already exist.", 'type': "danger"})
        db_cur.close()
        return redirect(url_for('auth.signup'))


    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    logout_user()
    session.clear()
    gc.collect()
    return redirect(url_for('main.index'))

