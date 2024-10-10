from dataclasses import dataclass

from app.tennis_logic.tennis import Tennis


@dataclass(frozen=True)
class MatchDTO:
    player1_name: str
    player2_name: str
    tennis: Tennis
