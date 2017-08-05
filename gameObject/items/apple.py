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
		super().__init__(itemGenerator, self.image, location, type= APPLE, lifeTimer= self.lifeTimer, sound = sound)

	def effect(self, screen, score, snake):
		point = 100
		score.up(point)
		snake.addLength()
		utility.playSound(self.sound)
		self.kill()
		self.killedEffect(screen)


	def killedEffect(self, screen):
		pass
