from app.observer.observer import Observer, Subject
from enum import Enum


class StatePoint(Enum):
    NORMAL = 0
    TIE_BREAK = 1


class TennisPoint(Subject):
    point_table = {
        0: "0",
        1: "15",
        2: "30",
        3: "40",
        4: "AD"
    }

    def __init__(self):
        self.__observer: Observer | None = None
        self.__value = 0
        self.__last_point = 3
        self.__state = StatePoint.NORMAL

    def notify_subscribers(self):
        if self.__observer is not None:
            self.__observer.update(self)

    def attach(self, observer: Observer):
        self.__observer = observer

    @property
    def point_value(self) -> int:
        return self.__value

    def get_value(self) -> str:
        if self.__state == StatePoint.NORMAL:
            return self.point_table[self.__value]
        else:
            return str(self.__value)

    def add_point(self) -> None:
        self.notify_subscribers()

    def plus_point(self):
        self.__value += 1

    def minus_point(self) -> None:
        self.__value -= 1

    def reset_value(self) -> None:
        self.__value = 0

    def is_last_point(self) -> bool:
        return self.__value == self.__last_point

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, TennisPoint)):
            raise TypeError("Операнд справа должен иметь тип int или Point")

    def __hash__(self):
        return hash(self.__value)

    def __eq__(self, other):
        self.__verify_data(other)
        return self.__value == other.__value

    def __lt__(self, other):
        self.__verify_data(other)
        return self.__value < other.__value

    def __gt__(self, other):
        self.__verify_data(other)
        return self.__value > other.__value

