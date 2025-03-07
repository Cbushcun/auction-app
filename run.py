import asyncio

from app.database.collections import users
from app.database import util
from app import app

if __name__ == '__main__':
    util.ping_database()
    asyncio.run(users.create_user("admin", "admin", "admin@admin.com", "admin"))
    app.run(debug=True, use_reloader=False)