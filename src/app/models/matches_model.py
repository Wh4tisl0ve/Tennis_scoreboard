from src.app.models.base_model import BaseModel
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import UUID, ForeignKey
from typing import Annotated, List
import uuid


class Matches(BaseModel):
    fk_players = Annotated[int, mapped_column(ForeignKey("Players.id", ondelete="CASCADE"), nullable=False)]

    uuid: Mapped[UUID] = mapped_column(default=uuid.uuid4)
    player1: Mapped[fk_players]
    player2: Mapped[fk_players]
    winner: Mapped[fk_players]
    score: Mapped[str]

    players: Mapped[List["players"]] = relationship(back_populates="Players", cascade="all, delete")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"uuid={self.uuid},"
                f"player1={self.player1},"
                f"player2={self.player2},"
                f"winner={self.winner},"
                f"score={self.score})")

    def __repr__(self):
        return str(self)
