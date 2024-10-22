from uuid import UUID

from sqlalchemy import select, update, or_, text
from sqlalchemy.orm import aliased

from app.exceptions import NotFoundError
from app.repository.sqlalchemy_repository import SqlAlchemyRepository
from app.models import Matches, Players


class MatchesRepository(SqlAlchemyRepository):
    __model_name__ = Matches

    def find_finished_matches(self, name: str, current_page: int, items_per_page: int) -> list[Matches]:
        player1 = aliased(Players)
        player2 = aliased(Players)
        winner = aliased(Players)

        query = (
            self._session.query(
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
            ).filter(or_(player1.name.contains(name), player2.name.contains(name)))
            .offset((current_page - 1) * items_per_page)
            .limit(items_per_page).all()
        )

        return query

    def find_count_finished_matches(self, name: str) -> int:
        query = text("SELECT COUNT(*) "
                     "FROM Matches m "
                     "INNER JOIN Players p1 ON p1.id = m.player1_id "
                     "INNER JOIN Players p2 ON p2.id = m.player2_id "
                     "WHERE is_end_game AND (p1.name LIKE :name OR p2.name LIKE :name)")

        result = self._session.execute(query, {'name': f'%{name}%'})
        return result.scalar()

    def find_by_uuid(self, uuid: UUID) -> Matches:
        try:
            return self._session.execute(select(Matches).filter(Matches.uuid == uuid)).first()[0]
        except TypeError:
            raise NotFoundError(f'Матч с uuid = {uuid} не был найден')

    def add_winner_id_by_uuid(self, uuid: str, winner_id: int) -> None:
        self._session.execute(update(Matches).where(Matches.uuid == uuid).values(winner_id=winner_id))
        self._session.execute(update(Matches).where(Matches.uuid == uuid).values(is_end_game=True))
        self._session.commit()


matches_repo = MatchesRepository()
