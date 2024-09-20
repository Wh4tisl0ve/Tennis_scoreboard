from app.game_logic.game import Game


class GameSet:
    def __init__(self, game: Game):
        self.__game = game
        self.__player1_value = 0
        self.__player2_value = 0

    def update(self):
        self.add_set_value()
        self.__game.reset()

    def add_set_value(self):
        if self.__game.get_player1_pointer() > self.__game.get_player2_pointer():
            self.__player1_value += 1
        else:
            self.__player2_value += 1

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
