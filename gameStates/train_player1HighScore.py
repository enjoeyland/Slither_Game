import os

import numpy
import pygame
import json

import sys
from PIL import Image
from assembler.train_assemblerFactory import TrainAssemblerFactory
from gameStates.train_gameMode import TrainGameMode
from train import train_utility
from utils.listener import Request
from utils.setting import PLAYER1_HIGH_SCORE, EXIT, CRASH_WALL, \
    CRASH_ITSELF, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT, FRAMES_PER_SECOND, SCREEN_BACKGROUND


class TrainPlayer1HighScore(TrainGameMode, object):
    def __init__(self, screen, sock, appleImg):
        super().__init__(PLAYER1_HIGH_SCORE, screen, sock)
        self.appleImg = appleImg

    def process(self):
        self.isGameRunning = True
        self.gameSession = True
        self.gameReplay = False
        self.isPause = False

        lastScore = 0
        if os.path.split(os.path.abspath(sys.argv[0]))[1] == "eval.py":
            # framesPerSecond = FRAMES_PER_SECOND
            framesPerSecond = 0

        else:
            framesPerSecond = 0



        ###Game Setting Start###
        # Create Group
        # groupItem = pygame.sprite.Group()
        groupWall = pygame.sprite.Group()
        groupText = pygame.sprite.Group()
        allSprites = pygame.sprite.Group()

        # Get All Object
        mAssembler = TrainAssemblerFactory().getAssembler(self.gameState, self.screen, self.appleImg)

        groupItem = mAssembler.getGroupItem()

        mPygameEventDistributor = mAssembler.getPygameEventDistributor()
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
        mLevelHandler.update(mScore.getScore())

        mPygameEventDistributor.listen(Request("Player1HighScore", self._quit, addtionalTarget = pygame.QUIT))
        mPygameEventDistributor.listen(Request("Player1HighScore", self._setGameRunningToFalse, addtionalTarget = CRASH_WALL))
        mPygameEventDistributor.listen(Request("Player1HighScore", self._setGameRunningToFalse, addtionalTarget = CRASH_ITSELF))

        ###Game Setting Over###
        self.screen.fill(WHITE)
        img_str = pygame.image.tostring(self.screen, "RGBA")
        img = Image.frombytes('RGBA', (SCREEN_WIDTH,SCREEN_HEIGHT), img_str)
        img = img.convert("L")
        img = numpy.array(img) / 255.0
        img = img.tolist()
        self.sock.send(json.dumps({"image":img}))

        while self.gameSession:
            while self.isGameRunning:
                # machine action
                action = train_utility.renderEnv2TrainerMsg(self.sock.receive())
                train_utility.actionExecute(action + 1)



                mPygameEventDistributor.distribute()
                mSnakeAction.tickMove()
                mLevelHandler.update(mScore.getScore())
                if (mScore.getScore() - lastScore)/100 > 0:
                    reward = 1
                    lastScore = mScore.getScore()
                else:
                    reward = 0


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
                img = img.convert("L")
                img = numpy.array(img) / 255.0
                img = img.tolist()
                # img.save("data/images/screen_shot.png")
                # print("img saved")

                self.screen.fill(SCREEN_BACKGROUND)
                mSnakeDisplayHandler.draw(self.screen)
                allSprites.draw(self.screen)



                self.sock.send(json.dumps({"image" : img, "reward" : reward, "done": not self.isGameRunning, "info" : mLevelHandler.getLevel(mScore.getScore())}))

                pygame.time.Clock().tick(framesPerSecond)

            ### Out of Game Running Loop ###
            if b'restart' == self.sock.receive():
                self._clickReplayButton()
                break
            raise RuntimeError("error")

        if self.gameReplay:
            return PLAYER1_HIGH_SCORE
        else:
            return EXIT

