import pygame

from ui.text import Text
from utils.setting import WHITE, SCREEN_MID, POS_X, POS_Y, CENTER_MIDDLE


class PopUp(object):
	def __init__(self, screen, backgroundColor = WHITE, pageSize = (500,300)):
		self.screen = screen
		self.backgroundColor = backgroundColor
		self.pageSize = pageSize
		self.popUpPageBasePoint = [SCREEN_MID[POS_X] - (self.pageSize[POS_X] / 2),
								   SCREEN_MID[POS_Y] - (self.pageSize[POS_Y] / 2)]

	def draw(self, *args, **kwargs):
		popUpPage = pygame.Surface(self.pageSize)
		popUpPage.set_alpha(128)
		popUpPage.fill(self.backgroundColor)
		self.screen.blit(popUpPage, self.popUpPageBasePoint)
		return self.drawContent(*args, **kwargs)

	def drawContent(self, *args, **kwargs):
		pass

	# def drawText(self, text):
	# 	return Text(text = text, fontSize= 50, location= SCREEN_MID, alignment= CENTER_MIDDLE)

class PausePage(PopUp):
	def __init__(self, screen, pageSize= (500,300)):
		PopUp.__init__(self, screen, pageSize= pageSize)

	def drawContent(self):
		return Text(text = "Pause", fontSize= 50, location= SCREEN_MID, alignment= CENTER_MIDDLE)