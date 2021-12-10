from src.database.schemas.user import User


def create_user(document: User, user, hashed_password):
    new_user = document(email= user.email, name= user.name, password= hashed_password)
    new_user.save()

def get_user(document, query):
    pass

