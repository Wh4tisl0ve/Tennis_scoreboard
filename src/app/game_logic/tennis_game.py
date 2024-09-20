from app.game_logic.match import Match
from app.game_logic.game import Game, StatusGame
from app.game_logic.set import GameSet


class TennisGame:
    def __init__(self):
        self.game: Game = Game()
        self.game_set: GameSet = GameSet(self.game)
        self.match: Match = Match(self.game_set)

    def player1_goals(self):
        player1_point = self.game.get_player1_point()
        player2_point = self.game.get_player2_point()
        self.game_set.calc_set(player1_point, player2_point)

    def player2_goals(self):
        player2_point = self.game.get_player2_point()
        player1_point = self.game.get_player1_point()
        self.game_set.calc_set(player2_point, player1_point)

    def get_dict(self) -> dict:
        return self.match.get_dict()
