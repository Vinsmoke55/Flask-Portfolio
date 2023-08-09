from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length,Email



class ContactForm(FlaskForm):
	username=StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
	email=StringField('Email',validators=[DataRequired(),Email()])
	text=TextAreaField('Text',validators=[DataRequired()])
	submit=SubmitField('Send')
