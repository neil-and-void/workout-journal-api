from re import S
from mongoengine.document import Document
from mongoengine.fields import DateField, FloatField, IntField, ListField, StringField
class Set(Document):
    reps: IntField
    weight: FloatField

class Exercise(Document):
    name: StringField
    sets: ListField(Set)
