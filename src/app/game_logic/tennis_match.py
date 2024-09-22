from app.game_logic.tennis_set import TennisSet


class TennisMatch:
    def __init__(self, game_set: TennisSet):
        self.__set: TennisSet = game_set
        self.__player1_value: int = 0
        self.__player2_value: int = 0

    def update(self):
        # update - будет вызывать сначала update set, а потом свой
        self.__set.update()

    def get_dict(self) -> dict:
        return {"player1_match":
                    {"value": self.__player1_value,
                     "player1_set": self.__set.get_dict()['player1_set']},
                "player2_match":
                    {"value": self.__player2_value,
                     "player2_set": self.__set.get_dict()['player2_set']}
                }