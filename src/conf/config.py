import os
from dotenv import load_dotenv

load_dotenv()

DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")


class Config:
    DB_URL = f"postgresql+asyncpg://{DB_USERNAME}:{DB_PASSWORD}@trumpet.db.elephantsql.com/{DB_NAME}"
    # DB_URL = "postgresql+asyncpg://pjpggqwg:g0oERr5tmQJ1emqQ9jUqddgPeo2CfoHV@trumpet.db.elephantsql.com/pjpggqwg"


config = Config
