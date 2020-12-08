# Flask, authentication, Login and Signup page
# This code is written by Ali Babolhavaeji at 12/8/2020

from flask import Flask
from flask_sqlalchemy import  SQLAlchemy



db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # app.config["SECRET_KEY"] = 'secret-key-goes-here'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    # db.init_app(app)

    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(main_blueprint)
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
