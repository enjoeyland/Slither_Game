import pygame
from utils.setting import DEFAULT_FONT_SIZE, CONTINUANCE, POS_X, POS_Y, BLACK, TOP_LEFT, TOP_MIDDLE, TOP_RIGHT, \
	CENTER_LEFT, CENTER_MIDDLE, CENTER_RIGHT, BOTTOM_LEFT, BOTTOM_MIDDLE, BOTTOM_RIGHT, ANTI_ALIAS, DEFAULT_FONT_TYPE, \
	WHITE


class Text(pygame.sprite.Sprite):
	def __init__(self, fontType = DEFAULT_FONT_TYPE, fontSize = DEFAULT_FONT_SIZE, color = BLACK, text = "", lifeTimer = CONTINUANCE, textIndex = 0, location = (0,0), alignment = TOP_LEFT):
		pygame.sprite.Sprite.__init__(self)
		pygame.font.init()

		self.textIndex = textIndex
		self.text = text
		self.textColor = color
		self.fontType = fontType

		self.fontSize = fontSize
		self.lifeTimer = lifeTimer
		self.alignment = alignment
		self.buildImage(self.textColor)
		self.position = location

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def update(self):
		if self.lifeTimer != CONTINUANCE:
			if not self.lifeTimer:
				self.kill()

			self.lifeTimer -= 1

		if self.alignment == TOP_LEFT:
			self.rect.topleft = (self.position[POS_X], self.position[POS_Y])

		elif self.alignment == TOP_MIDDLE:
			self.rect.midtop = (self.position[POS_X], self.position[POS_Y])

		elif self.alignment == TOP_RIGHT:
			self.rect.topright = (self.position[POS_X], self.position[POS_Y])

		elif self.alignment == CENTER_LEFT:
			self.rect.midleft = (self.position[POS_X], self.position[POS_Y])

		elif self.alignment == CENTER_MIDDLE:
			self.rect.center = (self.position[POS_X], self.position[POS_Y])

		elif self.alignment == CENTER_RIGHT:
			self.rect.midright = (self.position[POS_X], self.position[POS_Y])

		elif self.alignment == BOTTOM_LEFT:
			self.rect.bottomleft = (self.position[POS_X], self.position[POS_Y])

		elif self.alignment == BOTTOM_MIDDLE:
			self.rect.midbottom = (self.position[POS_X], self.position[POS_Y])

		elif self.alignment == BOTTOM_RIGHT:
			self.rect.bottomright = (self.position[POS_X], self.position[POS_Y])



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



	def getColor(self):
		return self.textColor



	def getPosition(self):
		"""This method returns the sprite's position"""
		return [self.position[POS_X], self.position[POS_Y]]



	def setPosition(self, position):
		"""This method sets the sprite's position"""
		self.position = position

	def isClicked(self):
		click = pygame.mouse.get_pressed()
		if self.mouseOver() and click[0] == 1:
			return True
		else:
			return False

	def mouseOver(self):
		mousePosition = list(pygame.mouse.get_pos())
		if ( mousePosition[POS_X] > self.rect.left ) and ( mousePosition[POS_X] < self.rect.right ) and ( mousePosition[POS_Y] > self.rect.top ) and ( mousePosition[POS_Y] < self.rect.bottom ):
			return True
		else:
			return False

	def mouseOverDump(self):
		print ("Mouse Position: ", list(pygame.mouse.get_pos()))
		print ("[Rect Dimensions: ", "<LEFT: ", self.rect.left, ">", "<RIGHT: ", self.rect.right, ">", "<TOP: ", self.rect.top, ">", "<BOTTOM: ", self.rect.bottom, ">]")



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

class Button(Text):
	def __init__(self, fontType = DEFAULT_FONT_TYPE, fontSize = DEFAULT_FONT_SIZE, color = BLACK, text = "", lifeTimer = CONTINUANCE, textIndex = 0, location = (0,0), alignment = CENTER_MIDDLE, backgroundColor = WHITE, buttonSize = None):
		Text.__init__(self, fontType, fontSize, color, text, lifeTimer, textIndex, location, alignment)
		self.backgroundColor = backgroundColor
		self.buttonSize = buttonSize
