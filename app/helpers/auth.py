def authenticated(session):
    return session.get("user")

def havePermits(session):
    return session.get("rol")

