import asyncio
from app.database import util
from app import app

if __name__ == '__main__':
    util.ping_db_server()
    asyncio.run(util.insert_new_user())
    app.run(debug=True, use_reloader=False)