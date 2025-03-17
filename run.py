import asyncio

from app.database.collections import users
from app.database import util
from app import app


if __name__ == '__main__':
    util.ping_database()
    if not asyncio.run(users.get_user_by_username("admin")):
        asyncio.run(users.insert_user("admin", "admin", "admin@admin.com", "admin"))

    app.run(debug=True, use_reloader=False)
    