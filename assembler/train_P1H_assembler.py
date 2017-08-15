from assembler.assembler import Assembler
from gameObject.control import SnakeArrowControl
from gameObject.player import  skin
from gameObject.player.player import Player
from utils.setting import DEFAULT_SPEED, DEFAULT_THICK, SKIN_DEFAULT, PLAYER1_HIGH_SCORE, P1_HIGH_SCORE_LISTENING_EVENT


class TrainP1H_assembler(Assembler):
    def __init__(self, screen, appleImg):
        super().__init__()

        self.createGroupItem()
        self.createAppleItemSpawner(appleImg)

        self.createEventDistributor(P1_HIGH_SCORE_LISTENING_EVENT)
        self.createKeyboardEventHandler()
        self.createTickEventHandler()

        self.player = Player()
        self.createRelatedToSnake(DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(), SnakeArrowControl(), skinNum= SKIN_DEFAULT, length = 2)
        self.player.setSnake(self._getSnake())
        self.player.setSnakeAction(self._getSnakeAction())
        self.player.setSnakeDisplayHandler(self._getSnakeDisplayHandler())

        self.createSnakeEventCreator()
        self.player.setSnakeEventCreator(self._getSnakeEventCreator())

        self.createLevelHandler(PLAYER1_HIGH_SCORE, {"apple" : self.getItemAppleSpawner()})
        self.player.setLevelHandler(self.getLevelHandler())

        self.createScore()
        self.player.setScore(self.getScore())

        self.createCrashItemEventHandler(screen)
    def getPlayers(self):
        return [self.player]