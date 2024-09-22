from app.observer.observer import Observer, Subject
from app.game_logic.tennis_point import TennisPoint
from enum import Enum


class StatusGame(Enum):
    NORMAL = 0
    DRAW = -1
    AD = 1


class TennisGame(Observer, Subject):
    _observer: Observer | None = None

    def __init__(self):
        self.__player1_point: TennisPoint = TennisPoint()
        self.__player2_point: TennisPoint = TennisPoint()
        self.__state: StatusGame = StatusGame.NORMAL

    def update(self, observer: TennisPoint):
        match self.__state:
            case StatusGame.NORMAL:
                if observer.is_last_point():
                    self.notify_subscribers()
                    self.reset()
                else:
                    observer.plus_point()
            case StatusGame.DRAW:
                observer.plus_point()
                self.__state = StatusGame.AD
            case StatusGame.AD:
                enemy = self.get_enemy(observer)
                if observer.point_value + 1 - enemy.point_value == 2:
                    self.notify_subscribers()
                    self.reset()
                else:
                    enemy.minus_point()

        if self.is_last_stage():
            if self.is_point_equals():
                self.__state = StatusGame.DRAW

    def notify_subscribers(self):
        if self._observer is not None:
            self._observer.update(self)

    def attach(self, observer: Observer) -> None:
        self._observer = observer

    @property
    def player1_point(self) -> TennisPoint:
        return self.__player1_point

    @property
    def player2_point(self) -> TennisPoint:
        return self.__player2_point

    def is_last_stage(self) -> bool:
        return self.__player1_point.is_last_point() or self.__player2_point.is_last_point()

    def is_point_equals(self) -> bool:
        return self.__player1_point == self.__player2_point

    def get_enemy(self, player_point: TennisPoint) -> TennisPoint:
        enemy_point = {self.__player1_point: self.__player2_point,
                       self.__player2_point: self.__player1_point}

        return enemy_point[player_point]

    def reset(self) -> None:
        self.__state = StatusGame.NORMAL
        self.__player1_point.reset_value()
        self.__player2_point.reset_value()

    def get_dict(self) -> dict:
        return {"player1_point": {"value": self.__player1_point.get_value()},
                "player2_point": {"value": self.__player2_point.get_value()}
                }
