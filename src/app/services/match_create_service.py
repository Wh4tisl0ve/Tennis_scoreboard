from app.models import Matches, Players
from app.repository.matches_repository import matches_repo
from app.repository.players_repository import players_repo


# repo Matches, repo Players
class MatchCreateService:
    def create_match(self, player1_name: str, player2_name: str) -> Matches:
        player1 = self.get_player(player1_name)
        player2 = self.get_player(player2_name)

        match = Matches(player1_id=player1.id, player2_id=player2.id)

        return matches_repo.add(match)

    def get_player(self, name: str) -> Players:
        try:
            return players_repo.find_by_name(name)
        except:
            return players_repo.add(Players(name=name))
