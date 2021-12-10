from mongoengine import Document, StringField

class User(Document):
    email = StringField(required=True, max_length=64)
    name = StringField(required=True, max_length=64)
    password = StringField(required=True, max_length=64)
