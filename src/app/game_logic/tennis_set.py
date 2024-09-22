from app.game_logic.tennis_game import TennisGame, StatusGame
from app.game_logic.tennis_point import TennisPoint
from app.observer.observer import Observer


class TennisSet(Observer):
    _observer: Observer | None = None

    def __init__(self, game: TennisGame):
        self.__game: TennisGame = game
        self.__player1_value: int = 0
        self.__player2_value: int = 0

    def update(self, observer: TennisPoint):
        print('set update')

    def set_state_draw(self):
        if self.__game.is_point_equals():
            self.__game.state = StatusGame.DRAW

    def win_set(self):
        if self.__game.player1_point > self.__game.player2_point:
            self.__player1_value += 1
        else:
            self.__player2_value += 1
        self.__game.reset()
        # сюда notify

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
