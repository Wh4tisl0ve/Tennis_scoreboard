from uuid import UUID
from dataclasses import dataclass

from app.tennis_logic.tennis import Tennis


@dataclass(frozen=True)
class Match:
    uuid: UUID
    player1_id: int
    player2_id: int
    tennis: Tennis
    winner_id: int = None
