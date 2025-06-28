import psycopg
from psycopg.rows import dict_row
from psycopg import AsyncConnection

from app.config import settings


async def get_async_db_connection() -> AsyncConnection:
    conn = None
    try:
        conn = await psycopg.AsyncConnection.connect(
            host=settings.db.POSTGRES_HOST,
            dbname=settings.db.POSTGRES_DB,
            user=settings.db.POSTGRES_USER,
            password=settings.db.POSTGRES_PASSWORD,
            port=settings.db.POSTGRES_PORT,
            row_factory=dict_row,
        )
        yield conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise ConnectionError(f"Could not connect to database: {e}")
    finally:
        if conn:
            await conn.close()
            print("Database connection closed.")
