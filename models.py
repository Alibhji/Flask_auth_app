# from . import db
#
# class User (db.Model):
#     id = db.Column(db.INTEGER , primary_key=True)
#     email =db.Column(db.String(100),unique=True)
#     password = db.Column(db.String(100))
#     name = db.Column(db.String(100))

from flask_login import UserMixin
from . import db , get_data__from_sql


class UserModel(UserMixin):
    def __init__(self , username, active =True):

        # self.username = username
        # self.password = password
        # self.email = email
        # self.active = active


        # db_cur = db.cursor()
        # get_id = "SELECT uid FROM users WHERE uid=%s"
        # db_cur.execute(get_id, (str(id),))
        # res = db_cur.fetchone()
        # db_cur.close()
        self.username = get_data__from_sql(db, "email", username)
        # self.id = get_data__from_sql(db , "uid" , id)

    def get_id(self):
        return 5
