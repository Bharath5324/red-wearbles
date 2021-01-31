from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField
class LoginForm(FlaskForm):
    email = EmailField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    rememberme = BooleanField('Remember Me')
    submit = SubmitField('SignIn')

class InstituteSignupForm(FlaskForm):
    name = StringField('Institution Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField("Email I.D", validators=[DataRequired()])
    kind = StringField('Institution Type', validators=[DataRequired()])
    scanner_id = StringField('Scanner I.D', validators=[DataRequired()])
    submit = SubmitField('Create Account')

class UserSignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    email = EmailField("Email I.D", validators=[DataRequired()])
    contact1 = IntegerField("Contact 1", validators=[DataRequired()])
    contact2 = IntegerField("Contact 2", validators=[DataRequired()])
    contact3 = IntegerField("Contact 3", validators=[DataRequired()])
    contact4 = IntegerField("Contact 4", validators=[DataRequired()])
    url = StringField('Medical History URL', validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    group = StringField('Blood Group', validators=[DataRequired()])
    tagid = StringField('RFID Ring ID', validators=[DataRequired()])
    submit = SubmitField('Create Account')