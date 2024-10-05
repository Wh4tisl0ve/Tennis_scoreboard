from app.models import Players
from app.repository.sqlalchemy_repository import SqlAlchemyRepository


class PlayersRepository(SqlAlchemyRepository):
    __model_name__ = Players

    def add(self, name: str) -> Players:
        player = Players(name=name)

        self._session.add(player)
        self._session.flush()
        self._session.commit()

        return player

    def find_all_by_name(self, name: str) -> list[Players]:
        query_filter_player = self._session.query(Players).filter(Players.name.contains(name))
        return self._session.execute(query_filter_player).all()

    def update(self, player: Players) -> None:
        pass

    def delete(self, player: Players) -> Players:
        pass
