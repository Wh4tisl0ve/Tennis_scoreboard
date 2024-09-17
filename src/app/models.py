from typing import Annotated, List
from uuid import UUID

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column, relationship
from sqlalchemy.sql import sqltypes
import uuid


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class Players(Base):
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False, index=True)

    matches: Mapped[List["matches"]] = relationship(back_populates="Matches", cascade="all, delete")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}"

    def __repr__(self):
        return str(self)


class Matches(Base):
    fk_players = Annotated[int, mapped_column(ForeignKey(Players.id, ondelete="CASCADE"), nullable=False)]

    uuid: Mapped[UUID] = mapped_column(String(36), default=uuid.uuid4)
    player1_id: Mapped[fk_players]
    player2_id: Mapped[fk_players]
    winner_id: Mapped[fk_players]
    score: Mapped[str] = mapped_column(String(255))

    player1: Mapped["player1"] = relationship(back_populates="Players")
    player2: Mapped["player2"] = relationship(back_populates="Players")
    winner: Mapped["winner"] = relationship(back_populates="Players")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id},"
                f"uuid={self.uuid},"
                f"player1={self.player1_id},"
                f"player2={self.player2_id},"
                f"winner={self.winner_id},"
                f"score={self.score})")

    def __repr__(self):
        return str(self)
