import asyncio
from flask import request, redirect, url_for
from flask import render_template
from app import app, database


@app.route('/')
def home():
    return render_template('/pages/home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('pages/login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('pages/register.html')

    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email = request.form['email']
    if password != confirm_password:
        print("ERROR: Passwords do not match")
        return render_template('pages/register.html', error='Passwords do not match')

    user = asyncio.run(database.collections.users.get_user_by_username(username))
    if user is not None:
        print("ERROR: User already exists")
        return render_template('pages/register.html', error='User already exists')

    asyncio.run(database.collections.users.create_user(username, password, email))
    return redirect(url_for('login'))
