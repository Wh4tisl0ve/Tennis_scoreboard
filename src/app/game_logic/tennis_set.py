from app.game_logic.tennis_game import TennisGame, StatusGame
from app.game_logic.tennis_point import TennisPoint
from app.observer.observer import Observer


class TennisSet(Observer):
    def __init__(self, game: TennisGame):
        self.__game = game
        self.__player1_value = 0
        self.__player2_value = 0

    def update(self, observer: TennisPoint):
        match self.__game.state:
            case StatusGame.NORMAL:
                if observer.is_last_point():
                    self.win_set()
            case StatusGame.DRAW:
                self.__game.state = StatusGame.AD
            case StatusGame.AD:
                if self.__game.is_diff_two_point():
                    self.win_set()
                else:
                    print('Плейер2 Минус очко')

        if self.__game.is_last_stage():
            self.set_state_draw()

    def set_state_draw(self):
        if self.__game.is_point_equals():
            self.__game.state = StatusGame.DRAW

    def win_set(self):
        if self.__game.player1_point > self.__game.player2_point:
            self.__player1_value += 1
        else:
            self.__player2_value += 1
        # сюда notify
        self.__game.reset()

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
