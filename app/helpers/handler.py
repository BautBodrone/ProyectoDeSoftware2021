from flask import render_template

def bad_request(e):
    kwargs = {
        "error_name": "400 Bad Request Error",
        "error_description": "La request está mal formulada",
    }
    return render_template("error.html", **kwargs), 400


def not_found_error(e):
    kwargs = {
        "error_name": "404 Not Found Error",
        "error_description": "La url a la que quiere acceder no existe",
    }
    return render_template("error.html", **kwargs), 404


def unauthorized_error(e):
    kwargs = {
        "error_name": "401 Unauthorized Error",
        "error_description": "No está autorizado para acceder a la url",
    }
    return render_template("error.html", **kwargs), 401

def server_error(e):
    kwargs = {
        "error_name": "500 Server Error",
        "error_description": "Ups, hubo un error de parte del servidor",
    }
    return render_template("error.html", **kwargs), 500

def range_not_satisfiable(e):
    kwargs = {
        "error_name": "416 Range Not Satisfiable",
        "error_description": "Pedido fuera del rango disponible",
    }
    return render_template("error.html", **kwargs), 416