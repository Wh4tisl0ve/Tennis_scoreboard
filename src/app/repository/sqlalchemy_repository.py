from abc import ABC

from app.models import Base
from app.repository.base_repository import BaseRepository, T


class SqlAlchemyRepository(BaseRepository, ABC):
    __model_name__ = Base

    def find_by_id(self, id_player: int) -> T:
        return self._session.query(self.__model_name__).filter(self.__model_name__.id == id_player).one()

    def find_all(self) -> list[T]:
        return self._session.query(self.__model_name__).all()
