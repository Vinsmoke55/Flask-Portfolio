from flask import Flask

app=Flask(__name__)

app.config['SECRET_KEY']='3666e0b91fe4e837650c8ce047ee7dca'

from flask_portfolio import routes