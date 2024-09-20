class Point:
    def __init__(self):
        self.__value = 0

    @property
    def point_value(self) -> int:
        return self.__value

    def add_point(self) -> None:
        self.__value += 1

    def minus_point(self) -> None:
        self.__value -= 1

    def reset_value(self) -> None:
        self.__value = 0

    def is_last_point(self) -> bool:
        return self.__value == 3

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Point)):
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
