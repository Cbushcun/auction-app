import asyncio
from flask import request, redirect, url_for, flash, get_flashed_messages, render_template, jsonify, session
from app import app
from app.database.collections import users

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
    user = asyncio.run(users.get_user_by_username(username))
    if user is None:
        flash('User not found', 'danger')
        return redirect(url_for('login'))
    if user['password'] != password:
        flash('Invalid password', 'danger')
        return redirect(url_for('login'))
    session['user_id'] = str(user['_id'])
    session['username'] = user['username']
    session['email'] = user['email']
    session['role'] = user['role']
    return render_template('pages/home.html')

@app.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return render_template('pages/logout.html')


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

    user = asyncio.run(users.get_user_by_username(username))
    if user is not None:
        flash('User already exists', 'error')
        return redirect(url_for('register'))

    asyncio.run(users.register_user(username, password, email))
    flash('User created successfully', 'success')
    return redirect(url_for('login'))

@app.route('/404', methods=['GET'])
def error_404():
    return render_template('errors/404.html')