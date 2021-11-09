from app.models.user import User
from flask import session

def is_admin(email):
    user = User.search_user_email(email)
    for rol in user.rols:
        if (rol.nombre == "admin"):
            return True
    return False

def user(email):
    return User.search_email(email)

def has_permit(permit):
    user = User.search_user_email(session["user"])
    for permit_user in user.get_permisos():
        if (permit_user.nombre == permit):
            return True
    return False
