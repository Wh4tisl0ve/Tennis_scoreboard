from app.models import Players
from app.repository.sqlalchemy_repository import SqlAlchemyRepository


class PlayersRepository(SqlAlchemyRepository):
    __model_name__ = Players

    def find_by_name(self, name: str) -> Players:
        query_filter_player = self._session.query(Players).filter(Players.name == name)
        return self._session.execute(query_filter_player).one()

    def update(self, player: Players) -> None:
        pass

    def delete(self, player: Players) -> Players:
        pass


players_repo = PlayersRepository()