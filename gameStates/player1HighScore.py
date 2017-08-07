import pygame

from assembler import assembler
from gameStates import gameMode
from utils import utility
from utils.listener import Request
from utils.setting import PLAY_INFINITELY, SCREEN_BACKGROUND, FRAMES_PER_SECOND, PLAYER1_HIGH_SCORE, EXIT, CRASH_WALL, \
    CRASH_ITSELF


class Player1HighScore(gameMode.GameMode, object):
    def __init__(self, screen):
        super().__init__(screen)

    def gameLoop(self):
        self.isGameRunning = True
        self.gameSession = True
        self.gameReplay = False
        self.isPause = False

        # Load Image

        # Load Sound
        soundBGM = utility.loadSound("BGM")
        soundBGM.set_volume(0.3)

        # Create Group
        # groupItem = pygame.sprite.Group()
        groupWall = pygame.sprite.Group()
        groupText = pygame.sprite.Group()
        groupPopUp = pygame.sprite.Group()
        allSprites = pygame.sprite.Group()

        # Get All Object
        mAssembler = assembler.Assembler(self.screen)

        groupItem = mAssembler.getGroupItem()

        mPygameEventDistributor = mAssembler.getPygameEventDistributor()
        mScoreDisplayHandler = mAssembler.getScoreDisplayHandler()
        mScore = mAssembler.getScore()
        mLevelHandler = mAssembler.getLevelHandler()
        mKeyboardEventHandler = mAssembler.getKeyboardEventHandler()
        mTickEventHandler = mAssembler.getTickEventHandler()
        mSnakeEventCreator = mAssembler.getSnakeEventCreator()
        player = mAssembler.getPlayer()
        itemAppleSpawner = mAssembler.getItemAppleSpawner()
        mSnakeDisplayHandler = mAssembler.getSnakeDisplayHandler()
        mSnakeAction = mAssembler.getSnakeAction()
        mPausePage = mAssembler.getPausePage()
        mScoreSavor = mAssembler.getScoreSavor()
        mScoreTable = mAssembler.getScoreTable()

        # Base Setting
        groupText.add(mScoreDisplayHandler.draw())
        mLevelHandler.update(mScore.getScore())

        mKeyboardEventHandler.listen(Request("Player1HighScore", self.pause, addtionalTarget = pygame.K_p))
        mPygameEventDistributor.listen(Request("Player1HighScore", self.quit, addtionalTarget = pygame.QUIT))
        mPygameEventDistributor.listen(Request("Player1HighScore", self.setGameRunningToFalse, addtionalTarget = CRASH_WALL))
        mPygameEventDistributor.listen(Request("Player1HighScore", self.setGameRunningToFalse, addtionalTarget = CRASH_ITSELF))


        # menuButton = {"name" : "menu", "listener" : mTickEventHandler, "func": self.setButtonSprite}
        replayButton = {"name" : "replay", "listener" : mTickEventHandler, "func": self.clickReplayButton}
        quitButton = {"name" : "quit", "listener" : mTickEventHandler, "func" : self.clickQuitButton}

        while self.gameSession:
            utility.playSound(soundBGM, loops= PLAY_INFINITELY)

            while self.isGameRunning:
                #wait for machine input (at machine learning)
                mPygameEventDistributor.distribute()
                mSnakeAction.tickMove()
                mLevelHandler.update(mScore.getScore())

                # Drop Item
                itemAppleSpawner.dropItem()
                groupApple = itemAppleSpawner.getItemGroup()

                # Group Update
                try:
                    groupItem.add(groupApple.sprites())
                    allSprites.add(groupItem.sprites(), groupWall.sprites(), groupText.sprites())
                except:
                    pass

                # Build Screen
                self.screen.fill(SCREEN_BACKGROUND)

                mSnakeDisplayHandler.update()
                mSnakeDisplayHandler.draw(self.screen)

                allSprites.update()
                allSprites.draw(self.screen)

                pygame.display.update()
                pygame.time.Clock().tick(FRAMES_PER_SECOND)

            ### Out of Gam running loop ###
            soundBGM.fadeout(2)

            if self.isPause:
                # End Listen
                mSnakeAction.endListen()

                groupPopUp.add(mPausePage)
                allSprites.add(groupPopUp.sprites())

                groupPopUp.update()
                groupPopUp.draw(self.screen)
                pygame.display.update()

                while self.isPause:
                    mPygameEventDistributor.distribute()

                    pygame.display.update()
                    pygame.time.Clock().tick(3)

                mPausePage.kill()

                #listen
                mSnakeAction.setListener()

            else:
                self.setGameSessionToFalse()
                # End Listen
                mSnakeAction.endListen()

                mScoreSavor.saveScore(mScore.getScore())
                mScoreTable.buildImage(mScoreSavor.getTopScore(10), mScore.getScore(), replayButton)

                groupPopUp.add(mScoreTable)
                groupPopUp.draw(self.screen)
                groupPopUp.update()

                pygame.display.update()

                while not self.gameReplay:
                    mPygameEventDistributor.distribute()

                    self.screen.fill(SCREEN_BACKGROUND)
                    mSnakeDisplayHandler.draw(self.screen)
                    allSprites.draw(self.screen)

                    groupPopUp.draw(self.screen)
                    groupPopUp.update()

                    pygame.display.update()
                    pygame.time.Clock().tick(10)

                mScoreTable.kill()
        if self.gameReplay:
            return PLAYER1_HIGH_SCORE
        else:
            return EXIT

