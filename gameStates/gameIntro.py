import pygame

from event.eventDistributor import pygameEventDistributor
from event.eventHandlers import tickEventHandler
from gameStates import gameMode
from ui.button import Button
from ui.text import Text
from utils import utility
from utils.listener import Request
from utils.setting import PLAYER1_HIGH_SCORE, INTRO, PLAYER2_COMPETE, SCREEN_BACKGROUND, BOTTOM_RIGHT, BOTTOM_LEFT, \
    BLACK, TOP_MIDDLE, SCREEN_HEIGHT, SCREEN_WIDTH, GAME_INTRO_LISTENING_EVENT, SCREEN_MID, BLUE, WHITE, PLAY_INFINITELY


class GameIntro(gameMode.GameMode, object):
    def __init__(self, screen):
        super().__init__(INTRO, screen)
        self.__changedGameState = None

    def process(self):
        # Load Image
        slitherPosterImg = utility.loadImage("2017_slither_poster")
        slitherPosterImg = utility.resizeImage(slitherPosterImg,(800,600))
        slitherPosterRect = slitherPosterImg.get_rect()
        slitherPosterRect.center = SCREEN_MID

        # Load Sound
        introBMG = utility.loadSound("BGM")
        introBMG.set_volume(0.3)

        # event
        mEventDistributor = pygameEventDistributor(GAME_INTRO_LISTENING_EVENT)
        mEventDistributor.listen(Request("GameIntro_quit", self._quit, addtionalTarget = pygame.QUIT))
        mTickEventHandler = tickEventHandler.TickEventHandler(mEventDistributor)

        # button settings
        buttonSize = (150,40)
        fontSize = 30
        padding_x = 150
        padding_y = 150

        # make button
        player1Btn = Button(self.returnP1HS, text = "1 player", alignment = BOTTOM_LEFT, location=(0 + padding_x,SCREEN_HEIGHT - padding_y), buttonSize=buttonSize, fontSize=fontSize)
        player1Btn.listen(mTickEventHandler)
        player2Btn = Button(self.returnP2C, text = "2 players", alignment = BOTTOM_RIGHT, location=(SCREEN_WIDTH - padding_x, SCREEN_HEIGHT - padding_y), buttonSize=buttonSize, fontSize=fontSize)
        player2Btn.listen(mTickEventHandler)

        # make text
        title = Text(color= BLUE, text= "Slither Game by Enjoeyland",fontSize= 40,location= (SCREEN_WIDTH/2, SCREEN_HEIGHT/4),alignment= TOP_MIDDLE)

        # merge(make intro page)
        groupIntro = pygame.sprite.Group()
        groupIntro.add(player1Btn)
        groupIntro.add(player2Btn)
        groupIntro.add(title)


        utility.playSound(introBMG, loops= PLAY_INFINITELY)

        while self.__changedGameState == None:

            mEventDistributor.distribute()

            self.screen.fill(SCREEN_BACKGROUND)

            self.screen.blit(slitherPosterImg, (0, 0))

            groupIntro.update()
            groupIntro.draw(self.screen)

            pygame.display.update()
            pygame.time.Clock().tick(10)

        introBMG.fadeout(2)
        return  self.__changedGameState

        # return PLAYER2_COMPETE
    def returnP1HS(self):
        self.__changedGameState = PLAYER1_HIGH_SCORE

    def returnP2C(self):
        self.__changedGameState = PLAYER2_COMPETE