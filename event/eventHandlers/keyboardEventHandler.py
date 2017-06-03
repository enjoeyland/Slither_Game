import pygame

from utils import listener


class KeyboardEventHandler(listener.ListenerHandler, object):
	def __init__(self, pygameEventDistributor):
		listener.ListenerHandler.__init__(self)
		self.pygameEventDistributor = pygameEventDistributor

		self.request = listener.Request("KeyboardEventHandler", self.process, description= "handle keyboard event")
		self.request.setAddtionalTarget(pygame.KEYDOWN)
		self.pygameEventDistributor.listen(self.request)

	def process(self, keyEvent):
		for listenerItem in self.listenerList:
			if keyEvent.key == listenerItem.getAddtionalTarget():
				listenerItem.notify()
