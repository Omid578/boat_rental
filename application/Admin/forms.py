from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,SelectField,TextAreaField,FileField,IntegerField,DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import phonenumbers

class AddBoatForm(FlaskForm):
    boat_name = StringField('Boat Name',
                        validators=[DataRequired()])
                        
    model = StringField('Model',
                        validators=[DataRequired()])


    seats = StringField('Seats',
                        validators=[DataRequired()])

    year = StringField('Year',
                        validators=[DataRequired()])


    group = StringField('Model Group',
                        validators=[DataRequired()])

    


    price_per_day = StringField('Price Per Day',
                        validators=[DataRequired()])

    

    boat_type = StringField('Boat Type',
                        validators=[DataRequired()])
    



    gear = StringField('Gear',
                        validators=[DataRequired()])


    boat_fuel = StringField('Boat fuel',
                        validators=[DataRequired()])


    performance_ps = StringField('Performance ps',
                        validators=[DataRequired()])



    doors = StringField('Doors',
                        validators=[DataRequired()])



    state = StringField('State',
                        validators=[DataRequired()])

    

    
    


    color = StringField('Color',
                        validators=[DataRequired()])


    submit = SubmitField('Add')



