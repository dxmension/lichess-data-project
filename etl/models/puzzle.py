from sqlalchemy import Column, ForeignKey, String, Integer, DateTime
from sqlalchemy.orm import relationship
from etl.database import Base

class Puzzle(Base):
    __tablename__ = "puzzles"

    id = Column(Integer, primary_key=True, nullable=False)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="cascade"), index=True, nullable=False)

    theme = Column(String)
    status = Column(String)
    rating = Column(String)

    played_at = Column(DateTime)

    player = relationship("Player", back_populates="puzzle", passive_deletes=True)