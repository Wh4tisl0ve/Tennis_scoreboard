from abc import ABC, abstractmethod
from typing import Generic, TypeVar


from app.models import Base

T = TypeVar("T", bound=Base)


class BaseRepository(Generic[T], ABC):
    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    @abstractmethod
    def delete(self) -> T:
        pass

    @abstractmethod
    def update(self) -> T:
        pass

    @abstractmethod
    def find_by_id(self, id_entity: int) -> T:
        pass
