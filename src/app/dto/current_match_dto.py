from dataclasses import dataclass


@dataclass(frozen=True)
class CurrentMatchDTO:
    player1_name: str
    player2_name: str
    tennis_serialize: dict
