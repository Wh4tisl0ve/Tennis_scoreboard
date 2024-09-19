from app.game_logic.game import Game


class GameSet:
    def __init__(self, game: Game):
        self.__game = game
        self.__player1_value = 0
        self.__player2_value = 0

    def update(self):
        if self.__game.is_last_point():
            if not self.__game.is_point_equals():
                if self.__game.get_player1_pointer() > self.__game.get_player2_pointer():
                    self.__player1_value += 1
                else:
                    self.__player2_value += 1
                self.__game.reset_pointer()
            else:
                print(self.__game.get_player1_pointer() )
                print(self.__game.get_player2_pointer() )

    def get_dict(self) -> dict:
        return {"player1_set":
            {
                "value": self.__player1_value,
                "points": self.__game.get_dict()["player1_point"]
            },
            "player2_set":
                {
                    "value": self.__player2_value,
                    "points": self.__game.get_dict()["player2_point"]
                }
        }
