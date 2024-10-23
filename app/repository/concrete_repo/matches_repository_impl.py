from uuid import UUID

from sqlalchemy import select, update, or_, text
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import aliased

from app.database_engine import db_engine_mysql
from app.exceptions import NotFoundError
from app.models import Matches, Players
from app.repository.interfaces.base_repository import T
from app.repository.interfaces.matches_repository import MatchesRepository


class MatchesRepositoryImpl(MatchesRepository):
    def __init__(self):
        self.__session_factory = db_engine_mysql.get_session_factory()

    def find_finished_matches(self, name: str = '', current_page: int = 1, items_per_page: int = 5) -> list[Matches]:
        player1 = aliased(Players)
        player2 = aliased(Players)
        winner = aliased(Players)
        with self.__session_factory() as session:
            statement = (
                session.query(
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

        return statement

    def find_count_finished_matches(self, name: str = '') -> int:
        statement = text("SELECT COUNT(*) "
                         "FROM Matches m "
                         "INNER JOIN Players p1 ON p1.id = m.player1_id "
                         "INNER JOIN Players p2 ON p2.id = m.player2_id "
                         "WHERE is_end_game AND (p1.name LIKE :name OR p2.name LIKE :name)")
        with self.__session_factory() as session:
            result = session.execute(statement, {'name': f'%{name}%'})

        return result.scalar()

    def find_by_uuid(self, uuid: UUID) -> Matches:
        try:
            statement = select(Matches).filter(Matches.uuid == uuid)
            with self.__session_factory() as session:
                result = session.execute(statement).scalar_one()
            return result
        except (TypeError, NoResultFound):
            raise NotFoundError(f'Матч с uuid = {uuid} не был найден')

    def add_winner_id_by_uuid(self, uuid: str, winner_id: int) -> None:
        statement = update(Matches).where(Matches.uuid == uuid).values(winner_id=winner_id, is_end_game=True)
        with self.__session_factory() as session:
            session.execute(statement)
            session.commit()

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
