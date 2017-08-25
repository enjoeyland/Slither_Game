#-*- coding: utf-8 -*-
import pygame

from gameStates import player1HighScore, gameIntro
from gameStates.player2Compete import Player2Compete
from utils import utility
from utils.setting import SCREEN_WIDTH, SCREEN_HEIGHT, FULL_SCREEN, PLAYER1_HIGH_SCORE, EXIT, INTRO, PLAYER2_COMPETE


def main():
    # pygame init
    pygame.mixer.pre_init(44100, -16, 2, 2048)
    pygame.init()
    pygame.mixer.init()

    if FULL_SCREEN:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        # screen = pygame.display.set_mode((640,480),SWSURFACE|FULLSCREEN)

    pygame.display.set_caption("Slither")
    pygame.display.set_icon(utility.loadImageByPil("apple"))

    state = INTRO
    while True:
        if state == PLAYER1_HIGH_SCORE:
            state = player1HighScore.Player1HighScore(screen).process()
        elif state == PLAYER2_COMPETE:
            state = Player2Compete(screen).process()
        elif state == INTRO:
            state = gameIntro.GameIntro(screen).process()
        elif state == EXIT:
            break

if __name__ == "__main__":
    main()
