import pygame
from setting import *

class Item(pygame.sprite.Sprite):
	def __init__(self, form, lifeTimer = CONTINUANCE, form_type = "img"):
		pygame.sprite.Sprite.__init__(self)
		self.type = form_type # "img" / "color"
		self.form = form
		self.lifeTimer = lifeTimer
	def display(self, location):
		pass
	def effect(self):
		raise NotImplementedError( "Should have implemented update %s" % self )
	def update(self):
		if not (self.lifeTimer == -1):
			if not self.lifeTimer:
				self.kill()

			self.lifeTimer -= 1


class Apple(Item):
	def __init__(self):
		# appleImg = 
		Item.__init__(self, appleImg, CONTINUANCE)

	def effect(self, score):
		point = 100
		score.up(100)
