from flask_wtf import FlaskForm
from wtforms import validators, StringField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
	firstname = StringField('First name', [])
	lastname = StringField('Last name', [])
	email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
	phonenumber = StringField('Phone number', [])
	organization = StringField('Organization', [])
	message = StringField('Message', [validators.Length(max=500)], widget=TextArea())
