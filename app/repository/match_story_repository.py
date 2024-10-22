from app.models import MatchStory
from app.repository.sqlalchemy_repository import SqlAlchemyRepository


class MatchStoryRepository(SqlAlchemyRepository):
    __model_name__ = MatchStory

    def get_last_record_story_by_match_id(self, id_match: int) -> MatchStory:
        return (
            self._session.query(MatchStory)
            .where(MatchStory.id_match == id_match)
            .order_by(MatchStory.id.desc()).first()
        )


matches_story_repo = MatchStoryRepository()
