

from typing import Callable

from app.game_logic.state_game import State
from app.game_logic.tennis_model import TennisModel


class TennisGame(TennisModel):
    point_table = ["0", "15", "30", "40", "AD"]

    def __init__(self):
        super().__init__()
        self._last_point = 3

    def get_value(self, value: int) -> str:
        if self._state == State.TIE_BREAK:
            return str(value)
        else:
            return self.point_table[value]

    def get_enemy_action(self, player_value: int) -> Callable:
        dict_enemy = {self._player1_value: self.minus_point_player2,
                      self._player2_value: self.minus_point_player1}

        return dict_enemy[player_value]

    def add_value_player1(self) -> None:
        if not self.is_advantage():
            self._player1_value += 1
        else:
            self.get_enemy_action(self._player1_value)()

    def add_value_player2(self) -> None:
        if not self.is_advantage():
            self._player2_value += 1
        else:
            self.get_enemy_action(self._player2_value)()

    def is_advantage(self):
        return self.is_last_stage() and self._state == State.AD

    def minus_point_player1(self) -> None:
        self._player1_value -= 1

    def minus_point_player2(self) -> None:
        self._player2_value -= 1

    def get_dict(self) -> dict:
        return {"player1_value": self.get_value(self._player1_value),
                "player2_value": self.get_value(self._player2_value)}
