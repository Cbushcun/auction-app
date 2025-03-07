import datetime

from database.util import connect_to_database

async def create_user(username: str,
                      password: str,
                      email: str,
                      role: str,
                      active: bool = True,
                      created_at: datetime = datetime.datetime.now(),
                      updated_at: datetime = datetime.datetime.now()):
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
    
