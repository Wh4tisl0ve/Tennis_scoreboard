from app.game_logic.tennis_match import TennisMatch
from app.game_logic.tennis_game import TennisGame
from app.game_logic.tennis_set import TennisSet


class Tennis:
    def __init__(self):
        self.__tennis_game: TennisGame = TennisGame()
        self.__tennis_set: TennisSet = TennisSet(self.__tennis_game)
        self.__tennis_match: TennisMatch = TennisMatch(self.__tennis_set)

    def player1_goals(self):
        player1_point = self.__tennis_game.player1_point
        player2_point = self.__tennis_game.player2_point
        self.__tennis_set.calc_set(player1_point, player2_point)

    def player2_goals(self):
        player2_point = self.__tennis_game.player2_point
        player1_point = self.__tennis_game.player1_point
        self.__tennis_set.calc_set(player2_point, player1_point)

    def get_dict(self) -> dict:
        return self.__tennis_match.get_dict()
