from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from typing import Generator


class DataBaseEngine:
    def __init__(self, url: str):
        self.engine = create_engine(url=url, echo=True)
        self.session_factory = sessionmaker(bind=self.engine, autocommit=False, autoflush=False)

    def dispose(self) -> None:
        self.engine.dispose()

    def get_session(self) -> Generator[Session, None, None]:
        with self.session_factory() as session:
            yield session


db_engine_mysql = DataBaseEngine(url=settings.db.DATABASE_URL_pymysql)
