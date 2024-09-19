from app.game_logic.match import Match
from app.game_logic.game import Game
from app.game_logic.set import GameSet


class TennisGame:
    def __init__(self):
        self.game: Game = Game()
        self.game_set: GameSet = GameSet(self.game)
        self.match: Match = Match(self.game_set)

    def player1_goals(self):
        self.game.add_point_player1()
        # match update
        self.game_set.update()

    def player2_goals(self):
        self.game.add_point_player2()
        # match update
        self.game_set.update()

    def get_dict(self) -> dict:
        return self.match.get_dict()
