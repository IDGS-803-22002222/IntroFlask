from wtforms import Form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Regexp
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField, EmailField
from wtforms import validators

class UserForm(Form):
    matricula=StringField("Matricula", [validators.DataRequired("Este campo es requerido")])
    edad=IntegerField("Edad", [validators.DataRequired("Este campo es requerido")])
    nombre=StringField("Nombre", [validators.DataRequired("Este campo es requerido")])
    apellidos=StringField("Apellidos", [validators.DataRequired("Este campo es requerido")])
    correo=EmailField("Correo", [validators.Email("Este campo es requerido")])