from flask_wtf import FlaskForm
from wtforms import validators, StringField
from wtforms.widgets import TextArea
from wtforms.fields.html5 import EmailField


class ContactForm(FlaskForm):
	firstname = StringField('First name', [validators.Length(min=1, max=99), validators.DataRequired()])
	lastname = StringField('Last name', [validators.Length(min=1, max=25), validators.DataRequired()])
	email = EmailField('Email address', [validators.DataRequired(), validators.Email()])
	phonenumber = StringField('Phone number', [validators.Length(min=9, max=25), validators.DataRequired()])
	organization = StringField('Organization', [validators.Length(max=99)])
	message = StringField('Message', [validators.Length(max=500)], widget=TextArea())
