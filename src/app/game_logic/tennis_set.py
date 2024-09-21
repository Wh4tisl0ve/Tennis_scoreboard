from app.game_logic.tennis_game import TennisGame, StatusGame
from app.game_logic.tennis_point import TennisPoint


class TennisSet:
    def __init__(self, game: TennisGame):
        self.__game = game
        self.__player1_value = 0
        self.__player2_value = 0

    def calc_set(self, player1_point: TennisPoint, player2_point: TennisPoint):
        match self.__game.state:
            case StatusGame.NORMAL:
                if player1_point.is_last_point():
                    self.win_set()
                else:
                    player1_point.add_point()
            case StatusGame.DRAW:
                player1_point.add_point()
                self.__game.state = StatusGame.AD
            case StatusGame.AD:
                if (player1_point.point_value + 1 - player2_point.point_value) == 2:
                    self.win_set()
                else:
                    player2_point.minus_point()

        if self.__game.is_last_stage():
            self.set_state_draw()

    def set_state_draw(self):
        if self.__game.is_point_equals():
            self.__game.state = StatusGame.DRAW

    def win_set(self):
        if self.__game.player1_point > self.__game.player2_point:
            self.__player1_value += 1
        else:
            self.__player2_value += 1

        self.__game.reset()

    def get_dict(self) -> dict:
        return {"player1_set":
            {
                "value": self.__player1_value,
                "player1_point": self.__game.get_dict()["player1_point"]
            },
            "player2_set":
                {
                    "value": self.__player2_value,
                    "player2_point": self.__game.get_dict()["player2_point"]
                }
        }
