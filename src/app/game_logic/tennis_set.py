from src.app.game_logic.tennis_model import TennisModel
from src.app.game_logic.tennis_game import TennisGame
from src.app.game_logic.state_game import State


class TennisSet(TennisModel):
    def __init__(self, tennis_game: TennisGame):
        super().__init__()
        self._child_model: TennisGame = tennis_game
        self._last_point: int = 6

    def update(self):
        if self._child_model.is_last_stage():
            match self._state:
                case State.NORMAL:
                    if self._child_model.is_points_not_last_value():
                        if self._child_model.is_diff_two_point():
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
