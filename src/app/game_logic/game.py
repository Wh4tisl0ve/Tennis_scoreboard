from app.game_logic.point import Point
from enum import Enum


class StatusGame(Enum):
    NORMAL = 0
    DRAW = -1
    AD = 1


class Game:
    point_table = {
        0: "0",
        1: "15",
        2: "30",
        3: "40",
        4: "AD"
    }

    def __init__(self):
        self.__player1_point = Point()
        self.__player2_point = Point()
        self.status = StatusGame.NORMAL

    def set_status_normal(self):
        self.status = StatusGame.NORMAL

    def set_status_draw(self):
        self.status = StatusGame.DRAW

    def set_status_ad(self):
        self.status = StatusGame.AD

    def get_status(self):
        return self.status

    def add_point_player1(self) -> None:
        self.__player1_point.add_point()

    def add_point_player2(self) -> None:
        self.__player2_point.add_point()

    def minus_point_player1(self):
        self.__player1_point.minus_point()

    def minus_point_player2(self):
        self.__player2_point.minus_point()

    def get_player1_point(self) -> Point:
        return self.__player1_point

    def get_player2_point(self) -> Point:
        return self.__player2_point

    def is_last_point(self):
        return self.__player1_point.get_point_value() == 3 or self.__player2_point.get_point_value() == 3

    def is_point_equals(self) -> bool:
        return self.__player1_point.get_point_value() == self.__player2_point.get_point_value()

    def get_point_value(self, pointer: int) -> str:
        return self.point_table[pointer]

    def reset(self):
        self.set_status_normal()
        self.__player1_point.reset_value()
        self.__player2_point.reset_value()

    def get_dict(self) -> dict:
        return {"player1_point": {"value": self.get_point_value(self.__player1_point.get_point_value())},
                "player2_point": {"value": self.get_point_value(self.__player2_point.get_point_value())}
                }
