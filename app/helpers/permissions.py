from app.models.user import User

def permissions(email):
    return User.search_email(email)