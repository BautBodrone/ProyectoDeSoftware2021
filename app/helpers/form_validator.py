from wtforms import Form,FloatField, validators

class CoordenadaForm(Form):
    latitud = FloatField("Latitud",
                         [validators.DataRequired()])
    longitud = FloatField("Longitud",
                          [validators.DataRequired()])