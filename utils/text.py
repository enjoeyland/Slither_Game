import pygame
from utils.setting import DEFAULT_FONT_SIZE, CONTINUANCE, POS_X, POS_Y, BLACK, TOP_LEFT, TOP_MIDDLE, TOP_RIGHT, \
	CENTER_LEFT, CENTER_MIDDLE, CENTER_RIGHT, BOTTOM_LEFT, BOTTOM_MIDDLE, BOTTOM_RIGHT, ANTI_ALIAS


class Text(pygame.sprite.Sprite):
	def __init__(self, fontType, fontSize = DEFAULT_FONT_SIZE, color = BLACK, text = "", lifeTimer = CONTINUANCE, textIndex = 0, location = (0,0)):
		pygame.sprite.Sprite.__init__(self)
		pygame.font.init()

		self.textIndex = textIndex
		self.text = text
		self.color = color
		self.fontType = fontType

		self.fontSize = fontSize
		self.lifeTimer = lifeTimer
		self.alignment = TOP_LEFT 
		self.buildImage()
		# self.position = vector.vector2d(0,0) #<-
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
		self.color = color
		self.fontType = fontType

		self.fontSize = fontSize
		self.buildImage()



	def setText(self, text):
		self.text = text
		self.buildImage()


	def getText(self):
		return self.text



	def setColor(self, color):
		self.color = color



	def getColor(self):
		return self.color



	def getPosition(self):
		"""This method returns the sprite's position"""
		return [self.position[POS_X], self.position[POS_Y]]



	def setPosition(self, position):
		"""This method sets the sprite's position"""
		self.position = position



	def mouseOver(self):
		mousePosition = list(pygame.mouse.get_pos())
		if ( mousePosition[0] > self.rect.left ) and ( mousePosition[0] < self.rect.right ) and ( mousePosition[1] > self.rect.top ) and ( mousePosition[1] < self.rect.bottom ):
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
		newObject = Text(self.fontType, self.fontSize, self.color, self.text, self.lifeTimer)
		newObject.setAlign(self.alignment)

		return newObject

	def buildImage(self):
		self.fontObject = pygame.font.SysFont(self.fontType, self.fontSize)
		self.image = self.fontObject.render(str(self.text), ANTI_ALIAS, self.color)
		self.rect = self.image.get_rect()

class TextSurface:
	def __init__(self, fontType, fontSize, color, text):
		fontObject = pygame.font.SysFont(fontType, fontSize)
		self.image = fontObject.render(str(text), ANTI_ALIAS, color)