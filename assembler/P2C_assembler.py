import pygame

from assembler.assembler import Assembler
from gameObject.control import SnakeArrowControl, SnakeWASDControl
from gameObject.player import  skin
from gameObject.player.player import Player
from utils import  utility
from utils.setting import DEFAULT_SPEED, DEFAULT_THICK, SKIN_DEFAULT, PLAYER1_HIGH_SCORE, \
    GREEN, PINK, UP, P2_COMPETE_LISTENING_EVENT, SCREEN_MID, POS_X, SCREEN_WIDTH, POS_Y, PLAYER2_COMPETE


class P2C_assembler(Assembler):
    def __init__(self, screen):
        super().__init__()
        # Item
        self.createGroupItem()
        appleImg = utility.loadImageByPil("apple")
        soundAppleBite = utility.loadSound("Apple_Bite")
        self.createAppleItemSpawner(appleImg, appleSound = soundAppleBite)

        # Event
        self.createEventDistributor(P2_COMPETE_LISTENING_EVENT)
        self.createKeyboardEventHandler()
        self.createTickEventHandler()

        # Player1
        self.player1 = Player()
        self.players.append(self.player1)
        self.createRelatedToSnake(DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(),
                                  SnakeArrowControl(),
                                  firstHeadDirection = UP,
                                  headPos = (SCREEN_MID[POS_X] - (SCREEN_WIDTH / 4), SCREEN_MID[POS_Y]),
                                  skinNum= SKIN_DEFAULT, color = GREEN)
        self.player1.setSnake(self._getSnake())
        self.player1.setSnakeAction(self._getSnakeAction())
        self.player1.setSnakeDisplayHandler(self._getSnakeDisplayHandler())

        self.createSnakeEventCreator()
        self.player1.setSnakeEventCreator(self._getSnakeEventCreator())

        self.createLevelHandler(PLAYER2_COMPETE, {"apple" : self.getItemAppleSpawner()})
        self.player1.setLevelHandler(self.getLevelHandler())

        self.createScore()
        self.player1.setScore(self.getScore())

        # Player2
        self.player2 = Player()
        self.players.append(self.player2)
        self.createRelatedToSnake(DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(),
                                  SnakeWASDControl(),
                                  firstHeadDirection = UP,
                                  headPos = (SCREEN_MID[POS_X] + (SCREEN_WIDTH / 4), SCREEN_MID[POS_Y]),
                                  skinNum= SKIN_DEFAULT, color = PINK)
        self.player2.setSnake(self._getSnake())
        self.player2.setSnakeAction(self._getSnakeAction())
        self.player2.setSnakeDisplayHandler(self._getSnakeDisplayHandler())

        self.createSnakeEventCreator()
        self.player2.setSnakeEventCreator(self._getSnakeEventCreator())

        self.createLevelHandler(PLAYER2_COMPETE, {"apple" : self.getItemAppleSpawner()})
        self.player2.setLevelHandler(self.getLevelHandler())

        self.createScore()
        self.player2.setScore(self.getScore())

        # set snakeEventCreator
        for player in self.players:
            player.snakeEventCreator.setOtherSnake([p.snake for p in self.players])


        # score for display
        self.createScore()
        self.createLevelHandler(PLAYER2_COMPETE, {"apple" : self.getItemAppleSpawner()})

        self.createCrashItemEventHandler(screen)

        self.createScoreDisplay()
        self.createScoreTable()

        self.createPausePage()