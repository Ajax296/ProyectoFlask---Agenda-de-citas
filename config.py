from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "jr.camacho296@gmail.com"
app.config["MAIL_PASSWORD"] = "wqxf biga zzqe hexa"
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USE_TSL"] = False

db = SQLAlchemy(app)
mail = Mail(app)