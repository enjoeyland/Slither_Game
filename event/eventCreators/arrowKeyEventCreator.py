import pygame

from event.eventCreators.eventCreator import EventCreator


class ArrowKeyEventCreator(EventCreator):
    def __init__(self, queue):
        super().__init__(queue)

    def onKeyLeft(self):
        self.createEvent(pygame.KEYDOWN, unicode = '', mod= 0, key = pygame.K_LEFT, scancode = 75)

    def onKeyRight(self):
        self.createEvent(pygame.KEYDOWN, unicode = '', mod= 0, key = pygame.K_RIGHT, scancode = 77)

    def onKeyUp(self):
        self.createEvent(pygame.KEYDOWN, unicode = '', mod= 0, key = pygame.K_UP, scancode = 72)

    def onKeyDown(self):
        self.createEvent(pygame.KEYDOWN, unicode = '', mod= 0, key = pygame.K_DOWN, scancode = 80)

