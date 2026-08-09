from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine 

db_url = "postgresql://deepakyadav:12345@localhost:5432/deepak"

engine = create_engine(db_url)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)