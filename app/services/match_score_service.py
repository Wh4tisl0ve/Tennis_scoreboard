from app.models import Matches, MatchStory
from app.repository.interfaces.match_story_repository import MatchStoryRepository
from app.repository.interfaces.matches_repository import MatchesRepository
from app.repository.interfaces.players_repository import PlayersRepository

from app.tennis_logic.tennis import Tennis


class MatchScoreService:
    def __init__(self, matches_repo: MatchesRepository,
                 players_repo: PlayersRepository,
                 matches_story_repo: MatchStoryRepository):
        self.__matches_repo = matches_repo
        self.__players_repo = players_repo
        self.__matches_story_repo = matches_story_repo

    def serialize_tennis(self, match: Matches) -> dict:
        player1 = self.__players_repo.find_by_id(match.player1_id)
        player2 = self.__players_repo.find_by_id(match.player2_id)

        tennis_serialize = {"uuid": match.uuid,
                            "player1_name": player1.name,
                            "player2_name": player2.name}

        return tennis_serialize

    def add_winner(self, tennis: Tennis, match: Matches) -> None:
        uuid = match.uuid
        if tennis.get_winner_id() == 1:
            winner_id = match.player1_id
        else:
            winner_id = match.player2_id
        self.__matches_repo.add_winner_id_by_uuid(uuid, winner_id)

    def deserialize_tennis(self, match: Matches) -> Tennis:
        last_record_story = self.__matches_story_repo.find_last_record_story_by_match_id(match.id)

        tennis = Tennis()
        tennis.deserialize_dict(last_record_story.score, last_record_story.match_status)

        return tennis

    def player_goals(self, player_scored_id: str, tennis: Tennis, match: Matches) -> None:
        if player_scored_id == '1':
            tennis.player1_goals()
        else:
            tennis.player2_goals()

        match_story_record = MatchStory(id_match=match.id,
                                        score=tennis.to_dict(),
                                        match_status=tennis.status_to_dict(),
                                        player_goal=player_scored_id)
        self.__matches_story_repo.create(match_story_record)
