from config import settings
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine(url=settings.DATABASE_URL_pymysql)

Session = sessionmaker(bind=engine)
