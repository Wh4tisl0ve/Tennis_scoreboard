from uuid import UUID

from sqlalchemy import select, update

from app.repository.sqlalchemy_repository import SqlAlchemyRepository
from app.repository.base_repository import T
from app.models import Matches, Players


class MatchesRepository(SqlAlchemyRepository):
    __model_name__ = Matches

    def find_all_by_player_name(self, name: str) -> list[Matches]:
        return self._session.query(Matches, Players).filter(Players.name.contains(name))

    def find_by_uuid(self, uuid: UUID) -> Matches:
        return self._session.execute(select(Matches).filter(Matches.uuid == uuid)).one()[0]

    def add_winner_id_by_uuid(self, uuid: str, winner_id: int) -> None:
        self._session.execute(update(Matches).where(Matches.uuid == uuid).values(winner_id=winner_id))
        self._session.execute(update(Matches).where(Matches.uuid == uuid).values(is_end_game=True))
        self._session.commit()

    def delete(self, entity: T) -> T:
        pass

    def update(self, entity: T) -> None:
        pass


matches_repo = MatchesRepository()
