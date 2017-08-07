import pygame

from PIL import Image
from assembler import assemblerFactory
from gameStates import gameMode
from utils import utility
from utils.listener import Request
from utils.setting import PLAYER1_HIGH_SCORE, EXIT, CRASH_WALL, \
    CRASH_ITSELF, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT
from utils.sockeClass import SocketServerForOneClient


class TrainPlayer1HighScore(gameMode.GameMode, object):
    def __init__(self, screen):
        super().__init__(PLAYER1_HIGH_SCORE, screen)
        self.sock = SocketServerForOneClient(('localhost',3490))


    def process(self):
        self.isGameRunning = True
        self.gameSession = True
        self.gameReplay = False
        self.isPause = False

        ###Game Setting Start###
        # Create Group
        # groupItem = pygame.sprite.Group()
        groupWall = pygame.sprite.Group()
        groupText = pygame.sprite.Group()
        allSprites = pygame.sprite.Group()

        # Get All Object
        mAssembler = assemblerFactory.AssemblerFactory().getAssembler(self.gameState, self.screen)

        groupItem = mAssembler.getGroupItem()

        mPygameEventDistributor = mAssembler.getPygameEventDistributor()
        mScoreDisplayHandler = mAssembler.getScoreDisplayHandler()
        mScore = mAssembler.getScore()
        mLevelHandler = mAssembler.getLevelHandler()
        # mKeyboardEventHandler = mAssembler.getKeyboardEventHandler()
        # mTickEventHandler = mAssembler.getTickEventHandler()
        # mSnakeEventCreator = mAssembler.getSnakeEventCreator()
        # player = mAssembler.getPlayer()
        itemAppleSpawner = mAssembler.getItemAppleSpawner()
        mSnakeDisplayHandler = mAssembler.getSnakeDisplayHandler()
        mSnakeAction = mAssembler.getSnakeAction()

        # Base Setting
        groupText.add(mScoreDisplayHandler.draw())
        mLevelHandler.update(mScore.getScore())

        mPygameEventDistributor.listen(Request("Player1HighScore", self._quit, addtionalTarget = pygame.QUIT))
        mPygameEventDistributor.listen(Request("Player1HighScore", self._setGameRunningToFalse, addtionalTarget = CRASH_WALL))
        mPygameEventDistributor.listen(Request("Player1HighScore", self._setGameRunningToFalse, addtionalTarget = CRASH_ITSELF))

        ###Game Setting Over###

        self.sock.accept()
        self.sock.send("how to play game/ex) available action")
        # available_action=["left","right","up","down"]
        available_action=[0,1,2,3]

        while self.gameSession:
            while self.isGameRunning:
                # machine action
                action = self.sock.receive()
                utility.trainActionExecute(action)


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
                self.screen.fill(WHITE)

                mSnakeDisplayHandler.update()
                mSnakeDisplayHandler.draw(self.screen)

                allSprites.update()
                allSprites.draw(self.screen)

                # self.screen = pygame.image.fromstring(pygame.image.tostring(self.screen, "RGBA"),(800,600),"RGBX")
                # image_file = image_file.convert('1') # convert image to black and white

                img_str = pygame.image.tostring(self.screen, "RGBA")
                img = Image.frombytes('RGBA', (SCREEN_WIDTH,SCREEN_HEIGHT), img_str)
                img = img.convert('1')
                img.save("data/images/screen_shot.png")
                print("img saved")

                self.sock.send("return img, reward")

            ### Out of Game Running Loop ###
            self.sock.send("game over")
            self.sock.receive()
            self._clickReplayButton()
            break

        if self.gameReplay:
            return PLAYER1_HIGH_SCORE
        else:
            return EXIT

