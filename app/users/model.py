from mongoengine import *
import time
from werkzeug.security import generate_password_hash, check_password_hash

connect('users', host='127.0.0.1',port=27017)


class Users(Document):

    email = StringField()
    username = StringField()
    password = StringField()
    login_time = IntField(default=int(time.time()))

    def __str__(self):
        return "Users(id='%s')" % self.id

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    def get(self, id):
        return self.objects(id=id).first()

