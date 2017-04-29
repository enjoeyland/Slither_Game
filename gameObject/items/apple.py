import pygame

from gameObject.items import item
from utils import utility
from utils.setting import DEFAULT_ITEM_SIZE, APPLE


class Apple(item.Item):
	def __init__(self, itemGenerator, location, size = DEFAULT_ITEM_SIZE):
		self.location = location
		self.image_size = size
		self.image = utility.loadImage("apple")
		self.resizeImage()
		item.Item.__init__(self, itemGenerator, self.image, location)
		self.type = APPLE

	def resizeImage(self):
		self.image = pygame.transform.scale(self.image,(self.image_size, self.image_size))

	def effect(self, score, snake):
		point = 100
		score.up(point)
		snake.addLength()
