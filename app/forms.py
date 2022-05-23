
from flask_wtf import FlaskForm
from wtforms import DateField, StringField, IntegerField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired

class NewInstrument(FlaskForm):
   date_bought = DateField("Date Bought", validators=[DataRequired()])
   nickname = StringField("Nickname", validators=[DataRequired()])
   year = IntegerField("Year")
   maker = StringField("Maker")
   type = SelectField("Type", choices= ['Other', 'String', 'Wood', 'Brass', 'Percussion'])
   used = BooleanField("Used", validators=[DataRequired()])
   submit = SubmitField("Submit")