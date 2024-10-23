from abc import ABC, abstractmethod

from app.models import Players
from app.repository.interfaces.base_repository import BaseRepository, T


class PlayersRepository(BaseRepository[Players], ABC):
    @abstractmethod
    def find_by_name(self, name: str) -> Players:
        pass
