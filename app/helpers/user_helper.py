from app.models.user import User
from flask import session

def is_admin(email):
    user = User.search_user_email(email)
    for permiso in user.get_permisos():
        if ('admin' == permiso.nombre):
            return True
    return False

def user(email):
    return User.search_user_email(email)

def has_permit(permit):
    try:
        user = User.search_user_email(session["user"])
        for permit_user in user.get_permisos():
            if (permit_user.nombre == permit):
                return True
        return False
    except:
        return False
