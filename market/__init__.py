from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = 'a1a9db1281afaf34d50225e9'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes
from market import models