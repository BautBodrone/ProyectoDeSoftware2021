from app.models.user import User

def permissions(email):
    print("-----------------")
    print(email)
    print(User.search_email(email))
    print("-----------------")
    return User.search_email(email)