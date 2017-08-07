import pygame


class GameMode(object):
    def __init__(self, gameState, screen):
        self.gameState = gameState
        self.screen = screen

    def _setGameSessionToFalse(self):
        self.gameSession = False

    def _setGameRunningToFalse(self, **kwargs):
        self.isGameRunning = False

    def _pause(self):
        if not self.isPause:
            self.isGameRunning = False
            self.isPause = True
        else:
            self.isGameRunning = True
            self.isPause = False

    def _quit(self, **kwargs):
        pygame.quit()
        quit()

    def _clickReplayButton(self):
        self.gameReplay = True

    def _clickQuitButton(self):
        pygame.quit()
        quit()

    def process(self):
        raise NotImplementedError( "Should have implemented update %s" % self )
