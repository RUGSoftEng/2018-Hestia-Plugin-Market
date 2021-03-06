"""
Initialize the database connection.
"""
import os

from sqlalchemy import (create_engine)
from sqlalchemy.orm import (sessionmaker)

DB_BASE_URL = 'localhost:5432'
DB_NAME = 'HestiaDB'
DB_USER = 'postgres'
DB_PASSWORD = 'hestia'
DB_URL = os.environ.get(
    "DATABASE_URL",
    (f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_BASE_URL}/{DB_NAME}')
)

ENGINE = create_engine(DB_URL)
SESSION = sessionmaker(bind=ENGINE)
