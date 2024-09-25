from app.game_logic.tennis_set import TennisSet
from app.game_logic.tennis_match import TennisMatch
from app.game_logic.tennis_game import TennisGame
from app.game_logic.tennis_match import TennisMatch


class Tennis:
    def __init__(self):
        self.__tennis_game: TennisGame = TennisGame()
        self.__tennis_set: TennisSet = TennisSet(self.__tennis_game)
        self.__tennis_match: TennisMatch = TennisMatch(self.__tennis_set)

    def player1_goals(self):
        self.__tennis_game.add_value_player1()
        self.update()

    def player2_goals(self):
        self.__tennis_game.add_value_player2()
        self.update()

    def update(self):
        self.__tennis_set.update()
        self.__tennis_match.update()

    def get_dict(self) -> dict:
        dict_game = {
            "game": self.__tennis_game.get_dict(),
            "set": self.__tennis_set.get_dict(),
            "match": self.__tennis_match.get_dict()
        }
        return dict_game
