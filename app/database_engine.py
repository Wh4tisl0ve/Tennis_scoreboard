from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.config import settings


class DataBaseEngine:
    def __init__(self, url: str):
        self.engine = create_engine(url=url, echo=False)
        self.session_factory = sessionmaker(bind=self.engine,
                                            autocommit=False,
                                            autoflush=False,
                                            expire_on_commit=False)

    def get_session(self) -> Session:
        with self.session_factory() as session:
            return session


db_engine_mysql = DataBaseEngine(url=settings.db.DATABASE_URL_pymysql)
