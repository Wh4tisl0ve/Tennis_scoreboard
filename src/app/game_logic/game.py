class Game:
    point_table = {
        0: "0",
        1: "15",
        2: "30",
        3: "40",
        4: "AD"
    }

    def __init__(self):
        self.__player1_pointer = 0
        self.__player2_pointer = 0

    def add_point_player1(self) -> None:
        self.__player1_pointer += 1

    def add_point_player2(self) -> None:
        self.__player2_pointer += 1

    def get_player1_pointer(self) -> int:
        return self.__player1_pointer

    def get_player2_pointer(self) -> int:
        return self.__player2_pointer

    def is_last_point(self):
        return self.__player1_pointer == 3 or self.__player2_pointer == 3

    def is_point_equals(self) -> bool:
        return self.__player1_pointer == self.__player2_pointer

    def get_point_value(self, pointer: int) -> str:
        return self.point_table[pointer]

    def reset_pointer(self):
        self.__player1_pointer = 0
        self.__player2_pointer = 0

    def get_dict(self) -> dict:
        return {"player1_point": self.get_point_value(self.__player1_pointer),
                "player2_point": self.get_point_value(self.__player2_pointer)
                }
