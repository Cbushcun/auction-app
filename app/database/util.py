import datetime
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
    client.close()
    
def establish_db_connection():
    uri = app.config['DB_URI']
    client = AsyncIOMotorClient(uri, server_api=ServerApi('1'))
    return client[app.config['DB_NAME']]

async def insert_new_user():
    db = establish_db_connection()
    users_collection = db['Users']
    user = {
        'username': 'test',
        'password': 'test',
        'email': 'test@testing.com',
        'role': 'admin',
        'active': True,
        'created_at': datetime.datetime.now(),
        'updated_at': datetime.datetime.now(),
    }
    result = await users_collection.insert_one(user)
    print(f'Inserted user with id {result.inserted_id}')