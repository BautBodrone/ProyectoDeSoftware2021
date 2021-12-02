from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, HiddenField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Email
from wtforms.widgets.core import ColorInput

class UserForm(FlaskForm):
    username = StringField('Nombre de usuario',[DataRequired(message=('Campo requerido')), Length(max=30)])
    email = EmailField('Email', validators=[DataRequired(), Length(max=30)])
    first_name = StringField('Nombre', validators=[DataRequired(message="Campo requerido"), Length(max=30)])
    last_name = StringField('Apellido', validators=[DataRequired(message="Campo requerido"), Length(max=30)])
    password = StringField('Contraseña',validators=[DataRequired(message="Campo requerido"), Length(max=30)])

class UserUpdateForm(FlaskForm):
    id = HiddenField('id')
    username = StringField('Nombre de usuario',[DataRequired(message=('Campo requerido')), Length(max=30)])
    email = EmailField('Email', validators=[DataRequired(), Length(max=30)])
    first_name = StringField('Nombre', validators=[DataRequired(message="Campo requerido"), Length(max=30)])
    last_name = StringField('Apellido', validators=[DataRequired(message="Campo requerido"), Length(max=30)])
    password = StringField('Contraseña',validators=[DataRequired(message="Campo requerido"), Length(max=30)])
    estado = SelectField('Estado', choices=[("False",'Desactivar'),("True",'Activar')])

class ZonaForm(FlaskForm):
    coordenadas = StringField('coordenadas')
    nombre = StringField('Nombre',[DataRequired()])
    color = StringField(widget=ColorInput())
    estado = SelectField('Estado', choices=[("publicado",'Publicado'),("despublicado",'Despublicado')])
