from app.game_logic.game import Game, StatusGame
from app.game_logic.point import Point


class GameSet:
    def __init__(self, game: Game):
        self.__game = game
        self.__player1_value = 0
        self.__player2_value = 0

    def add_set_value(self):
        if self.__game.get_player1_point().get_point_value() > self.__game.get_player2_point().get_point_value():
            self.__player1_value += 1
        else:
            self.__player2_value += 1

    def calc_set(self, player1_point: Point, player2_point: Point):
        match self.__game.get_status():
            case StatusGame.NORMAL:
                if player1_point.get_point_value() == 3:
                    self.add_set_value()
                    self.__game.reset()
                    return
                player1_point.add_point()
            case StatusGame.DRAW:
                player1_point.add_point()
                if (player1_point.get_point_value() - player2_point.get_point_value() ) == 1:
                    self.__game.set_status_ad()
            case StatusGame.AD:
                if (player1_point.get_point_value() + 1 - player2_point.get_point_value()) == 2:
                    self.add_set_value()
                    self.__game.reset()
                else:
                    player2_point.minus_point()

        if self.__game.is_last_point():
            if self.__game.is_point_equals():
                self.__game.set_status_draw()

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
