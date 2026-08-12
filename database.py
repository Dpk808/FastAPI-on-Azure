from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

db_url = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:Password1@fastapi-inventory-pg.postgres.database.azure.com:5432/fastapi-pg?sslmode=require"
)

engine = create_engine(db_url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# changes to the requirements.txt 2 3 