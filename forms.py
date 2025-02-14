from wtforms import form
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email, EqualTo, Length, NumberRange, Regexp
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, DecimalField, EmailField


class UserForm(Form):
    matricula=StringField("Matricula")
    edad=IntegerField("Edad")
    nombre=StringField("Nombre")
    apellidos=StringField("Apellidos")
    correo=EmailField("Correo")