from app.models import Matches


# repo Match
class MatchFinderService:
    # тут выбор определенных полей
    def get_matches_by_player_name(self, name: str) -> list[Matches]:
        return MatchesRepository().find_by_player_name(name)
