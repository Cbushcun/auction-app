import datetime
from app import app
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo.server_api import ServerApi

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

async def insert_new_user(username, password, email, role, active = True, created_at = datetime.datetime.now(), updated_at = datetime.datetime.now()):
    db = connect_to_database()
    users_collection = db['Users']
    user = {
        'username': username,
        'password': password,
        'email': email,
        'role': role,
        'active': True,
        'created_at': created_at,
        'updated_at': updated_at,
    }
    result = await users_collection.insert_one(user)
    print(f'Inserted user with id {result.inserted_id}')