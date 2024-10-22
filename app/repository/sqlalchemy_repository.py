from abc import ABC

from app.models import Base
from app.repository.base_repository import BaseRepository, T
from app.database_engine import db_engine_mysql


class SqlAlchemyRepository(BaseRepository, ABC):
    __model_name__: Base = Base

    def __init__(self):
        self._session = db_engine_mysql.get_session()

    def add(self, entity: T) -> T:
        self._session.add(entity)

        self._session.flush()
        self._session.commit()

        return entity

    def find_by_id(self, id_entity: int) -> T:
        return self._session.query(self.__model_name__).filter(self.__model_name__.id == id_entity).one()
