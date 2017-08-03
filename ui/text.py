import pygame
from utils.setting import DEFAULT_FONT_SIZE, CONTINUANCE, POS_X, POS_Y, BLACK, TOP_LEFT, TOP_MIDDLE, TOP_RIGHT, \
	CENTER_LEFT, CENTER_MIDDLE, CENTER_RIGHT, BOTTOM_LEFT, BOTTOM_MIDDLE, BOTTOM_RIGHT, ANTI_ALIAS, DEFAULT_FONT_TYPE, \
	WHITE


class Text(pygame.sprite.Sprite):
	def __init__(self, fontType = DEFAULT_FONT_TYPE, fontSize = DEFAULT_FONT_SIZE, color = BLACK, text = "", lifeTimer = CONTINUANCE, textIndex = 0, location = (0,0), alignment = TOP_LEFT, basePoint = (0,0)):
		super().__init__()
		pygame.font.init()

		self.textIndex = textIndex
		self.text = text
		self.textColor = color
		self.fontType = fontType

		self.fontSize = fontSize
		self.lifeTimer = lifeTimer
		self.alignment = alignment
		self.buildImage(self.textColor)
		self.location = location
		self.basePoint = basePoint

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def update(self):
		if self.lifeTimer != CONTINUANCE:
			if not self.lifeTimer:
				self.kill()

			self.lifeTimer -= 1

		if self.alignment == TOP_LEFT:
			self.rect.topleft = self.location

		elif self.alignment == TOP_MIDDLE:
			self.rect.midtop = self.location

		elif self.alignment == TOP_RIGHT:
			self.rect.topright = self.location

		elif self.alignment == CENTER_LEFT:
			self.rect.midleft = self.location

		elif self.alignment == CENTER_MIDDLE:
			self.rect.center = self.location

		elif self.alignment == CENTER_RIGHT:
			self.rect.midright = self.location

		elif self.alignment == BOTTOM_LEFT:
			self.rect.bottomleft = self.location

		elif self.alignment == BOTTOM_MIDDLE:
			self.rect.midbottom = self.location

		elif self.alignment == BOTTOM_RIGHT:
			self.rect.bottomright = self.location



	def setFont(self, fontSize, color, fontType):
		self.textColor = color
		self.fontType = fontType

		self.fontSize = fontSize
		self.buildImage(self.textColor)



	def setText(self, text):
		self.text = text
		self.buildImage(self.textColor)


	def getText(self):
		return self.text



	def setColor(self, color):
		self.textColor = color
		self.buildImage(self.textColor)


	def getColor(self):
		return self.textColor



	def getLocation(self):
		"""This method returns the sprite's location"""
		return self.location



	def setLocation(self, location):
		"""This method sets the sprite's location"""
		self.location = location

	def isClicked(self):
		click = pygame.mouse.get_pressed()
		if self.isMouseOver() and click[0] == 1:
			return True
		else:
			return False

	def isMouseOver(self):
		mousePosition = list(pygame.mouse.get_pos())
		if ( mousePosition[POS_X] > self.rect.left + self.basePoint[POS_X] ) and ( mousePosition[POS_X] < self.rect.right + self.basePoint[POS_X] )\
				and ( mousePosition[POS_Y] > self.rect.top + self.basePoint[POS_Y]) and ( mousePosition[POS_Y] < self.rect.bottom + self.basePoint[POS_Y]):
			return True
		else:
			return False

	def mouseOverDump(self):
		print ("Mouse Position: ", list(pygame.mouse.get_pos()))
		print ("[Rect Dimensions: ", "<LEFT: ", self.rect.left + self.basePoint[POS_X], ">", "<RIGHT: ", self.rect.right + self.basePoint[POS_X], ">", "<TOP: ", self.rect.top + self.basePoint[POS_Y], ">", "<BOTTOM: ", self.rect.bottom + self.basePoint[POS_Y], ">]")



	def setTimer(self, lifeTimer):
		self.lifeTimer = lifeTimer

	def setAlign(self, alignment):
		self.alignment = alignment

	def copy(self):
		newObject = Text(self.fontType, self.fontSize, self.textColor, self.text, self.lifeTimer)
		newObject.setAlign(self.alignment)

		return newObject

	def buildImage(self, color):
		self.fontObject = pygame.font.SysFont(self.fontType, self.fontSize)
		self.image = self.fontObject.render(str(self.text), ANTI_ALIAS, color)
		self.rect = self.image.get_rect()

class TextSurface:
	def __init__(self, fontType, fontSize, color, text):
		fontObject = pygame.font.SysFont(fontType, fontSize)
		self.image = fontObject.render(str(text), ANTI_ALIAS, color)
