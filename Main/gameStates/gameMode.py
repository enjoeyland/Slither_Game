import pygame


class GameMode(object):
    def __init__(self, screen):
        self.screen = screen

    def setGameSessionToFalse(self):
        self.gameSession = False

    def setGameRunningToFalse(self):
        self.isGameRunning = False

    def pause(self):
        if not self.isPause:
            self.isGameRunning = False
            self.isPause = True
        else:
            self.isGameRunning = True
            self.isPause = False

    def clickReplayButton(self):
        self.gameReplay = True

    def clickQuitButton(self):
        pygame.quit()
        quit()

    def gameLoop(self):
        raise NotImplementedError( "Should have implemented update %s" % self )
