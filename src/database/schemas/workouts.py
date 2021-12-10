from mongoengine import Document
from mongoengine.fields import DateField, ListField, StringField

class Workout(Document):
    name: StringField
    date: DateField
    exercises: ListField()
