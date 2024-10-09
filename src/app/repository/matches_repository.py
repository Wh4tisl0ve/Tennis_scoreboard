from uuid import UUID

from app.repository.sqlalchemy_repository import SqlAlchemyRepository
from app.repository.base_repository import T
from app.models import Matches, Players


class MatchesRepository(SqlAlchemyRepository):
    __model_name__ = Matches

    def find_all_by_player_name(self, name: str) -> list[Matches]:
        return self._session.query(Matches, Players).filter(Players.name.contains(name))

    def find_by_uuid(self, uuid: UUID) -> Matches:
        return self._session.query(Matches).filter(Matches.uuid == uuid)

    def delete(self, entity: T) -> T:
        pass

    def update(self, entity: T) -> None:
        pass


matches_repo = MatchesRepository()