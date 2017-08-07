import pygame


class TrainGameMode(object):
    def __init__(self, screen):
        self.screen = screen

    def setGameSessionToFalse(self):
        self.gameSession = False

    def setGameRunningToFalse(self, **kwargs):
        self.isGameRunning = False

    def quit(self, **kwargs):
        pygame.quit()
        quit()

    def clickReplayButton(self):
        self.gameReplay = True

    def process(self):
        raise NotImplementedError( "Should have implemented update %s" % self )
