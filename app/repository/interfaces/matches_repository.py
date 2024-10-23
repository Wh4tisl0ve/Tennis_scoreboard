from abc import ABC, abstractmethod
from uuid import UUID

from app.models import Matches
from app.repository.interfaces.base_repository import BaseRepository


class MatchesRepository(BaseRepository[Matches], ABC):
    @abstractmethod
    def find_finished_matches(self, name: str, current_page: int, items_per_page: int) -> list[Matches]:
        pass

    @abstractmethod
    def find_count_finished_matches(self, name: str) -> int:
        pass

    @abstractmethod
    def find_by_uuid(self, uuid: UUID) -> Matches:
        pass

    @abstractmethod
    def add_winner_id_by_uuid(self, uuid: str, winner_id: int) -> None:
        pass
