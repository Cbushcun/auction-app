import os
from dotenv import load_dotenv
from flask import Flask


os.environ.pop('MONGO_DB_URI', None)
os.environ.pop('MONGO_DB_NAME', None)

load_dotenv()

app = Flask(__name__)

app.config['DB_URI'] = os.getenv('MONGO_DB_URI')
app.config['DB_NAME'] = os.getenv('MONGO_DB_NAME')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['ADMIN_USERNAME'] = os.getenv('ADMIN_USERNAME')
app.config['ADMIN_PASSWORD'] = os.getenv('ADMIN_PASSWORD')
app.config['ADMIN_EMAIL'] = os.getenv('ADMIN_EMAIL')

from app.routes import routes
