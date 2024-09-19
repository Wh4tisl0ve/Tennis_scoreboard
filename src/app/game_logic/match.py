from app.game_logic.set import GameSet


class Match:
    def __init__(self, game_set: GameSet):
        self.__set: GameSet = game_set
        self.__player1_value: int = 0
        self.__player2_value: int = 0

    # update - будет вызывать сначала update set, а потом свой
    def get_dict(self) -> dict:
        return {"player1_match":
                    {"value": self.__player1_value,
                     "player1_set": self.__set.get_dict()['player1_set']},
                "player2_match":
                    {"value": self.__player2_value,
                     "player2_set": self.__set.get_dict()['player2_set']}
                }
