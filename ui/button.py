import pygame

from ui.text import Text
from utils.setting import DEFAULT_FONT_TYPE, DEFAULT_FONT_SIZE, CONTINUANCE, GREEN, WHITE, TOP_LEFT, CENTER_MIDDLE, \
	POS_X, POS_Y, DARK_GREEN, BOTTOM_RIGHT, BOTTOM_MIDDLE, BOTTOM_LEFT, CENTER_RIGHT, CENTER_LEFT, TOP_MIDDLE, TOP_RIGHT

class Button(pygame.sprite.Sprite):
	def __init__(self,func, fontType = DEFAULT_FONT_TYPE, fontSize = DEFAULT_FONT_SIZE, textColor = WHITE, text = "", buttonLifeTimer = CONTINUANCE, textIndex = 0, location = (0,0), alignment = TOP_LEFT, backgroundColor = GREEN, buttonSize = None, hoverColor = DARK_GREEN, basePoint = (0,0)):
		pygame.sprite.Sprite.__init__(self)
		self.buttonSize = buttonSize
		self.backgroundColor = backgroundColor
		self.hoverColor = hoverColor
		self.buttonLifeTimer = buttonLifeTimer

		self.basePoint = basePoint
		self.textLocation = (self.buttonSize[POS_X] / 2, self.buttonSize[POS_Y] / 2)
		self.buttonBasePoint = location

		self.effect = func
		self.alignment = alignment

		self.textSprite = Text(fontType, fontSize, textColor, text, textIndex= textIndex, location= self.textLocation, alignment = CENTER_MIDDLE, basePoint= self.basePoint)
		self.buildImage(self.backgroundColor)

	def draw(self, screen):
		screen.blit(self.image, self.rect)

	def update(self):
		if self.buttonLifeTimer != CONTINUANCE:
			if not self.buttonLifeTimer:
				self.kill()

			self.buttonLifeTimer -= 1

	def updateAlignment(self):
		if self.alignment == TOP_LEFT:
			self.rect.topleft = self.buttonBasePoint

		elif self.alignment == TOP_MIDDLE:
			self.rect.midtop = self.buttonBasePoint

		elif self.alignment == TOP_RIGHT:
			self.rect.topright = self.buttonBasePoint

		elif self.alignment == CENTER_LEFT:
			self.rect.midleft = self.buttonBasePoint

		elif self.alignment == CENTER_MIDDLE:
			self.rect.center = self.buttonBasePoint

		elif self.alignment == CENTER_RIGHT:
			self.rect.midright = self.buttonBasePoint

		elif self.alignment == BOTTOM_LEFT:
			self.rect.bottomleft = self.buttonBasePoint

		elif self.alignment == BOTTOM_MIDDLE:
			self.rect.midbottom = self.buttonBasePoint

		elif self.alignment == BOTTOM_RIGHT:
			self.rect.bottomright = self.buttonBasePoint

	def buildImage(self, color):
		self.buttonSurface = pygame.Surface(self.buttonSize)
		self.buttonSurface.fill(color)

		self.textSprite.update()
		self.buttonSurface.blit(self.textSprite.image, self.textSprite.rect)

		self.image = self.buttonSurface
		self.rect = self.image.get_rect()
		self.updateAlignment()


	def setFont(self, fontSize, color, fontType):
		self.textSprite.setFont(fontSize, color, fontType)
		self.buildImage(self.backgroundColor)

	def setText(self, text):
		self.textSprite.setText(text)
		self.buildImage(self.backgroundColor)

	def getText(self):
		return self.textSprite.text

	def setTextColor(self, color):
		self.textSprite.setColor(color)
		self.buildImage(self.backgroundColor)

	def getTextColor(self):
		return self.textSprite.getColor()

	def getTextLocation(self):
		return self.textSprite.getLocation()

	def setLocation(self, location):
		self.buttonBasePoint = location

	def setTimer(self, buttonLifeTimer):
		self.buttonLifeTimer = buttonLifeTimer

	def setAlign(self, alignment):
		self.alignment = alignment

	def copy(self):
		newObject = Button(self.effect, self.fontType, self.fontSize, self.textColor, self.textSprite.text, self.buttonLifeTimer, backgroundColor= self.backgroundColor, buttonSize= self.buttonSize, hoverColor= self.hoverColor, alignment= self.alignment)
		return newObject



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


	def click(self):
		if self.isClicked():
			self.effect()

	def hover(self):
		if self.isMouseOver():
			self.buildImage(self.hoverColor)
		else:
			self.buildImage(self.backgroundColor)


	def listen(self, TickEventHandler):
		TickEventHandler.listen("button_%s_click"% self, self.click, group = "button_%s"% self)
		TickEventHandler.listen("button_%s_hover"% self, self.hover, group = "button_%s"% self)

	def endListen(self, TickEventHandler):
		TickEventHandler.endListen(group = "button_%s"% self)
