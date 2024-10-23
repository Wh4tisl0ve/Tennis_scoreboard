from sqlalchemy import select

from app.database_engine import db_engine_mysql
from app.models import Players
from app.repository.interfaces.base_repository import T
from app.repository.interfaces.players_repository import PlayersRepository


class PlayersRepositoryImpl(PlayersRepository):

    def __init__(self):
        self.__session_factory = db_engine_mysql.get_session_factory()

    def find_by_name(self, name: str = '') -> Players:
        statement = select(Players).filter(Players.name == name)
        with self.__session_factory() as session:
            result = session.execute(statement).scalar_one()
        return result

    def create(self, entity: T) -> T:
        with self.__session_factory() as session:
            session.add(entity)
            session.commit()

        return entity

    def find_by_id(self, id_player: int) -> T:
        statement = select(Players).filter(Players.id == id_player)
        with self.__session_factory() as session:
            result = session.execute(statement).scalar_one()
        return result

    def delete(self) -> T:
        pass

    def update(self) -> T:
        pass
