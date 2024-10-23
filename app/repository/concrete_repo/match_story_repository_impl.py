from app.database_engine import db_engine_mysql
from app.models import MatchStory
from app.repository.interfaces.base_repository import T
from app.repository.interfaces.match_story_repository import MatchStoryRepository


class MatchStoryRepositoryImpl(MatchStoryRepository):
    def __init__(self):
        self.__session_factory = db_engine_mysql.get_session_factory()

    def find_last_record_story_by_match_id(self, id_match: int) -> MatchStory:
        with self.__session_factory() as session:
            statement = session.query(MatchStory).where(MatchStory.id_match == id_match).order_by(
                MatchStory.id.desc()).first()

        return statement

    def create(self, entity: T) -> T:
        with self.__session_factory() as session:
            session.add(entity)
            session.commit()

        return entity

    def delete(self) -> T:
        pass

    def update(self) -> T:
        pass

    def find_by_id(self, id_entity: int) -> T:
        pass

