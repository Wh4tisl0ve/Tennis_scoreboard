from app.models import Matches, MatchStory
from app.repository.match_story_repository import matches_story_repo
from app.repository.matches_repository import matches_repo
from app.repository.players_repository import players_repo
from app.tennis_logic.tennis import Tennis


class MatchScoreService:
    def serialize_tennis(self, match: Matches) -> dict:
        player1 = players_repo.find_by_id(match.player1_id)
        player2 = players_repo.find_by_id(match.player2_id)

        tennis_serialize = {"uuid": match.uuid,
                            "player1_name": player1.name,
                            "player2_name": player2.name}

        return tennis_serialize

    def add_winner(self, tennis: Tennis, match: Matches) -> None:
        if tennis.get_winner_id() == 1:
            matches_repo.add_winner_id_by_uuid(match.uuid, match.player1_id)
        else:
            matches_repo.add_winner_id_by_uuid(match.uuid, match.player2_id)

    def deserialize_tennis(self, match: Matches) -> Tennis:
        last_record_story = matches_story_repo.get_last_record_story_by_match_id(match.id)

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
        matches_story_repo.add(match_story_record)


match_score_service = MatchScoreService()
