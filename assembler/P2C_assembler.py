import pygame

from assembler.assembler import Assembler
from gameObject.control import SnakeArrowControl, SnakeWASDControl
from gameObject.player import  skin
from utils import  utility
from utils.setting import DEFAULT_SPEED, DEFAULT_THICK, SKIN_DEFAULT, PLAYER1_HIGH_SCORE, \
    GREEN, PINK, UP, P2_COMPETE_LISTENING_EVENT, SCREEN_MID, POS_X, SCREEN_WIDTH, POS_Y


class P2C_assembler(Assembler):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.createGroupItem()
        self.createScore()

        self.createEventDistributor(P2_COMPETE_LISTENING_EVENT)
        self.createKeyboardEventHandler()
        self.createTickEventHandler()
        self.createCrashItemEventHandler(self.screen)

        self.createPlayer(1, DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(), SnakeArrowControl(), firstHeadDirection = UP, headPos = (SCREEN_MID[POS_X] - (SCREEN_WIDTH / 4), SCREEN_MID[POS_Y]), skinNum = SKIN_DEFAULT, color = GREEN)
        self.createPlayer(2, DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(), SnakeWASDControl(), firstHeadDirection = UP, headPos = (SCREEN_MID[POS_X] + (SCREEN_WIDTH / 4), SCREEN_MID[POS_Y]), skinNum = SKIN_DEFAULT, color = PINK)

        self.createScoreDisplay()
        self.createScoreTable()

        self.createSnakeEventCreator()

        self.createPausePage()

        appleImg = utility.loadImageByPil("apple")
        soundAppleBite = utility.loadSound("Apple_Bite")
        self.createAppleItemSpawner(appleImg, appleSound = soundAppleBite)
        self.createLevelHandler(PLAYER1_HIGH_SCORE, {"apple" : self.getItemAppleSpawner()})

