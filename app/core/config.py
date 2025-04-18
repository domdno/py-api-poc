import os
from dotenv import load_dotenv

load_dotenv()

# db config
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# logging config
LOG_TABLE = os.getenv("LOG_TABLE")

# endpoints
V1_BRAND_ENROLLMENT_CREATED = "/v1/brand/enrollment/created/"