from app.models.user import User

def is_admin(email):
    user = User.search_user_email(email)
    for rol in user.rols:
        if (rol.nombre == "admin"):
            return True
    return False

def user(email):
    return User.search_email(email)