from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.orm import relationship
from etl.database import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    token = Column(String)

    blitz_rating = Column(Integer)
    rapid_rating = Column(Integer)
    classic_rating = Column(Integer)

    last_update_at = Column(DateTime)

    game = relationship("Game", back_populates="players", passive_deletes=True)
    puzzle = relationship("Puzzle", back_populates="players", passive_deletes=True)