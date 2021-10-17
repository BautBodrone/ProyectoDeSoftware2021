from app.models.configuration import Configuration

def settings(session):
    return Configuration.query.first()