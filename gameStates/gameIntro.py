from gameStates import gameMode
from utils.setting import PLAYER1_HIGH_SCORE


class GameIntro(gameMode.GameMode, object):
    def __init__(self, screen):
        super().__init__(screen)

    def gameLoop(self):
        # need to change
        return PLAYER1_HIGH_SCORE