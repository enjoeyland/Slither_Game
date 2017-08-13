from utils import listener
from utils.setting import *


def appendOnTickEvent(func):
	def wrapper(*args):
		pygame.event.post(pygame.event.Event(ON_TICK))
		return func(*args)
	return wrapper

class pygameEventDistributor(listener.ListenerHandler, object):
	def __init__(self, eventListToListen):
		super().__init__()
		self.eventListToListen = eventListToListen

		pygame.event.set_allowed(None)
		pygame.event.set_allowed(self.eventListToListen)

	@appendOnTickEvent
	def _getEvent(self,eventList):
		self.__eventCache = pygame.event.get(eventList)
		# print("[EventDistributor] : " + str(self.__eventCache))
		pygame.event.clear()
		return self.__eventCache

	def distribute(self):
		"""This function need to be called once per fame"""
		for pygameEvent in self._getEvent(self.eventListToListen):
			for listenerItem in self._listenerList:
				if pygameEvent.type == listenerItem.getAddtionalTarget():
					self._notifyOne(listenerItem, data = pygameEvent)

