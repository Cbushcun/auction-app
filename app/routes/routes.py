from app import app

@app.route('/')
def home():
    return "Welcome to my Flask app!"