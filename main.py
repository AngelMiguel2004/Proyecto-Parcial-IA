import sys
from pyberzerk import GameState

#INicializa el juego
if __name__ == "__main__":
    gs = GameState()
    gs.Go("HighScore")
    sys.exit()
