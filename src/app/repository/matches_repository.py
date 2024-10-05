from app.repository.base_repository import T
from app.models import Matches
from app.repository.sqlalchemy_repository import SqlAlchemyRepository


class MatchesRepository(SqlAlchemyRepository):
    __model_name__ = Matches

    # сюда передается сформированный матч
    def add(self, match: Matches) -> Matches:
        self._session.add(match)

        self._session.flush()
        self._session.commit()

        return match

    def delete(self, entity: T) -> T:
        pass

    def update(self, entity: T) -> None:
        pass
