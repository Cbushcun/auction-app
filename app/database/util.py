from app import app
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

def ping_db_server():
    

    uri = app.config['DB_URI']
    
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    
    print("Pinging server")
    
    try:
        client.admin.command('ping')
        print('Ping success')
    except Exception as e:
        print(f'Ping failed: {e}')
        quit()