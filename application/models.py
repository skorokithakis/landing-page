from google.appengine.ext import db


class SignupModel(db.Model):
    email = db.EmailProperty()
    timestamp = db.DateTimeProperty(auto_now_add=True)
