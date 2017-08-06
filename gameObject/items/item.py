import random
import pygame

from utils import utility
from utils.setting import POS_Y, POS_X, CONTINUANCE, FRAMES_PER_SECOND, BEGIN, SPRITE_OFFSET, ITEM_MARGIN, \
	DEFAULT_ITEM_SIZE, END


class Item(pygame.sprite.Sprite):
	"""This class is abstract class"""
	def __init__(self, image, type, sound = None, size = DEFAULT_ITEM_SIZE, location=None, lifeTimer = CONTINUANCE):
		super().__init__()
		self.type = type
		self.image_size = size
		self.image = utility.resizeImage(image, self.image_size)

		self.rect = self.image.get_rect()
		self.location = location
		if location:
			self.rect.x, self.rect.y = location
		self.lifeTimer = lifeTimer
		self.sound = sound

	def setLifeTimer(self, lifeTimer):
		self.lifeTimer = lifeTimer

	def setLocation(self, location):
		self.location = location
		self.rect.x = location[POS_X]
		self.rect.y = location[POS_Y]

	def getLocation(self):
		return self.location

	def getSize(self):
		return self.rect.size

	def effect(self, *args):
		raise NotImplementedError("Should have implemented update %s" % self)

	def update(self):
		if self.lifeTimer != CONTINUANCE:
			if self.lifeTimer <= 0:
				self.kill()
			self.lifeTimer -= 1

	def clone(self):
		# return Item(self.image, self.type, self.sound, self.image_size, self.location, self.lifeTimer)
		return NotImplementedError("Should have implemented update %s" % self)


class ItemSpawner(object):
	def __init__(self, itemPrototype, dropProbability = FRAMES_PER_SECOND, lifeTimer =  CONTINUANCE):
		self.itemPrototype = itemPrototype
		self.dropProbability = dropProbability / FRAMES_PER_SECOND
		self.itemMaximumNum = 1
		self.itemLifeTimer = lifeTimer
		self.itemGroup = pygame.sprite.Group()

	def getItemGroup(self):
		return self.itemGroup

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

	def spawn(self):
		return self.itemPrototype.clone()

	def generateLocation(self, method = "random", size = DEFAULT_ITEM_SIZE):
		"""method = 'random' or 'relative'  """
		if method == "random":
			posX = random.randrange(SPRITE_OFFSET[POS_X][BEGIN] + ITEM_MARGIN, SPRITE_OFFSET[POS_X][END] - ITEM_MARGIN - size[POS_X])
			posY = random.randrange(SPRITE_OFFSET[POS_Y][BEGIN] + ITEM_MARGIN, SPRITE_OFFSET[POS_Y][END] - ITEM_MARGIN - size[POS_Y])
			return (posX, posY)

	def itemDropDecision(self):
		return random.random() <= self.dropProbability

	def dropItem(self, method = "random"):
		if  len(self.itemGroup.sprites()) < self.itemMaximumNum:
			if self.itemDropDecision():
				item = self.spawn()
				location = self.generateLocation(method, item.getSize())
				item.setLocation(location)
				item.setLifeTimer(self.itemLifeTimer)
				self.itemGroup.add(item)