from enum import Enum


class State(Enum):
    NORMAL = 0
    DRAW = -1
    AD = 1
    TIE_BREAK = 2