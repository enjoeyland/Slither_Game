import pygame
# import numpy
# from PIL import Image

from assembler import assemblerFactory
from gameStates import gameMode
from utils import utility
from utils.listener import Request
from utils.setting import PLAY_INFINITELY, SCREEN_BACKGROUND, FRAMES_PER_SECOND, EXIT, CRASH_WALL, \
    CRASH_ITSELF, SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, PLAYER2_COMPETE, CRASH_OTHER_SNAKE


class Player2Compete(gameMode.GameMode, object):
    def __init__(self, screen):
        super().__init__(PLAYER2_COMPETE, screen)

    def process(self):
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
        mAssembler = assemblerFactory.AssemblerFactory().getAssembler(self.gameState, self.screen)

        groupItem = mAssembler.getGroupItem()
        itemAppleSpawner = mAssembler.getItemAppleSpawner()

        mEventDistributor = mAssembler.getEventDistributor()
        mKeyboardEventHandler = mAssembler.getKeyboardEventHandler()
        mTickEventHandler = mAssembler.getTickEventHandler()

        mPlayer = mAssembler.getPlayers()

        mScoreDisplayHandler = mAssembler.getScoreDisplayHandler()
        mScore = mAssembler.getScore()
        mLevelHandler = mAssembler.getLevelHandler()

        mPausePage = mAssembler.getPausePage()
        mScoreSavor = mAssembler.getScoreSavor()
        mScoreTable = mAssembler.getScoreTable()

        # Base Setting
        groupText.add(mScoreDisplayHandler.draw())
        mLevelHandler.update(mScore.getScore())

        mKeyboardEventHandler.listen(Request("Player1HighScore_pause", self._pause, addtionalTarget = pygame.K_p))
        mEventDistributor.listen(Request("Player1HighScore_quit", self._quit, addtionalTarget = pygame.QUIT))
        mEventDistributor.listen(Request("Player1HighScore_crashWall", self._setGameRunningToFalse, addtionalTarget = CRASH_WALL))
        mEventDistributor.listen(Request("Player1HighScore_crashOtherSnake", self._setGameRunningToFalse, addtionalTarget = CRASH_OTHER_SNAKE))


        # menuButton = {"name" : "menu", "listener" : mTickEventHandler, "func": self.setButtonSprite}
        replayButton = {"name" : "replay", "listener" : mTickEventHandler, "func": self._clickReplayButton}
        quitButton = {"name" : "quit", "listener" : mTickEventHandler, "func" : self._clickQuitButton}

        while self.gameSession:
            utility.playSound(soundBGM, loops= PLAY_INFINITELY)

            while self.isGameRunning:
                mEventDistributor.distribute()
                for player in mPlayer:
                    player.snakeAction.tickMove()
                    player.levelHandler.update(player.score.getScore())
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
                # self.screen.fill(WHITE)

                for player in mPlayer:
                    player.snakeDisplayHandler.update()
                    player.snakeDisplayHandler.draw(self.screen)

                allSprites.update()
                allSprites.draw(self.screen)



                # if count == 100:
                #     img_str = pygame.image.tostring(self.screen, "RGBA")
                #     img = Image.frombytes('RGBA', (SCREEN_WIDTH,SCREEN_HEIGHT), img_str)
                #     img = img.convert("L")
                #     img.save("data/images/screen_shot.png")
                #     print(len(list(img.getdata())))
                #     img = numpy.array(img)
                #     img = Image.fromarray(img.squeeze(), "L")
                #     img.save("data/images/screen_shot2.png")
                #     print("img saved")
                #     # print(list(img.getdata()))
                #     print(len(list(img.getdata())))

                # count +=1

                pygame.display.update()
                pygame.time.Clock().tick(FRAMES_PER_SECOND)

            ### Out of Gam running loop ###
            soundBGM.fadeout(2)

            if self.isPause:
                # End Listen
                for player in mPlayer:
                    player.snakeAction.endListen()

                groupPopUp.add(mPausePage)
                allSprites.add(groupPopUp.sprites())

                groupPopUp.update()
                groupPopUp.draw(self.screen)
                pygame.display.update()

                while self.isPause:
                    mEventDistributor.distribute()

                    pygame.display.update()
                    pygame.time.Clock().tick(3)

                mPausePage.kill()

                #listen
                for player in mPlayer:
                    player.snakeAction.setListener()

            else:
                self._setGameSessionToFalse()
                # End Listen
                for player in mPlayer:
                    player.snakeAction.endListen()

                mKeyboardEventHandler.listen(Request("Player1HighScore_replay", self._clickReplayButton, addtionalTarget = pygame.K_RETURN))

                mScoreSavor.saveScore(mScore.getScore())
                mScoreTable.buildImage(mScoreSavor.getTopScore(10), mScore.getScore(), replayButton)

                groupPopUp.add(mScoreTable)
                groupPopUp.draw(self.screen)
                groupPopUp.update()

                pygame.display.update()

                while not self.gameReplay:
                    mEventDistributor.distribute()

                    self.screen.fill(SCREEN_BACKGROUND)
                    for player in mPlayer:
                        player.snakeDisplayHandler.draw(self.screen)
                    allSprites.draw(self.screen)

                    groupPopUp.draw(self.screen)
                    groupPopUp.update()

                    pygame.display.update()
                    pygame.time.Clock().tick(10)

                mKeyboardEventHandler.endListen("Player1HighScore_replay")
                mScoreTable.kill()
        if self.gameReplay:
            return PLAYER2_COMPETE
        else:
            return EXIT

