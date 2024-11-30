from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask_login import LoginManager
import cloudinary

app = Flask(__name__)
app.secret_key = "dsdji34^&&^%534fef##@$@#"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4' % quote('Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

cloudinary.config(cloud_name='dedsaxk7j',
                  api_key='475528271894445',
                  api_secret='8OjLj8udRhzD494zkKSwCO3tZOo')

db = SQLAlchemy(app=app)

login=LoginManager(app=app)
