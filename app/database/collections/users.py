from app.database import util
from flask import flash, session

import datetime



async def insert_user(username: str,
                      password: str,
                      email: str,
                      role: str = 'user',
                      active: bool = True,
                      created_at: datetime = datetime.datetime.now(),
                      updated_at: datetime = datetime.datetime.now()):
    hashed_password = util.hash_password(password)
    db = util.connect_to_database()
    collection = db['Users']
    user = {
        'username': username,
        'password': hashed_password,
        'email': email,
        'role': role,
        'active': active,
        'created_at': created_at,
        'updated_at': updated_at,
    }
    await collection.insert_one(user)
    
async def login_user(username: str, password: str):
    user = await get_user_by_username(username)
    if user is None:
        flash('User not found', 'danger')
        return False
    if not util.verify_password(password, user['password']):
        flash('Invalid password', 'danger')
        return False
    session['user_id'] = str(user['_id'])
    session['username'] = user['username']
    session['email'] = user['email']
    session['role'] = user['role']
    return True

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

async def register_user(username: str, password: str, confirm_password: str, email: str):
    if password != confirm_password:
        flash('Passwords do not match', 'danger')
        return False
    
    user = await get_user_by_username(username)
    
    if user is not None:
        flash('User already exists', 'danger')
        return False
    else:
        await insert_user(username, password, email)
        flash('User created successfully', 'success')
        return True 
