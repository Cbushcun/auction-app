from app import app

from flask import Flask, render_template


@app.route('/')
def home():
    return render_template('pages/home.html')