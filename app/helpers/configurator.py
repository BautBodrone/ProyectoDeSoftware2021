from app.models.configuration import Configuration

def settings():
    return Configuration.get_config()

def private_bg_color():
    return Configuration.get_private_bg_color()
    