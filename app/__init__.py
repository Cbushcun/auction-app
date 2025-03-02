from flask import Flask
from dotenv import load_dotenv
import os

os.environ.pop('MONGO_DB_URI', None)
os.environ.pop('MONGO_DB_NAME', None)

load_dotenv()

app = Flask(__name__)

app.config['DB_URI'] = os.getenv('MONGO_DB_URI')
app.config['DB_NAME'] = os.getenv('MONGO_DB_NAME')

from app.routes import routes


