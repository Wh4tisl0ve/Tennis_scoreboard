from enum import Enum


class StatePoint(Enum):
    NORMAL = 0
    TIE_BREAK = 1


class TennisPoint:
    point_table = {
        0: 0,
        1: 15,
        2: 30,
        3: 40,
        4: "AD"
    }

    def __init__(self):
        self.__value = 0
        self.__last_point = 3
        self.__state = StatePoint.NORMAL

    @property
    def point_value(self) -> int:
        if self.__state == StatePoint.NORMAL:
            return self.point_table[self.__value]
        else:
            return self.__value

    def add_point(self) -> None:
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

    def __eq__(self, other):
        self.__verify_data(other)
        return self.__value == other.__value

    def __lt__(self, other):
        self.__verify_data(other)
        return self.__value < other.__value

    def __gt__(self, other):
        self.__verify_data(other)
        return self.__value > other.__value
