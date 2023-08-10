from flask_portfolio import db


class Contact(db.Model):
	id=db.Column(db.Integer,primary_key=True,nullable=False)
	username=db.Column(db.String(20),unique=True,nullable=False)
	email=db.Column(db.String(120),unique=True,nullable=False)
	text=db.Column(db.String(200),unique=True,nullable=False)

	def __repr__(self):
		return f"User('{self.username}','{self.email}','{self.text}'),"