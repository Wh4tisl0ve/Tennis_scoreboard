from app.game_logic.match import Match
from app.game_logic.game import Game, StatusGame
from app.game_logic.set import GameSet


class TennisGame:
    def __init__(self):
        self.game: Game = Game()
        self.game_set: GameSet = GameSet(self.game)
        self.match: Match = Match(self.game_set)

    def player1_goals(self):
        # ЭТО ЛОГИКА ПОДСЧЕТА СЕТОВ, ТАК ЧТО ЭТО НАДО ТУДА
        match self.game.get_status():
            case StatusGame.NORMAL:
                if self.game.get_player1_pointer() == 3:
                    self.match.update()
                    self.game.reset()
                    return
                self.game.add_point_player1()
            case StatusGame.DRAW:
                self.game.add_point_player1()
                if (self.game.get_player1_pointer() - self.game.get_player2_pointer()) == 1:
                    self.game.set_status_ad()
            case StatusGame.AD:
                if (self.game.get_player1_pointer() + 1 - self.game.get_player2_pointer()) == 2:
                    self.match.update()
                    self.game.reset()
                else:
                    self.game.minus_point_player2()

        if self.game.is_last_point():
            if self.game.is_point_equals():
                self.game.set_status_draw()

    def player2_goals(self):
        match self.game.get_status():
            case StatusGame.NORMAL:
                if self.game.get_player2_pointer() == 3:
                    self.match.update()
                    self.game.reset()
                    return
                self.game.add_point_player2()
            case StatusGame.DRAW:
                self.game.add_point_player2()
                if (self.game.get_player2_pointer() - self.game.get_player1_pointer()) == 1:
                    self.game.set_status_ad()
            case StatusGame.AD:
                if (self.game.get_player2_pointer() + 1 - self.game.get_player1_pointer()) == 2:
                    self.match.update()
                    self.game.reset()
                else:
                    self.game.minus_point_player1()

        if self.game.is_last_point():
            if self.game.is_point_equals():
                self.game.set_status_draw()

    def get_dict(self) -> dict:
        return self.match.get_dict()
