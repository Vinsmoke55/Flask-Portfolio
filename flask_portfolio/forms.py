from flask_wtf import Form
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length,Email



class ContactForm(Form):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	text=TextAreaField('Text',validators=[DataRequired()])
	submit=SubmitField('Send')
