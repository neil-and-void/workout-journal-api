from mongoengine import Document, StringField, IntField, ListField

class WorkoutTemplate(Document):
    name: StringField
    exercises: ListField

class ExerciseTemplate(Document):
    name: StringField
    sets: IntField
    reps: IntField
