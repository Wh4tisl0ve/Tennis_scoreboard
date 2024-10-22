from app.tennis_logic.tennis_game import TennisGame
from app.tennis_logic.tennis_match import TennisMatch
from app.tennis_logic.tennis_set import TennisSet


class Tennis:
    def __init__(self):
        self.__tennis_game: TennisGame = TennisGame()
        self.__tennis_set: TennisSet = TennisSet(self.__tennis_game)
        self.__tennis_match: TennisMatch = TennisMatch(self.__tennis_set)
        self.__is_game_end: bool = False

    @property
    def is_end_game(self) -> bool:
        return self.__is_game_end

    def player1_goals(self) -> None:
        if not self.__is_game_end:
            self.__tennis_game.add_value_player1()
            self.update()

    def player2_goals(self) -> None:
        if not self.__is_game_end:
            self.__tennis_game.add_value_player2()
            self.update()

    def update(self) -> None:
        self.__tennis_set.update()
        self.__tennis_match.update()
        self.set_end_game()

    def set_end_game(self) -> None:
        if self.__tennis_match.is_last_stage():
            self.__is_game_end = True

    def get_winner_id(self) -> int:
        if self.__tennis_match.player1_value > self.__tennis_match.player2_value:
            return 1
        else:
            return 2

    def to_dict(self) -> dict:
        dict_game = {
            "game": self.__tennis_game.to_dict(),
            "set": self.__tennis_set.to_dict(),
            "match": self.__tennis_match.to_dict()
        }
        return dict_game

    def to_render(self) -> dict:
        dict_game = {
            "game": self.__tennis_game.to_render(),
            "set": self.__tennis_set.to_dict(),
            "match": self.__tennis_match.to_dict()
        }
        return dict_game

    def status_to_dict(self) -> dict:
        dict_status = {
            "game_status": self.__tennis_game.state,
            "set_status": self.__tennis_set.state,
            "match_status": self.__tennis_match.state
        }
        return dict_status

    def deserialize_dict(self, dict_tennis: dict, dict_state: dict) -> None:
        self.__tennis_game.deserialize(dict_tennis['game'], dict_state.get('game_status', 0))
        self.__tennis_set.deserialize(dict_tennis['set'], dict_state.get('set_status', 0))
        self.__tennis_match.deserialize(dict_tennis['match'], dict_state.get('match_status', 0))
        self.set_end_game()
