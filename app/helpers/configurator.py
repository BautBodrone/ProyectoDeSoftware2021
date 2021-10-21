from app.models.configuration import Configuration

def settings():
    return Configuration.get_config()
