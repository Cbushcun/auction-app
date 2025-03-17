from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi
from app import app

import bcrypt

def ping_database():

    uri = app.config['DB_URI']

    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))

    print("Pinging server")

    try:
        client.admin.command('ping')
        print('Ping success')
    except Exception as e:
        print(f'Ping failed: {e}')
        quit()
    client.close()

def connect_to_database():
    uri = app.config['DB_URI']
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    return client[app.config['DB_NAME']]

def hash_password(password: str):
    password_bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed_password.decode('utf-8')

def verify_password(password: str, hashed_password: str):
    password_bytes = password.encode('utf-8')
    hashed_password_bytes = hashed_password.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hashed_password_bytes)