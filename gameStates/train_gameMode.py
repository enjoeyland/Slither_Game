import pygame


class TrainGameMode(object):
    def __init__(self, gameState, screen, sock):
        self.gameState = gameState
        self.screen = screen
        self.sock = sock
        self.player = None

    def _setGameSessionToFalse(self):
        self.gameSession = False

    def _setGameRunningToFalse(self, data):
        if self.player.snake == data.snake:
            self.isGameRunning = False

    def _quit(self, **kwargs):
        pygame.quit()
        quit()

    def _clickReplayButton(self):
        self.gameReplay = True

    def process(self):
        raise NotImplementedError( "Should have implemented update %s" % self )
