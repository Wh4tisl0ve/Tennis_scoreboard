from app.game_logic.state_game import State
from app.game_logic.tennis_set import TennisSet
from app.game_logic.tennis_model import TennisModel


class TennisMatch(TennisModel):
    def __init__(self, tennis_set: TennisSet):
        super().__init__()
        self.__tennis_set: TennisSet = tennis_set
        self._last_point = 6

    def update(self):
        match self._state:
            case State.NORMAL:
                if self.is_last_stage() and self.__tennis_set.is_diff_two_point():
                    self.win_set()
            case State.TIE_BREAK:
                print('TIE_BREAK')

    def win_set(self):
        if self.__tennis_set._player1_value > self.__tennis_set._player1_value:
            self._player1_value += 1
        else:
            self._player2_value += 1

        self.__tennis_set.reset_value()
