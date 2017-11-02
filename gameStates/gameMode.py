import pygame


class GameMode(object):
    def __init__(self, gameState, screen):
        self.gameState = gameState
        self.screen = screen
        self.player = None
        self.goMenu = False

    def _setGameSessionToFalse(self):
        self.gameSession = False

    def _setGameRunningToFalse(self, data):
        # if self.player.snake == data.snake:
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

    def _clickMenuButton(self):
        self.goMenu = True

    def _clickReplayButton(self):
        self.gameReplay = True

    def _clickQuitButton(self):
        pygame.quit()
        quit()

    def process(self):
        raise NotImplementedError( "Should have implemented update %s" % self )
