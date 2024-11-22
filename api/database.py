from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os


DATABASE_URL = os.getenv("DATABASE_URL", "mssql+pyodbc://developer:SecurePassword123@libraryserverproject.database.windows.net:1433/Northwind?driver=ODBC+Driver+17+for+SQL+Server")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
metadata = MetaData()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()