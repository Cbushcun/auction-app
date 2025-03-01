from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['DB_URI'] = os.getenv('MONGO_DB_URI')


from app.routes import routes


