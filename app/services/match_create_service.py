from sqlalchemy.exc import IntegrityError, NoResultFound

from app.models import Matches, Players
from app.repository.interfaces.matches_repository import MatchesRepository
from app.repository.interfaces.players_repository import PlayersRepository


class MatchCreateService:
    def __init__(self, matches_repo: MatchesRepository, players_repo: PlayersRepository):
        self.__matches_repo = matches_repo
        self.__players_repo = players_repo

    def create_match(self, player1_name: str, player2_name: str) -> Matches:
        player1 = self.get_player(player1_name)
        player2 = self.get_player(player2_name)

        match = Matches(player1_id=player1.id, player2_id=player2.id)

        return self.__matches_repo.create(match)

    def get_player(self, name: str) -> Players:
        try:
            return self.__players_repo.find_by_name(name)
        except (IntegrityError, NoResultFound):
            return self.__players_repo.create(Players(name=name))
