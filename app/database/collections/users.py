import datetime

from app.database import util



async def create_user(username: str,
                      password: str,
                      email: str,
                      role: str = 'user',
                      active: bool = True,
                      created_at: datetime = datetime.datetime.now(),
                      updated_at: datetime = datetime.datetime.now()):
    db = util.connect_to_database()
    collection = db['Users']
    user = {
        'username': username,
        'password': password,
        'email': email,
        'role': role,
        'active': True,
        'created_at': created_at,
        'updated_at': updated_at,
    }
    result = await collection.insert_one(user)
    print(f'Inserted user with id {result.inserted_id}')
    
async def get_user_by_id(user_id: str):
    db = util.connect_to_database()
    collection = db['Users']
    user = await collection.find_one({'_id': user_id})
    return user

async def get_user_by_username(username: str):
    db = util.connect_to_database()
    collection = db['Users']
    user = await collection.find_one({'username': username})
    return user

async def get_all_users():
    db = util.connect_to_database()
    collection = db['Users']
    users = collection.find()
    return users

async def update_user(user_id: str, user_data: dict):
    db = util.connect_to_database()
    collection = db['Users']
    user = collection.find_one({'_id': user_id})
    if user is None:
        print("User not found")
        return None
    else: 
        await collection.update_one({'_id': user_id}, {'$set': user_data})
        
        
async def register_user(username: str, password: str, email: str):
    user = await get_user_by_username(username)
    if user is not None:
        print("ERROR: User already exists")
        return None
    else:
        await create_user(username, password, email)
        print("User created: ", username, password, email)
        return await get_user_by_username(username)