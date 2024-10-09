from dataclasses import dataclass


@dataclass(frozen=True)
class PlayersNameDTO:
    player1_name: str
    player2_name: str
