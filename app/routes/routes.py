from app import app
from flask import Flask, render_template
from flask import request, redirect, url_for

@app.route('/')
def home():
    return render_template('/pages/home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('pages/register.html')
    else:
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        email = request.form['email']
        if password != confirm_password:
            return render_template('pages/register.html', error='Passwords do not match')
        else:
            user = app.database.collections.users.get_user_by_username(username)
            if user is not None:
                return render_template('pages/register.html', error='User already exists')
            else:
                app.database.collections.users.create_user(username, password, email, 'user')
                return redirect(url_for('login'))
            
        return redirect(url_for('login'))