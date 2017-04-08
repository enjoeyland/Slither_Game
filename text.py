import sys
import pygame
# import utility
# import vector

# from utility import *  

X = 0
Y = 1

class Text(pygame.sprite.Sprite):
	def __init__(self, fontType, fontSize = 12, color = (0,0,0), text = "", lifeTimer = -1, textIndex = 0):
		pygame.sprite.Sprite.__init__(self)
		pygame.font.init()

		self.textIndex = textIndex
		self.text = text
		self.color = color
		self.fontType = fontType

		#if hasattr(sys, '_MEIPASS'):

		self.fontSize = fontSize
		self.lifeTimer = lifeTimer
		self.buildImage()

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def update(self):
		if not (self.lifeTimer == -1):
			if not self.lifeTimer:
				self.kill()

			self.lifeTimer -= 1

		if self.alignment == TOP_LEFT:
			self.rect.topleft = (self.position.x, self.position.y)

		elif self.alignment == TOP_MIDDLE:
			self.rect.midtop = (self.position.x, self.position.y)

		elif self.alignment == TOP_RIGHT:
			self.rect.topright = (self.position.x, self.position.y)

		elif self.alignment == CENTER_LEFT:
			self.rect.midleft = (self.position.x, self.position.y)

		elif self.alignment == CENTER_MIDDLE:
			self.rect.center = (self.position.x, self.position.y)

		elif self.alignment == CENTER_RIGHT:
			self.rect.midright = (self.position.x, self.position.y)

		elif self.alignment == BOTTOM_LEFT:
			self.rect.bottomleft = (self.position.x, self.position.y)

		elif self.alignment == BOTTOM_MIDDLE:
			self.rect.midbottom = (self.position.x, self.position.y)

		elif self.alignment == BOTTOM_RIGHT:
			self.rect.bottomright = (self.position.x, self.position.y)



	def setFont(self, fontSize, color, fontType):
		self.color = color
		self.fontType = fontType

		#if hasattr(sys, '_MEIPASS'):

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
		return [self.position.x, self.position.y]



	def setPosition(self, Position):
		"""This method sets the sprite's position"""
		self.position.x = position[X]
		self.position.y = Position[Y]



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
		newObject.setAlign(self.alignment)

		return newObject

	def buildImage(self):
		self.fontObject = pygame.font.Font(self.fontType, self.fontSize)
		self.rect = self.image.get_rect()

class TextSurface:
		#if hasattr(sys, '_MEIPASS'):

		fontObject = pygame.font.Font(fontType, fontSize)
