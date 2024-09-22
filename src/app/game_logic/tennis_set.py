from app.game_logic.tennis_game import TennisGame, StatusGame
from app.game_logic.tennis_point import TennisPoint
from app.observer.observer import Observer, Subject
from enum import Enum


class StatusSet(Enum):
    NORMAL = 0
    TIE_BREAK = 1


class TennisSet(Observer, Subject):
    last_point = 6
    _observer: Observer | None = None

    def __init__(self, game: TennisGame):
        self.__game: TennisGame = game
        self.__state: StatusSet = StatusSet.NORMAL
        self.__player1_value: int = 0
        self.__player2_value: int = 0

    def update(self, observer: TennisGame):
        match self.__state:
            case StatusSet.NORMAL:
                self.win_set()
                if self.is_last_stage() and self.is_diff_two_game():
                    self.notify_subscribers()
                    self.reset()
            case StatusSet.TIE_BREAK:
                print('TIE_BREAK')

    def is_diff_two_game(self):
        return abs(self.__player1_value - self.player2_value) >= 2

    @property
    def player1_value(self) -> int:
        return self.__player1_value

    @property
    def player2_value(self) -> int:
        return self.__player2_value

    def notify_subscribers(self):
        if self._observer is not None:
            self._observer.update(self)

    def attach(self, observer: Observer):
        self._observer = observer

    def set_state_draw(self):
        if self.__game.is_point_equals():
            self.__game.state = StatusGame.DRAW

    def win_set(self):
        if self.__game.player1_point > self.__game.player2_point:
            self.__player1_value += 1
        else:
            self.__player2_value += 1

    def reset(self):
        self.__player1_value = 0
        self.__player2_value = 0

    def is_last_stage(self) -> bool:
        return self.__player1_value >= self.last_point or self.__player2_value >= self.last_point

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
