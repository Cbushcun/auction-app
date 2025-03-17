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
    login_success = asyncio.run(users.login_user(username, password))
    if login_success:
        return render_template('pages/home.html')
    return redirect(url_for('login'))
    

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
    
    is_registered = asyncio.run(users.register_user(username, password, confirm_password, email))

    if is_registered:
        return redirect(url_for('login'))
           
    return redirect(url_for('register'))

@app.route('/404', methods=['GET'])
def error_404():
    return render_template('errors/404.html')