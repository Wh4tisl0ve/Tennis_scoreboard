import uuid
from typing import List
from uuid import UUID

from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Boolean, JSON, Integer


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Players(Base):
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False, index=True)

    matches_player1: Mapped[List["Matches"]] = relationship("Matches",
                                                            back_populates="player1",
                                                            cascade="all, delete",
                                                            foreign_keys="Matches.player1_id")
    matches_player2: Mapped[List["Matches"]] = relationship("Matches",
                                                            back_populates="player2",
                                                            cascade="all, delete",
                                                            foreign_keys="Matches.player2_id")
    matches_winner: Mapped[List["Matches"]] = relationship("Matches",
                                                           back_populates="winner",
                                                           cascade="all, delete",
                                                           foreign_keys="Matches.winner_id")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name})"

    def __repr__(self):
        return str(self)


class Matches(Base):
    uuid: Mapped[UUID] = mapped_column(String(36), default=uuid.uuid4)
    player1_id: Mapped[int] = mapped_column(ForeignKey(Players.id, ondelete="CASCADE"), nullable=False)
    player2_id: Mapped[int] = mapped_column(ForeignKey(Players.id, ondelete="CASCADE"), nullable=False)
    winner_id: Mapped[int] = mapped_column(ForeignKey(Players.id, ondelete="CASCADE"), nullable=True)
    is_end_game: Mapped[bool] = mapped_column(Boolean, default=False)

    player1: Mapped["Players"] = relationship("Players", foreign_keys=[player1_id])
    player2: Mapped["Players"] = relationship("Players", foreign_keys=[player2_id])
    winner: Mapped["Players"] = relationship("Players", foreign_keys=[winner_id])

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"uuid={self.uuid},"
                f"player1={self.player1_id},"
                f"player2={self.player2_id},"
                f"winner={self.winner_id})")

    def __repr__(self):
        return str(self)


class MatchStory(Base):
    id_match: Mapped[int] = mapped_column(ForeignKey(Matches.id, ondelete="CASCADE"), nullable=False)
    score: Mapped[dict] = mapped_column(JSON, nullable=False)
    match_status: Mapped[dict] = mapped_column(JSON, nullable=False)
    player_goal: Mapped[int] = mapped_column(Integer, nullable=True)

    match: Mapped["Matches"] = relationship("Matches", foreign_keys=[id_match])

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"id_match={self.id_match},"
                f"score={self.score},"
                f"match_status={self.match_status},"
                f"player_goal={self.player_goal})")

    def __repr__(self):
        return str(self)
