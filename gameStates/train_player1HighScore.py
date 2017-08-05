import pygame

from Main import assembler
from gameStates import gameMode
from utils import utility
from utils.listener import Request
from utils.setting import PLAY_INFINITELY, PLAYER1_HIGH_SCORE, EXIT, CRASH_WALL, \
    CRASH_ITSELF, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from PIL import Image


class TrainPlayer1HighScore(gameMode.GameMode, object):
    def __init__(self, screen):
        super().__init__(screen)

    def gameLoop(self):
        self.isGameRunning = True
        self.gameSession = True
        self.gameReplay = False
        self.isPause = False

        # Load Image
        appleImg = utility.loadImage("apple")

        # Create Group
        groupApple = pygame.sprite.Group()
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
        itemAppleGenerator = mAssembler.getItemAppleGenerator()
        mSnakeDisplayHandler = mAssembler.getSnakeDisplayHandler()
        mSnakeAction = mAssembler.getSnakeAction()
        mPausePage = mAssembler.getPausePage()
        mScoreSavor = mAssembler.getScoreSavor()
        mScoreTable = mAssembler.getScoreTable()

        # Base Setting
        groupText.add(mScoreDisplayHandler.draw())
        mLevelHandler.update(mScore.getScore())

        mPygameEventDistributor.listen(Request("Player1HighScore", self.quit, addtionalTarget = pygame.QUIT))
        mPygameEventDistributor.listen(Request("Player1HighScore", self.setGameRunningToFalse, addtionalTarget = CRASH_WALL))
        mPygameEventDistributor.listen(Request("Player1HighScore", self.setGameRunningToFalse, addtionalTarget = CRASH_ITSELF))

        while self.gameSession:
            while self.isGameRunning:
                #wait for machine input (at machine learning)
                mPygameEventDistributor.distribute()
                mSnakeAction.tickMove()
                mLevelHandler.update(mScore.getScore())

                # Drop Item
                objectApple = itemAppleGenerator.dropItem(image = appleImg)
                if objectApple:
                    groupApple.add(objectApple)

                # Group Update
                try:
                    groupItem.add(groupApple.sprites())
                    allSprites.add(groupItem.sprites(), groupWall.sprites(), groupText.sprites())
                except:
                    pass

                # Build Screen
                self.screen.fill(WHITE)

                mSnakeDisplayHandler.update()
                mSnakeDisplayHandler.draw(self.screen)

                allSprites.update()
                allSprites.draw(self.screen)

                # Update Screen
                # self.screen = pygame.image.fromstring(pygame.image.tostring(self.screen, "RGBA"),(800,600),"RGBX")
                # image_file = image_file.convert('1') # convert image to black and white

                img_str = pygame.image.tostring(self.screen, "RGBA")
                # print(len(pygame.image.tostring(self.screen, "RGBA")))
                img = Image.frombytes('RGBA', (SCREEN_WIDTH,SCREEN_HEIGHT), img_str)
                img.save("hi.png")
                print("img saved")


            ### Out of Gam running loop ###

        if self.gameReplay:
            return PLAYER1_HIGH_SCORE
        else:
            return EXIT

