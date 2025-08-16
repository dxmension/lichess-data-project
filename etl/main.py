import sys
from pathlib import Path

project_root = str(Path(__file__).parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)

from etl.models.player import Player
from etl.models.game import Game
from etl.models.puzzle import Puzzle

from etl.database import engine, Base

def init_db():
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db()