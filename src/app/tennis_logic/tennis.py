import json

from src.app.tennis_logic.tennis_game import TennisGame
from src.app.tennis_logic.tennis_match import TennisMatch
from src.app.tennis_logic.tennis_set import TennisSet


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
        # эту проверку можно вынести ещё выше
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

    def to_json(self) -> json:
        return json.dumps(self.to_dict())

    def deserialize_json(self, dict_tennis: dict) -> None:
        self.__tennis_game.deserialize(dict_tennis['game'])
        self.__tennis_set.deserialize(dict_tennis['set'])
        self.__tennis_match.deserialize(dict_tennis['match'])
        self.set_end_game()

