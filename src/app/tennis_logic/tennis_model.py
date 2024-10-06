from abc import ABC

from src.app.tennis_logic.state_game import State


class TennisModel(ABC):
    _state: State = State.NORMAL

    def __init__(self):
        self._player1_value: int = 0
        self._player2_value: int = 0
        self._child_model: TennisModel | None = None

    @property
    def player1_value(self) -> int:
        return self._player1_value

    @property
    def player2_value(self) -> int:
        return self._player2_value

    def set_state(self, state: State) -> None:
        self._state = state
        self._child_model.set_state(state)

    def win(self) -> None:
        if self._child_model._player1_value > self._child_model._player2_value:
            self._player1_value += 1
        else:
            self._player2_value += 1

        self.reset()

    def is_last_stage(self) -> bool:
        return self._player1_value >= self._last_point or self._player2_value >= self._last_point

    def is_points_not_last_value(self) -> bool:
        return self._player1_value != self._last_point and self._player2_value != self._last_point

    def is_equals_value(self) -> bool:
        return self._player1_value == self._player2_value

    def is_diff_two_point(self) -> bool:
        return abs(self._player1_value - self._player2_value) >= 2

    def reset(self) -> None:
        self.set_state(State.NORMAL)
        self._child_model._player1_value = 0
        self._child_model._player2_value = 0

    def get_dict(self) -> dict:
        return {"player1_value": str(self._player1_value),
                "player2_value": str(self._player2_value)}
