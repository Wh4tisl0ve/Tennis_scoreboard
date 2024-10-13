from app.models import MatchStory
from app.repository.base_repository import T
from app.repository.sqlalchemy_repository import SqlAlchemyRepository


class MatchStoryRepository(SqlAlchemyRepository):
    __model_name__ = MatchStory

    def get_last_record_story_by_match_id(self, id_match: int) -> MatchStory:
        return (self._session.query(MatchStory)
                .where(MatchStory.id_match == id_match)
                .order_by(MatchStory.id.desc()).first())

    def find_match_story_by_match_id(self, id_match: int) -> list[MatchStory]:
        return self._session.query(MatchStory).where(MatchStory.id_match == id_match).all()

    def delete(self, entity: T) -> T:
        pass

    def update(self, entity: T) -> None:
        pass


matches_story_repo = MatchStoryRepository()
