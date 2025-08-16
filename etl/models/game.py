from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from etl.database import Base

class Game(Base):
    __tablename__ = "games"

    id = Column(String, primary_key=True, nullable=False)
    player_id = Column(Integer, ForeignKey("players.id", ondelete="cascade"), nullable=False, index=True)

    variant = Column(String)
    speed = Column(String)
    perf = Column(String)
    opening = Column(String, nullable=True)

    status = Column(String)

    duration = Column(Integer, nullable=True)
    rating_diff = Column(Integer)
    move_count = Column(Integer)
    played_at = Column(DateTime)

    player = relationship("Player", back_populates="games", passive_deletes=True)