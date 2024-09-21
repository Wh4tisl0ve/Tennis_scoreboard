from app.game_logic.tennis_point import TennisPoint
from enum import Enum


class StatusGame(Enum):
    NORMAL = 0
    DRAW = -1
    AD = 1


# почистить класс
class TennisGame:
    def __init__(self):
        self.__player1_point = TennisPoint()
        self.__player2_point = TennisPoint()
        self.__state = StatusGame.NORMAL

    @property
    def player1_point(self) -> TennisPoint:
        return self.__player1_point

    @property
    def player2_point(self) -> TennisPoint:
        return self.__player2_point

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, status: StatusGame):
        self.__state = status

    def is_last_stage(self):
        return self.__player1_point.is_last_point() or self.__player2_point.is_last_point()

    def is_point_equals(self) -> bool:
        return self.__player1_point == self.__player2_point

    def reset(self):
        self.__state = StatusGame.NORMAL
        self.__player1_point.reset_value()
        self.__player2_point.reset_value()

    def get_dict(self) -> dict:
        return {"player1_point": {"value": self.__player1_point.point_value},
                "player2_point": {"value": self.__player2_point.point_value}
                }
