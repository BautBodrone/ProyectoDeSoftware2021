from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import String
from wtforms import StringField, EmailField, HiddenField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms.widgets.core import ColorInput, TextArea

#Forms de USERS
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


#Forms de ZONAS
class ZonaForm(FlaskForm):
    coordenadas = StringField('coordenadas')
    nombre = StringField('Nombre',[DataRequired()])
    color = StringField(widget=ColorInput())
    estado = SelectField('Estado', choices=[("publicado",'Publicado'),("despublicado",'Despublicado')])

class ZonaUpdateForm(FlaskForm):
    id = HiddenField('id')
    coordenadas = HiddenField('coordenadas')
    zonas = HiddenField('zonas')
    zonascolores = HiddenField('zonas-colores')
    zonasnombre = HiddenField('zonas-nombre')
    nombre = StringField('Nombre',[DataRequired()])
    color = StringField(widget=ColorInput())
    estado = SelectField('Estado', choices=[("publicado",'Publicado'),("despublicado",'Despublicado')])

#Form de DENUNCIAS
class DenunciaForm(FlaskForm):
    one_marker = HiddenField('one-marker')
    lat = StringField('punto_lat')
    lng = StringField('punto_lng')
    titulo = StringField('Titulo',validators=[DataRequired(message="Campo requerido")])
    categoria = SelectField('Categoria', choices=[("cañeria_rota",'Cañeria Rota'),
                        ("calle_inundable",'Calle Inundable'),("calle_rota",'Calle Rota'),("otro",'Otro')], validators=[DataRequired(message="Campo requerido")])
    descripcion = StringField('Descripcion',widget=TextArea(), validators=[DataRequired(message="Campo requerido")])
    estado = SelectField('Estado', choices=[("sinConfirmar",'Sin Confirmar'),("curso",'Curso'),
                                            ("resuelta",'Resuelta'),("cerrada",'Cerrada')], validators=[DataRequired(message="Campo requerido")])
    apellidoD = StringField(label='Apellido del denunciante', validators=[DataRequired(message="Campo requerido")])
    nombreD = StringField(label='Nombre del denunciate', validators=[DataRequired(message="Campo requerido")])
    telefono = IntegerField(label="Telefono", validators=[DataRequired(message="Campo requerido"),NumberRange(min=100000,message="Tiene que tener por lo menos 6 digitos")])
    emailD = EmailField('Email del denunciante', validators=[Email(message="Email no valido"),DataRequired(message="Campo requerido"), Length(max=30)])
    asignadoA = SelectField('Usuario Encargado')