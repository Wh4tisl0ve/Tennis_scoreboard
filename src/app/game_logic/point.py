class Point:
    def __init__(self):
        self.__value = 0

    def get_point_value(self) -> int:
        return self.__value

    def add_point(self) -> None:
        self.__value += 1

    def minus_point(self) -> None:
        self.__value -= 1

    def reset_value(self) -> None:
        self.__value = 0