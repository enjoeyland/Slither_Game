from assembler.assembler import Assembler
from gameObject.control import SnakeArrowControl
from gameObject.player import  skin
from utils.setting import DEFAULT_SPEED, DEFAULT_THICK, SKIN_DEFAULT, PLAYER1_HIGH_SCORE, P1_HIGH_SCORE_LISTENING_EVENT


class TrainP1H_assembler(Assembler):
    def __init__(self, screen, appleImg):
        super().__init__()
        self.screen = screen
        self.createGroupItem()
        self.createScore()

        self.createEventDistributor(P1_HIGH_SCORE_LISTENING_EVENT)
        self.createKeyboardEventHandler()
        self.createTickEventHandler()
        self.createCrashItemEventHandler(self.screen)
        self.createPlayer(1, DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(),SnakeArrowControl(), skinNum= SKIN_DEFAULT, length = 2)
        self.createSnakeEventCreator()

        self.createAppleItemSpawner(appleImg)
        self.createLevelHandler(PLAYER1_HIGH_SCORE, {"apple" : self.getItemAppleSpawner()})

