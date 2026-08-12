from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine 

# db_url = "postgresql://deepakyadav:12345@localhost:5432/deepak"
db_url = "postgresql://postgres:password@db:5432/fastapi"

engine = create_engine(db_url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)