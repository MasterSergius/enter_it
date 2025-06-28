from fastapi import Depends
from psycopg import AsyncConnection

from app.models.user import UserInfo
from app.models.user import UserDBModel
from app.services.db_connection import get_async_db_connection


class DBService:
    def __init__(self, conn: AsyncConnection):
        self.conn = conn

    async def add_user(
        self,
        username: str,
        password: str,
    ) -> UserDBModel:
        """Adds a new user to the database."""
        sql = "INSERT INTO users (username, password) VALUES (%s, %s);"
        try:
            async with self.conn.cursor() as cur:
                await cur.execute(sql, (username, password))
            await self.conn.commit()
        except Exception as e:
            await self.conn.rollback()
            raise Exception(f"Error adding user: {e}")
        return None

    async def get_users(self) -> list[UserInfo]:
        """Retrieves a user by ID."""
        sql = "SELECT username FROM users"
        async with self.conn.cursor() as cur:
            await cur.execute(sql)
            users = await cur.fetchall()
        if users:
            return [UserInfo(username=user_dict["username"]) for user_dict in users]
        return []


async def get_db_service(
    conn: AsyncConnection = Depends(get_async_db_connection),
) -> DBService:
    return DBService(conn)
