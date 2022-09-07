from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,TextAreaField,FileField,IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import phonenumbers

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Passwort',validators=[DataRequired(),Length(min=5,max=30)])
    
    submit = SubmitField('Anmeldung')


class RegisterationForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    firstname = StringField('Vorname',validators=[DataRequired(),Length(min=5,max=30)])
    lastname = StringField('Nachname',validators=[DataRequired(),Length(min=5,max=30)])
   
    password = PasswordField('Passwort',validators=[DataRequired(),Length(min=5,max=30)])
    gender_choices = ([('Männlich','Männlich'),('Weiblich','Weiblich')])

    gender = SelectField('Geschlecht',
                        choices=gender_choices)
    age = StringField('Das Alter',validators=[DataRequired()])


    street = StringField('Straße',validators=[DataRequired()])
    state = StringField('Zustand',validators=[DataRequired()])
    plz = StringField('bitte',validators=[DataRequired()])

    submit = SubmitField('Registrieren')

    