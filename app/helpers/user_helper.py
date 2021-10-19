from app.models.user import User

def is_admin(email):
    user = User.search_user_email(email)
    for permiso in user.get_permisos():
        if ('admin' == permiso.nombre):
            return True
    return False

def user(email):
    return User.search_email(email)