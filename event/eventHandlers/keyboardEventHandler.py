import pygame

from utils import listener


class KeyboardEventHandler(listener.ListenerHandler, object):
	def __init__(self, pygameEventDistributor):
		super().__init__()
		self.pygameEventDistributor = pygameEventDistributor

		self.request = listener.Request("KeyboardEventHandler", self.process, description= "handle keyboard event")
		self.request.setAddtionalTarget(pygame.KEYDOWN)
		self.pygameEventDistributor.listen(self.request)

	def process(self, data):
		for listenerItem in self._listenerList:
			if data.key == listenerItem.getAddtionalTarget():
				self._notifyOne(listenerItem)
