from src.app.models.base_model import BaseModel
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import VARCHAR
from typing import List


class Players(BaseModel):
    name: Mapped[str] = mapped_column(VARCHAR(30), unique=True, nullable=False)

    matches: Mapped[List["matches"]] = relationship(back_populates="Matches", cascade="all, delete")

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}"

    def __repr__(self):
        return str(self)
