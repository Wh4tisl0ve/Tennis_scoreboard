from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from app.database_engine import db_engine_mysql
from app.models import Base

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T], ABC):
    def __init__(self):
        self._session = db_engine_mysql.get_session()

    @abstractmethod
    def add(self, entity: T) -> T:
        pass

    @abstractmethod
    def find_by_id(self, id_entity: int) -> T:
        pass

    @abstractmethod
    def find_all(self) -> list[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, entity: T) -> T:
        pass
