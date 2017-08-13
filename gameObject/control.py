import pygame

from utils.listener import Request


class Control(object):
    def __init__(self):
        pass

class SnakeControl(object):
    def left(self):
        return NotImplementedError("You should implement SnakeControl(%s)" % self)
    def right(self):
        return NotImplementedError("You should implement SnakeControl(%s)" % self)
    def up(self):
        return NotImplementedError("You should implement SnakeControl(%s)" % self)
    def down(self):
        return NotImplementedError("You should implement SnakeControl(%s)" % self)


class SnakeArrowControl(SnakeControl):
    def left(self):
        return pygame.K_LEFT
    def right(self):
        return pygame.K_RIGHT
    def up(self):
        return pygame.K_UP
    def down(self):
        return pygame.K_DOWN

class SnakeWASDControl(SnakeControl):
    def left(self):
        return pygame.K_a
    def right(self):
        return pygame.K_d
    def up(self):
        return pygame.K_w
    def down(self):
        return pygame.K_s
