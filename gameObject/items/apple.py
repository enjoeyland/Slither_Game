from gameObject.items import item
from utils import utility
from utils.setting import DEFAULT_ITEM_SIZE, APPLE, CONTINUANCE


class Apple(item.Item):
	def __init__(self, image, sound = None, size = DEFAULT_ITEM_SIZE, location = None, lifeTimer = CONTINUANCE):
		super().__init__(image, APPLE, sound = sound, size = size, location = location, lifeTimer = lifeTimer, )

	def effect(self, screen, score, snake):
		point = 100
		score.up(point)
		snake.addLength()
		if self.sound:
			utility.playSound(self.sound)
		self.kill()
		self.killedEffect(screen)

	def killedEffect(self, screen):
		pass

	def clone(self):
		return Apple(self.image, sound= self.sound, size= self.image_size, location= self.location, lifeTimer= self.lifeTimer)
