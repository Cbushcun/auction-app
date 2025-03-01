from app import app
from app.database import util

if __name__ == '__main__':
    util.ping_db_server()
    app.run(debug=True)