from flask import redirect, render_template, request, url_for, abort, session, flash, Flask
import flask_sqlalchemy
from app.models.user import User
from oauthlib.oauth2 import WebApplicationClient
from config import config


import requests
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)

import json  
GOOGLE_CLIENT_ID ="416190660321-8mnvf3fsinumi9lj45f2ruvmge9q3jkn.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET = "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"
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

def get_google_provider_cfg():
    return requests.get(GOOGLE_DISCOVERY_URL).json()
client = WebApplicationClient(GOOGLE_CLIENT_ID)

def loginG():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]
    

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri= config["production"].dir,
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

# @app.route("/login/callback")
def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")

    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens!
    client.parse_request_body_response(json.dumps(token_response.json()))
    
    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)
    if userinfo_response.json().get("email_verified"):
        name = userinfo_response.json()["name"]
        users_email = userinfo_response.json()["email"]
        users_name = userinfo_response.json()["given_name"]
        family_name=userinfo_response.json()["family_name"]
    else:
        return "User email not available or not verified by Google.", 400
        
    # Create a user in your db with the information provided
    # by Google

    # Doesn't exist? Add it to the database.
  
    if not User.query.filter_by(email=users_email).first():
        user = User(
        first_name=users_name,last_name=family_name,password="",username=users_email, email=users_email,activo = False)
        User.save(user)
        

    # Begin user session by logging the user in
    # login_user(user)

    # Send user back to homepage

    aux = User.query.filter_by(email=users_email).first()
    if not aux.is_activo():
        flash("Usuario bloqueado, Debe esperar a aceptacion del administrador.")
        return redirect(url_for("auth_login"))

    session["user"] = aux.email
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))


def login():
    return render_template("auth/login.html")


def authenticate():
    
    params = request.form

    user = User.authenticate_user(params)

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))

    if not user.is_activo():
        flash("Usuario bloqueado.")
        return redirect(url_for("auth_login"))

    session["user"] = user.email
    flash("La sesión se inició correctamente.")

    return redirect(url_for("home"))


def logout():
    del session["user"]
    session.clear()
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("home"))
