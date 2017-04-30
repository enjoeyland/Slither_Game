import pygame

from ui.text import Text
from utils.setting import WHITE, SCREEN_MID, POS_X, POS_Y, CENTER_MIDDLE


class PopUp(pygame.sprite.Sprite):
	def __init__(self, backgroundColor = WHITE, pageSize = (500,300), transparent = 128,buildImageAutomatic =True, *args, **kwargs):
		pygame.sprite.Sprite.__init__(self)
		self.backgroundColor = (backgroundColor[0], backgroundColor[1], backgroundColor[2], transparent)
		self.pageSize = pageSize
		self.popUpPageBasePoint = [SCREEN_MID[POS_X] - (self.pageSize[POS_X] / 2),
								   SCREEN_MID[POS_Y] - (self.pageSize[POS_Y] / 2)]
		if buildImageAutomatic == True:
			self.buildImage( *args, **kwargs)

	def buildImage(self, *args, **kwargs):
		self.popUpPage = pygame.Surface(self.pageSize, pygame.SRCALPHA)
		# self.popUpPage.set_alpha(128)
		self.popUpPage.fill(self.backgroundColor)
		self.drawAdditionalContent(*args, **kwargs)
		self.image = self.popUpPage
		self.rect = self.image.get_rect()
		self.rect.topleft = self.popUpPageBasePoint

	def drawAdditionalContent(self, *args, **kwargs):
		pass

	# def drawText(self, text):
	# 	return Text(text = text, fontSize= 50, location= SCREEN_MID, alignment= CENTER_MIDDLE)

class PausePage(PopUp):
	def __init__(self, pageSize= (500,300)):
		PopUp.__init__(self, pageSize= pageSize)

	def drawAdditionalContent(self):
		textSprite = Text(text = "Pause", fontSize= 50, location= (self.pageSize[POS_X]/2, self.pageSize[POS_Y]/2), alignment= CENTER_MIDDLE)
		textSprite.update()
		self.popUpPage.blit(textSprite.image, textSprite.rect)