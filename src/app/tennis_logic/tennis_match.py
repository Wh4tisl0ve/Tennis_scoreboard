from src.app.tennis_logic.tennis_model import TennisModel
from src.app.tennis_logic.tennis_set import TennisSet
from src.app.tennis_logic.state_game import State


class TennisMatch(TennisModel):
    def __init__(self, tennis_set: TennisSet):
        super().__init__()
        self._child_model: TennisSet = tennis_set
        self._last_point: int = 2

    def update(self) -> None:
        if self._child_model.is_last_stage() and not self.is_diff_two_point():
            match self._state:
                case State.NORMAL:
                    if self._child_model.is_diff_two_point():
                        self.win()
                        return
                case State.TIE_BREAK:
                    if self.is_child_value_diff_one_point():
                        self.win()
                        return

            if self._child_model.is_equals_value():
                self.set_state(State.TIE_BREAK)

    def is_child_value_diff_one_point(self) -> bool:
        return abs(self._child_model._player1_value - self._child_model._player2_value) >= 1

