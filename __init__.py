# Flask, authentication, Login and Signup page
# This code is written by Ali Babolhavaeji at 12/8/2020

from flask import Flask
# from flask_sqlalchemy import  SQLAlchemy
import mysql.connector
from flask_login import LoginManager



# db = SQLAlchemy()

def create_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="132",
        database="pythonprog"
    )
    return db

def get_data__from_sql(db , from_column, where_column  , value ):
    db_cur = db.cursor(buffered=True)
    sql = "SELECT %s FROM users WHERE %s=" % (str(from_column).lower() ,str(where_column).lower())
    sql = sql+"%s"
    # sql = "SELECT * FROM users WHERE uid=%s"
    db_cur.execute(sql, (str(value).lower(),))
    # db_cur.execute(sql, ( str(value),))
    res = db_cur.fetchone()
    db_cur.close()
    return None if res is None else res[0]

db =create_db()
from .models import UserModel



def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = 'secret-key-goes-here'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # db.init_app(app)



    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    @login_manager.user_loader
    def load_user(id):
        return UserModel(id)


    # # blueprint for auth routes in our app
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)
    #
    # # blueprint for non-auth parts of app
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    return app


# app = create_app()
#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run(debug=True , host="192.168.1.12")
