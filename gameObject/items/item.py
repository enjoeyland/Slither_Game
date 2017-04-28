import random
import pygame

from utils.setting import *

class Item(pygame.sprite.Sprite, object):
	"""This class is abstract class"""
	def __init__(self, itemGenerator, image, location, lifeTimer = CONTINUANCE):
		pygame.sprite.Sprite.__init__(self)
		self.itemGenerator = itemGenerator
		self.image = image
		self.rect = self.image.get_rect()
		self.setLocation(location)
		# self.type = form_type # "img" / "color"
		# self.form = form
		self.lifeTimer = lifeTimer

	def setLocation(self, location):
		self.rect.x = location[POS_X]
		self.rect.y = location[POS_Y]

	def effect(self, *args):
		raise NotImplementedError( "Should have implemented update %s" % self )

	def itemKill(self):
		self.kill()
		self.itemGenerator.itemKilled()

	def update(self):
		if self.lifeTimer != CONTINUANCE:
			if not self.lifeTimer:
				self.itemKill()
			self.lifeTimer -= 1

class ItemGenerator(object):
	def __init__(self, item, dropProbability):
		self.item = item
		self.dropProbability = dropProbability
		self.itemMaximumNum = 1
		self.currentItemNum = 0

		self.count = 0
		self.count2 = 0

	def generateLocation(self, method = "random", size = DEFAULT_ITEM_SIZE):
		"""method = 'random' or 'relative'  """
		if method == "random":
			posX = random.randrange(SPRITE_OFFSET[POS_X][BEGIN] + ITEM_MARGIN, SPRITE_OFFSET[POS_X][END] - ITEM_MARGIN - size)
			posY = random.randrange(SPRITE_OFFSET[POS_Y][BEGIN] + ITEM_MARGIN, SPRITE_OFFSET[POS_Y][END] - ITEM_MARGIN - size)
			return (posX, posY)

	def itemDropDecision(self):
		return random.random() <= self.dropProbability

	def getItemMaximumNum(self):
		return self.itemMaximumNum

	def setItemMaximumNum(self, num):
		self.itemMaximumNum = num

	def dropItem(self, method = "random", *args, **kwargs):
		if "size" in kwargs.keys():
			size = kwargs["size"]
		else:
			size = DEFAULT_ITEM_SIZE
		if  self.currentItemNum < self.itemMaximumNum:
			location = self.generateLocation(method, size)
			if self.itemDropDecision():
				self.currentItemNum += 1
				return self.item(self, location, *args, **kwargs)

	def itemKilled(self):
		self.currentItemNum -= 1

# apples = pygame.sprite.Group()
# items = pygame.sprite.Group()
# players = pygame.sprite.Group()
# walls = pygame.sprite.Group()
# allSprites = pygame.sprite.Group()
#
# location = (0,0)
# apple1 = item.Apple(location)
# apple2 = item.Apple(location)
# apple3 = item.Apple(location)
#
# apples.add(apple1,apple2,apple3)
# allSprites.add(apples.sprites())
# # allSprites.draw(screen)
# # allSprites.update()