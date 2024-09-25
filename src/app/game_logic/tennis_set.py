from app.game_logic.tennis_model import TennisModel
from app.game_logic.tennis_game import TennisGame
from app.game_logic.state_game import State


class TennisSet(TennisModel):
    def __init__(self, tennis_game: TennisGame):
        super().__init__()
        self.__tennis_game: TennisGame = tennis_game

    def update(self):
        match self._state:
            case State.NORMAL:
                if self.__tennis_game.is_last_stage():
                    if self.__tennis_game.is_diff_two_point() and self.__tennis_game.is_points_not_last_stage():
                        self.win()
            case State.DRAW:
                self.__tennis_game.set_state(State.AD)
                self.set_state(State.AD)
            case State.AD:
                if self.__tennis_game.is_diff_two_point():
                    self.win()

        if self.__tennis_game.is_last_stage() and self.__tennis_game.is_value_equals():
            self.__tennis_game.set_state(State.DRAW)
            self._state = State.DRAW

    def win(self):
        if self.__tennis_game._player1_value > self.__tennis_game._player2_value:
            self._player1_value += 1
        else:
            self._player2_value += 1

        self.__tennis_game.reset_value()
