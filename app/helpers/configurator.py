from app.models.configuration import Configuration

def settings():
    return Configuration.get_config()

def private_bg_color():
    aux = Configuration.get_config().get_private_bg_color()
    return aux

def private_letters_color():
    aux = Configuration.get_config().get_private_letters_color()
    return aux

def private_accent_color():
    aux = Configuration.get_config().get_private_accent_color()
    return aux

def rows_per_page():
    aux = Configuration.get_config().get_rows_per_page()
    return aux