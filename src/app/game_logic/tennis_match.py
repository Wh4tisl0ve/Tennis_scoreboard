from app.game_logic.tennis_model import TennisModel
from app.game_logic.tennis_set import TennisSet
from app.game_logic.state_game import State


class TennisMatch(TennisModel):
    def __init__(self, tennis_set: TennisSet):
        super().__init__()
        self._child_model: TennisSet = tennis_set

    def update(self):
        if self._child_model.is_last_stage():
            match self._state:
                case State.NORMAL:
                    if self._child_model.is_diff_two_point():
                        self.win()
                case State.TIE_BREAK:
                    if self.is_set_diff_one_point():
                        self.win()

            if self._child_model.is_equals_value():
                self.set_state(State.TIE_BREAK)

    def is_set_diff_one_point(self):
        return abs(self._child_model._player1_value - self._child_model._player2_value) >= 1
