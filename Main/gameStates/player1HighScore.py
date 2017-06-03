import pygame

from Main import assembler
from Main.gameStates import gameMode
from utils import utility
from utils.setting import PLAY_INFINITELY, SCREEN_BACKGROUND, FRAMES_PER_SECOND, PLAYER1_HIGH_SCORE, EXIT
from utils.listener import Request


class Player1HighScore(gameMode.GameMode, object):
    def __init__(self, screen):
        gameMode.GameMode.__init__(self, screen)

    def gameLoop(self):
        self.isGameRunning = True
        self.gameSession = True
        self.gameReplay = False
        self.isPause = False

        # Load Image
        appleImg = utility.loadImage("apple")

        # Load Sound
        soundAppleBite = utility.loadSound("Apple_Bite")
        soundAppleBite.set_volume(1)
        soundBGM = utility.loadSound("BGM")
        soundBGM.set_volume(0.3)

        # Create Group
        groupApple = pygame.sprite.Group()
        groupItem = pygame.sprite.Group()
        groupWall = pygame.sprite.Group()
        groupText = pygame.sprite.Group()
        groupPopUp = pygame.sprite.Group()
        allSprites = pygame.sprite.Group()

        # Get All Object
        mAssembler = assembler.Assembler()
        mPygameEventDistributor = mAssembler.getPygameEventDistributor()
        mScoreDisplayHandler = mAssembler.getScoreDisplayHandler()
        mScore = mAssembler.getScore()
        mGameHandler = mAssembler.getGameHandler()
        mKeyboardEventHandler = mAssembler.getKeyboardEventHandler()
        mTickEventCreator = mAssembler.getTickEventCreator()
        mSnakeEventCreator = mAssembler.getSnakeEventCreator()
        player = mAssembler.getPlayer()
        itemAppleGenerator = mAssembler.getItemAppleGenerator()
        mSnakeDisplayHandler = mAssembler.getSnakeDisplayHandler()
        mSnakeStateHandler = mAssembler.getSnakeStateHandler()
        mPausePage = mAssembler.getPausePage()
        mScoreSavor = mAssembler.getScoreSavor()
        mScoreTable = mAssembler.getScoreTable()
        mTickEventHandler = mAssembler.getTickEventHandler()


        mPygameEventDistributor.start()
        groupText.add(mScoreDisplayHandler.draw())
        mGameHandler.update(mScore.getScore())

        mKeyboardEventHandler.listen(Request("Player1HighScore", self.pause, addtionalTarget= pygame.K_p))

        # menuButton = {"name" : "menu", "listener" : mTickEventHandler, "func": self.setButtonSprite}
        replayButton = {"name" : "replay", "listener" : mTickEventHandler, "func": self.clickReplayButton}
        quitButton = {"name" : "quit", "listener" : mTickEventHandler, "func" : self.clickQuitButton}

        while self.gameSession:
            utility.playSound(soundBGM, loops= PLAY_INFINITELY)

            while self.isGameRunning:

                # Make Event
                mTickEventCreator.onTick()

                mSnakeEventCreator.crashWall(player, self.setGameRunningToFalse)
                mSnakeEventCreator.crashItself(player, self.setGameRunningToFalse)
                mSnakeEventCreator.crashItem(player, groupItem)

                mGameHandler.update(mScore.getScore())

                # Drop Item
                objectApple = itemAppleGenerator.dropItem(image= appleImg, sound= soundAppleBite)
                if objectApple:
                    groupApple.add(objectApple)

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

                # Update Screen
                pygame.display.update()
                pygame.time.Clock().tick(FRAMES_PER_SECOND)

            ### Out of Gam running loop ###
            soundBGM.fadeout(2)

            if self.isPause:
                # End Listen
                mSnakeStateHandler.endListen()

                groupPopUp.add(mPausePage)
                allSprites.add(groupPopUp.sprites())

                groupPopUp.update()
                groupPopUp.draw(self.screen)
                pygame.display.update()

                while self.isPause:
                    mTickEventCreator.onTick()

                    pygame.display.update()
                    pygame.time.Clock().tick(3)

                mPausePage.kill()

                #listen
                mSnakeStateHandler.setListener()

            else:
                self.setGameSessionToFalse()
                # End Listen
                mSnakeStateHandler.endListen()

                mScoreSavor.saveScore(mScore.getScore())
                mScoreTable.buildImage(mScoreSavor.getTopScore(10), mScore.getScore(), replayButton)

                groupPopUp.add(mScoreTable)
                groupPopUp.draw(self.screen)
                groupPopUp.update()
                pygame.display.update()

                while not self.gameReplay:
                    mTickEventCreator.onTick()

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

