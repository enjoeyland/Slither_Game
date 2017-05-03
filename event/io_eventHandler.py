import pygame

from utils.setting import *


class IOEventHandler(object):
	def __init__(self,keyboardEventHandler , onTickListenerHandler, mScore, screen):
		self.keyboardEventHandler = keyboardEventHandler
		onTickListenerHandler.listen("eventHandler", self.handleEvent)
		self.pygameTickEventList = []

		self.mScore = mScore
		self.screen = screen

	def handleEvent(self):
		# while pygame.event.peek(ON_TICK):
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
					pygameEvent.item.effect(self.screen, self.mScore, pygameEvent.snake)

			elif pygameEvent.type == CRASH_ITSELF:
				pass

			elif pygameEvent.type == CRASH_OTHER_SNAKE:
				pass


	def getPygameTickEvent(self):
		return self.pygameTickEventList

class pygameEventHandler():
	def __init__(self, pygameEventListenerHandler):
		self.listerHandler = pygameEventListenerHandler
		self.listenedEventList = []

	def handleEvent(self):
		self.listenedEventList = []
		self.pygameWholeEvent = pygame.event.get()

		for pygameEvent in self.pygameWholeEvent:
			for listener in self.listerHandler.listenerList:
				if pygameEvent.type == listener["target"]:
					try:
						listener["func"](pygameEvent)
						self.listenedEventList.append(pygameEvent.type)
					except TypeError:
						try:
							listener["func"]()
							self.listenedEventList.append(pygameEvent.type)
						except Exception as e:
							print(listener["description"])
							raise e

		for listener in self.listerHandler.listenerList:
			if listener["target"] == "WholeEvent":
				listener["func"](self.pygameWholeEvent)

			elif listener["target"] == "ListenedEvent":
				listener["func"](list(set(self.listenedEventList)))
