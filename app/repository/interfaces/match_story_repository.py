from abc import ABC, abstractmethod

from app.models import MatchStory
from app.repository.interfaces.base_repository import BaseRepository


class MatchStoryRepository(BaseRepository[MatchStory], ABC):
    @abstractmethod
    def find_last_record_story_by_match_id(self, id_match: int) -> MatchStory:
        pass
