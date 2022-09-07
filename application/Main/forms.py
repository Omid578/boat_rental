from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,TextAreaField,FileField,IntegerField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import phonenumbers

class BookBoatForm(FlaskForm):
    ReserveDate = DateField('Datum reservieren',
                        validators=[DataRequired()])
                        
    ReturnDate = DateField('Rückflugdatum',
                        validators=[DataRequired()])

    PickupDate = DateField('Abholdatum',
                        validators=[DataRequired()])
    Reason = TextAreaField('Grund',
                        validators=[DataRequired()])
    
    submit = SubmitField('Einreichen')



