from . import bcrypt, UserMixin
from webapp import db
import mongoengine as me

class User(UserMixin, me.Document):
    firstname = me.StringField(max_length=40, min_length=2, required=True)
    lastname = me.StringField(max_length=40, min_length=2, required=True)
    email = me.EmailField(max_length=40, min_length=10, required=True)
    username = me.StringField(max_length=40, min_length=6, required=True)
    password = me.StringField(required=True, min_length=8)
    meta = {'alias': 'authusers', 'collection': 'users'}
    
    def __repr__(self):
        return f"Username: {self.username}"
     
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)
        
    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    