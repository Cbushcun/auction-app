from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

from app import app

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
