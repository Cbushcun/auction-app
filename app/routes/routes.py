import asyncio
from flask import request, redirect, url_for, flash, get_flashed_messages
from flask import render_template
from app import app, database


@app.route('/')
def home():
    return render_template('/pages/home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        get_flashed_messages()
        return render_template('pages/login.html')

    username = request.form['username']
    password = request.form['password']
    user = asyncio.run(database.collections.users.get_user_by_username(username))
    if user is None:
        flash('User not found', 'danger')
        return redirect(url_for('login'))
    if user['password'] != password:
        flash('Invalid password', 'danger')
        return redirect(url_for('login'))
    redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('pages/register.html')

    username = request.form['username']
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    email = request.form['email']
    if password != confirm_password:
        flash('Passwords do not match', 'danger')
        return redirect(url_for('register'))

    user = asyncio.run(database.collections.users.get_user_by_username(username))
    if user is not None:
        flash('User already exists', 'error')
        return redirect(url_for('register'))

    asyncio.run(database.collections.users.create_user(username, password, email))
    flash('User created successfully', 'success')
    return redirect(url_for('login'))
