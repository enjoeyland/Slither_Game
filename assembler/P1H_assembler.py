import pygame

from assembler.assembler import Assembler
from gameObject.player import  skin
from utils import  utility
from utils.setting import DEFAULT_SPEED, DEFAULT_THICK, SKIN_DEFAULT, PLAYER1_HIGH_SCORE, P1_HIGH_SCORE_LISTENING_EVENT


class P1H_assembler(Assembler):
    def __init__(self, screen):
        self.screen = screen
        self.createGroupItem()
        self.createScore()

        self.createEventDistributor(P1_HIGH_SCORE_LISTENING_EVENT)
        self.createKeyboardEventHandler()
        self.createTickEventHandler()
        self.createCrashItemEventHandler(self.screen)

        self.createPlayer(1, DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(), skinNum= SKIN_DEFAULT)

        self.createScoreDisplay()
        self.createScoreTable()

        self.createSnakeEventCreator()

        self.createPausePage()

        appleImg = utility.loadImageByPil("apple")
        soundAppleBite = utility.loadSound("Apple_Bite")
        self.createAppleItemSpawner(appleImg, appleSound = soundAppleBite)
        self.createLevelHandler(PLAYER1_HIGH_SCORE, {"apple" : self.getItemAppleSpawner()})

