import asyncio
import os

from app.database.collections import users
from app.database import util
from app import app


if __name__ == '__main__':
    util.ping_database()
    if not asyncio.run(users.get_user_by_username("admin")):
        asyncio.run(users.insert_user(os.getenv('ADMIN_USERNAME'), os.getenv('ADMIN_PASSWORD'), os.getenv('ADMIN_EMAIL'), "admin"))

    app.run(debug=True, use_reloader=False)
    