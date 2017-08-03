import random
import pygame

from utils.setting import POS_Y, POS_X, CONTINUANCE, FRAMES_PER_SECOND, BEGIN, SPRITE_OFFSET, ITEM_MARGIN, \
	DEFAULT_ITEM_SIZE, END


class Item(pygame.sprite.Sprite):
	"""This class is abstract class"""
	def __init__(self, itemGenerator, image, location, type = None, lifeTimer = CONTINUANCE, sound = None):
		super().__init__()
		self.itemGenerator = itemGenerator
		self.type = type
		self.image = image
		self.rect = self.image.get_rect()
		self.location = location
		self.setLocation(self.location)
		self.lifeTimer = lifeTimer
		self.sound = sound

	def setLocation(self, location):
		self.rect.x = location[POS_X]
		self.rect.y = location[POS_Y]

	def getLocation(self):
		return self.location

	def getSize(self):
		return self.rect.size

	def effect(self, *args):
		raise NotImplementedError( "Should have implemented update %s" % self )

	def kill(self):
		pygame.sprite.Sprite.kill(self)
		self.itemGenerator.itemKilled()

	def update(self):
		if self.lifeTimer != CONTINUANCE:
			if self.lifeTimer <= 0:
				self.kill()
			self.lifeTimer -= 1

class ItemGenerator(object):
	def __init__(self, item, dropProbability = FRAMES_PER_SECOND, lifeTimer =  CONTINUANCE):
		self.item = item
		self.dropProbability = dropProbability / FRAMES_PER_SECOND
		self.itemMaximumNum = 1
		self.currentItemNum = 0
		self.itemLifeTimer = lifeTimer

	def setItemMaximumNum(self, num):
		self.itemMaximumNum = num

	def getItemMaximumNum(self):
		return self.itemMaximumNum

	def setDropProbability(self, probability):
		self.dropProbability = probability / FRAMES_PER_SECOND

	def getDropProbability(self):
		return self.dropProbability

	def setItemLifeTimer(self, lifeTimer):
		self.itemLifeTimer = lifeTimer

	def getItemLifeTime(self):
		return self.itemLifeTimer



	def generateLocation(self, method = "random", size = DEFAULT_ITEM_SIZE):
		"""method = 'random' or 'relative'  """
		if method == "random":
			posX = random.randrange(SPRITE_OFFSET[POS_X][BEGIN] + ITEM_MARGIN, SPRITE_OFFSET[POS_X][END] - ITEM_MARGIN - size)
			posY = random.randrange(SPRITE_OFFSET[POS_Y][BEGIN] + ITEM_MARGIN, SPRITE_OFFSET[POS_Y][END] - ITEM_MARGIN - size)
			return (posX, posY)


	def itemDropDecision(self):
		return random.random() <= self.dropProbability

	def dropItem(self, method = "random", *args, **kwargs):
		if "size" in kwargs.keys():
			size = kwargs["size"]
		else:
			size = DEFAULT_ITEM_SIZE
		if  self.currentItemNum < self.itemMaximumNum:
			location = self.generateLocation(method, size)
			if self.itemDropDecision():
				self.currentItemNum += 1
				return self.item(self, location, lifeTimer = self.itemLifeTimer,*args, **kwargs)

	def itemKilled(self):
		if self.currentItemNum > 0:
			self.currentItemNum -= 1
		else:
			print("the number of item is not positive")