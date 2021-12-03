from flask_wtf import FlaskForm
from sqlalchemy.sql.sqltypes import String
from wtforms import StringField, EmailField, HiddenField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, NumberRange
from wtforms.widgets.core import ColorInput, TextArea

#Forms de USERS
class UserForm(FlaskForm):
    username = StringField('Nombre de usuario',[DataRequired(message=('Campo requerido')),
                                                Length(max=30,message="No se pueden mas de 30 caracteres")])
    email = EmailField('Email del denunciante', validators=[Email(message="Email no valido"),
                                                            DataRequired(message="Campo requerido"), Length(max=30,message="No se pueden mas de 30 caracteres")])
    first_name = StringField('Nombre', validators=[DataRequired(message="Campo requerido"),
                                                   Length(max=30,message="No se pueden mas de 30 caracteres")])
    last_name = StringField('Apellido', validators=[DataRequired(message="Campo requerido"),
                                                    Length(max=30,message="No se pueden mas de 30 caracteres")])
    password = StringField('Contraseña',validators=[DataRequired(message="Campo requerido"),
                                                    Length(max=30,message="No se pueden mas de 30 caracteres")])

class UserUpdateForm(FlaskForm):
    id = HiddenField('id')
    username = StringField('Nombre de usuario',[DataRequired(message=('Campo requerido')),
                                                Length(max=30,message="No se pueden mas de 30 caracteres")])
    email = EmailField('Email del denunciante', validators=[Email(message="Email no valido"),DataRequired(message="Campo requerido"), Length(max=30)])
    first_name = StringField('Nombre', validators=[DataRequired(message="Campo requerido"), 
                                                   Length(max=30,message="No se pueden mas de 30 caracteres")])
    last_name = StringField('Apellido', validators=[DataRequired(message="Campo requerido"),
                                                    Length(max=30,message="No se pueden mas de 30 caracteres")])
    password = StringField('Contraseña',validators=[DataRequired(message="Campo requerido"),
                                                    Length(max=30,message="No se pueden mas de 30 caracteres")])
    estado = SelectField('Estado', choices=[("False",'Desactivar'),("True",'Activar')])


#Forms de ZONAS
class ZonaForm(FlaskForm):
    coordenadas = StringField('coordenadas')
    nombre = StringField('Nombre',[DataRequired("Campo requerido"),Length(max=30,message="No se pueden mas de 30 caracteres")])
    color = StringField(widget=ColorInput())
    estado = SelectField('Estado', choices=[("publicado",'Publicado'),("despublicado",'Despublicado')])

class ZonaUpdateForm(FlaskForm):
    id = HiddenField('id')
    coordenadas = HiddenField('coordenadas')
    zonas = HiddenField('zonas')
    zonascolores = HiddenField('zonas-colores')
    zonasnombre = HiddenField('zonas-nombre')
    nombre = StringField('Nombre',[DataRequired("Campo requerido"), Length(max=30,message="No se pueden mas de 30 caracteres")])
    color = StringField(widget=ColorInput())
    estado = SelectField('Estado', choices=[("publicado",'Publicado'),("despublicado",'Despublicado')])

#Form de DENUNCIAS
class DenunciaForm(FlaskForm):
    lat = StringField('punto_lat')
    lng = StringField('punto_lng')
    titulo = StringField('Titulo',validators=[DataRequired(message="Campo requerido"),Length(max=30,message="No se pueden mas de 30 caracteres")])
    categoria = SelectField('Categoria', choices=[("cañeria_rota",'Cañeria Rota'),
                        ("calle_inundable",'Calle Inundable'),("calle_rota",'Calle Rota'),("otro",'Otro')], validators=[DataRequired(message="Campo requerido")])
    descripcion = StringField('Descripcion',widget=TextArea(), validators=[DataRequired(message="Campo requerido")])
    estado = SelectField('Estado', choices=[("sinConfirmar",'Sin Confirmar'),("curso",'Curso'),
                                            ("resuelta",'Resuelta'),("cerrada",'Cerrada')], validators=[DataRequired(message="Campo requerido")])
    apellidoD = StringField(label='Apellido del denunciante', validators=[DataRequired(message="Campo requerido"),Length(max=30,message="No se pueden mas de 30 caracteres")])
    nombreD = StringField(label='Nombre del denunciate', validators=[DataRequired(message="Campo requerido"),Length(max=30,message="No se pueden mas de 30 caracteres")])
    telefono = IntegerField(label="Telefono", validators=[DataRequired(message="Campo requerido"),NumberRange(min=100000,message="Tiene que tener por lo menos 6 digitos")])
    emailD = EmailField('Email del denunciante', validators=[Email(message="Email no valido"),DataRequired(message="Campo requerido"), Length(max=30)])
    asignadoA = SelectField('Usuario Encargado')
    
