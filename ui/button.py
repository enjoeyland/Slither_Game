import pygame

from ui.text import Text
from utils.setting import DEFAULT_FONT_TYPE, DEFAULT_FONT_SIZE, CONTINUANCE, GREEN, WHITE, TOP_LEFT, CENTER_MIDDLE, \
	POS_X, POS_Y, DARK_GREEN, BOTTOM_RIGHT, BOTTOM_MIDDLE, BOTTOM_LEFT, CENTER_RIGHT, CENTER_LEFT, TOP_MIDDLE, TOP_RIGHT


class Button(Text):
	def __init__(self,func, fontType = DEFAULT_FONT_TYPE, fontSize = DEFAULT_FONT_SIZE, color = WHITE, text = "", lifeTimer = CONTINUANCE, textIndex = 0, location = (0,0), alignment = TOP_LEFT, backgroundColor = GREEN, buttonSize = None, hoverColor = DARK_GREEN, basePoint = (0,0)):
		self.buttonSize = buttonSize
		self.backgroundColor = backgroundColor
		self.location = (self.buttonSize[POS_X] / 2, self.buttonSize[POS_Y] / 2)
		self.buttonBasePoint = location
		self.effect = func
		self.hoverColor = hoverColor
		self.buttonAlignment = alignment
		self.basePint = basePoint
		Text.__init__(self, fontType, fontSize, color, text, lifeTimer, textIndex, location= self.location, alignment = CENTER_MIDDLE, basePoint= self.basePint)
		self.buildButtonImage(self.backgroundColor)

	def buildButtonImage(self, color):
		self.buttonSurface = pygame.Surface(self.buttonSize)
		self.buttonSurface.fill(color)
		self.update()
		self.buttonSurface.blit(self.image, self.rect)
		self.image = self.buttonSurface
		self.rect = self.image.get_rect()
		self.buttonUpdate()

	def buttonUpdate(self):
		if self.buttonAlignment == TOP_LEFT:
			self.rect.topleft = self.buttonBasePoint

		elif self.buttonAlignment == TOP_MIDDLE:
			self.rect.midtop = self.buttonBasePoint

		elif self.buttonAlignment == TOP_RIGHT:
			self.rect.topright = self.buttonBasePoint

		elif self.buttonAlignment == CENTER_LEFT:
			self.rect.midleft = self.buttonBasePoint

		elif self.buttonAlignment == CENTER_MIDDLE:
			self.rect.center = self.buttonBasePoint

		elif self.buttonAlignment == CENTER_RIGHT:
			self.rect.midright = self.buttonBasePoint

		elif self.buttonAlignment == BOTTOM_LEFT:
			self.rect.bottomleft = self.buttonBasePoint

		elif self.buttonAlignment == BOTTOM_MIDDLE:
			self.rect.midbottom = self.buttonBasePoint

		elif self.buttonAlignment == BOTTOM_RIGHT:
			self.rect.bottomright = self.buttonBasePoint

	def setText(self, text):
		self.text = text
		self.buildImage(self.textColor)
		self.buildButtonImage(self.backgroundColor)


	def setFont(self, fontSize, color, fontType):
		self.textColor = color
		self.fontType = fontType
		self.fontSize = fontSize
		self.buildImage(self.textColor)
		self.buildButtonImage(self.backgroundColor)

	def click(self):
		if self.isClicked():
			self.effect()

	def hover(self):
		if self.isMouseOver():
			self.buildImage(self.textColor)
			self.buildButtonImage(self.hoverColor)
		else:
			self.buildImage(self.textColor)
			self.buildButtonImage(self.backgroundColor)

	def listen(self, onTickListenerHandler):
		onTickListenerHandler.listen("button_%s_click"% self, self.click, group = "button_%s"% self)
		onTickListenerHandler.listen("button_%s_hover"% self, self.hover, group = "button_%s"% self)

	def endListen(self, onTickListenerHandler):
		onTickListenerHandler.endListen(group = "button_%s"% self)