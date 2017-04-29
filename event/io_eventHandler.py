import pygame

from utils.setting import *


class IOEventHandler(object):
	def __init__(self,keyboardEventHandler , onTickListenerHandler, score):
		self.keyboardEventHandler = keyboardEventHandler
		onTickListenerHandler.listen("eventHandler", self.handleEvent)
		self.pygameTickEventList = []

		self.score = score

	def handleEvent(self):
		self.pygameTickEventList = pygame.event.get()
		for pygameEvent in self.pygameTickEventList:
			if pygameEvent.type == pygame.QUIT:
				pygame.quit()
				quit()

			elif pygameEvent.type == pygame.KEYDOWN:
				self.keyboardEventHandler.process(pygameEvent)

			elif pygameEvent.type == ON_TICK:
				pass

			elif pygameEvent.type == CRASH_WALL:
				pass

			elif pygameEvent.type == CRASH_ITEM:
				if pygameEvent.item.type == APPLE:
					pygameEvent.item.effect(self.score, pygameEvent.snake)
					pygameEvent.item.itemKill()

			elif pygameEvent.type == CRASH_ITSELF:
				pass

			elif pygameEvent.type == CRASH_OTHER_SNAKE:
				pass


	def getPygameTickEvent(self):
		return self.pygameTickEventList