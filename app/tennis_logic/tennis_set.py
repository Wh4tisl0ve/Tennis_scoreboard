from app.tennis_logic.tennis_model import TennisModel
from app.tennis_logic.tennis_game import TennisGame
from app.tennis_logic.state_game import State


class TennisSet(TennisModel):
    def __init__(self, tennis_game: TennisGame):
        super().__init__()
        self._child_model: TennisGame = tennis_game
        self._last_point: int = 6

    def update(self) -> None:
        if self._child_model.is_last_stage():
            match self._state:
                case State.NORMAL:
                    if self._child_model.is_points_not_last_value() and self._child_model.is_diff_two_point():
                        self.win()
                        return
                case State.DRAW:
                    self.set_state(State.AD)
                case _:
                    if self._child_model.is_diff_two_point():
                        self.win()
                        return

            if self._child_model.is_equals_value():
                self.set_state(State.DRAW)

    def is_diff_one_point(self) -> bool:
        return abs(self._player1_value - self._player2_value) >= 1
