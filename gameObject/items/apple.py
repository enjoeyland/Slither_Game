import pygame

from gameObject.items import item
from utils import utility
from utils.setting import DEFAULT_ITEM_SIZE, APPLE, CONTINUANCE


class Apple(item.Item):
	def __init__(self, itemGenerator, location, size = DEFAULT_ITEM_SIZE, image = None, sound = None,lifeTimer = CONTINUANCE):
		self.location = location
		self.image_size = size
		self.lifeTimer = lifeTimer
		if image is None:
			self.image = utility.loadImage("apple")
		else:
			self.image = image
		self.image = utility.resizeImage(image, (self.image_size, self.image_size))
		item.Item.__init__(self, itemGenerator, self.image, location, type= APPLE, lifeTimer= self.lifeTimer, sound = sound)

		if sound is None:
			self.sound = utility.loadSound("Apple_Bite")
		else:
			self.sound = sound

	def effect(self, screen, score, snake):
		point = 100
		score.up(point)
		snake.addLength()
		utility.playSound(self.sound)
		self.eatenEffect(screen)
		self.itemKill()

	def eatenEffect(self, screen):
		pass