class DenunciaEditForm(FlaskForm):
    id = HiddenField('id')
    lat = StringField('punto_lat')
    lng = StringField('punto_lng')
    titulo = StringField('Titulo',validators=[DataRequired(message="Campo requerido"),Length(max=30,message="No se pueden mas de 30 caracteres")])
    categoria = SelectField('Categoria', choices=[("cañeria_rota",'Cañeria Rota'),
                        ("calle_inundable",'Calle Inundable'),("calle_rota",'Calle Rota'),("otro",'Otro')], validators=[DataRequired(message="Campo requerido")])
    descripcion = StringField('Descripcion',widget=TextArea(), validators=[DataRequired(message="Campo requerido")])
    estado = SelectField('Estado', choices=[("sinConfirmar",'Sin Confirmar'),("curso",'Curso'),
                                            ("resuelta",'Resuelta'),("cerrada",'Cerrada')], validators=[DataRequired(message="Campo requerido")])
    apellidoD = StringField(label='Apellido del denunciante', validators=[DataRequired(message="Campo requerido"),Length(max=30,message="No se pueden mas de 30 caracteres")])
    nombreD = StringField(label='Nombre del denunciate', validators=[DataRequired(message="Campo requerido"),Length(max=30,message="No se pueden mas de 30 caracteres")])
    telefono = IntegerField(label="Telefono", validators=[DataRequired(message="Campo requerido"),NumberRange(min=100000,message="Tiene que tener por lo menos 6 digitos")])
    emailD = EmailField('Email del denunciante', validators=[Email(message="Email no valido"),DataRequired(message="Campo requerido"), Length(max=30)])
    asignadoA = SelectField('Usuario Encargado')
    
    
#Form de RECORRIDO
class RecorridoForm(FlaskForm):
    coordenadas = HiddenField('coordenadas')
    nombre = StringField('Nombre de usuario',[DataRequired(message=('Campo requerido')),
                                              Length(max=30,message="No se pueden mas de 30 caracteres")])
    descripcion =  StringField('Descripcion',widget=TextArea(), validators=[DataRequired(message="Campo requerido")])
    estado = SelectField('Estado', choices=[("publicado",'Publicado'),("despublicado",'Despublicado')])
    
class RecorridoEditForm(FlaskForm):
    id = HiddenField('id')
    nombre = StringField('Nombre de usuario',[DataRequired(message=('Campo requerido')),
                                              Length(max=30,message="No se pueden mas de 30 caracteres")])
    descripcion =  StringField('Descripcion',widget=TextArea(), validators=[DataRequired(message="Campo requerido")])
    estado = SelectField('Estado', choices=[("publicado",'Publicado'),("despublicado",'Despublicado')])
    coordenadas = StringField('coordenadas')
    
#Form de Punto
class PuntoForm (FlaskForm):
    email = EmailField('Email del denunciante', validators=[Email(message="Email no valido"),DataRequired(message="Campo requerido"), Length(max=30)])
    nombre = StringField('Nombre de usuario',[DataRequired(message=('Campo requerido')),
                                              Length(max=30,message="No se pueden mas de 30 caracteres")])
    lat = StringField('punto_lat')
    lng = StringField('punto_lng') 
    estado = SelectField('Estado', choices=[("publicado",'Publicado'),("despublicado",'Despublicado')])
    telefono = IntegerField(label="Telefono", validators=[DataRequired(message="Campo requerido"),NumberRange(min=100000,message="Tiene que tener por lo menos 6 digitos")])

class PuntoEditForm(FlaskForm):
    id = HiddenField('id')
    punto_nombre = HiddenField('punto_nombre') #variable del mapa
    email = EmailField('Email del denunciante', validators=[Email(message="Email no valido"),DataRequired(message="Campo requerido"), Length(max=30)])
    nombre = StringField('Nombre de punto',[DataRequired(message=('Campo requerido')),
                                              Length(max=30,message="No se pueden mas de 30 caracteres")])
    lat = StringField('punto-lat')
    lng = StringField('punto-lng')  
    estado = SelectField('Estado', choices=[("publicado",'Publicado'),("despublicado",'Despublicado')])
    telefono = IntegerField(label="Telefono", validators=[DataRequired(message="Campo requerido"),NumberRange(min=100000,message="Tiene que tener por lo menos 6 digitos")])
