from uuid import UUID

from sqlalchemy import select, update, or_
from sqlalchemy.orm import aliased

from app.repository.sqlalchemy_repository import SqlAlchemyRepository
from app.repository.base_repository import T
from app.models import Matches, Players


class MatchesRepository(SqlAlchemyRepository):
    __model_name__ = Matches

    def find_finished_matches_by_player_name(self, name: str) -> list[Matches]:
        player1 = aliased(Players)
        player2 = aliased(Players)
        winner = aliased(Players)

        return self._session.query(
            Matches.uuid,
            player1.name.label('player1_name'),
            player2.name.label('player2_name'),
            winner.name.label('winner')
        ).join(
            player1, Matches.player1_id == player1.id
        ).join(
            player2, Matches.player2_id == player2.id
        ).join(
            winner, Matches.winner_id == winner.id
        ).filter(or_(player1.name.contains(name), player2.name.contains(name))).all()

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
