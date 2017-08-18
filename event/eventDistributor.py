from utils import listener
from utils.setting import *


class EventDistributor(listener.ListenerHandler, object):
	def __init__(self, eventListToListen):
		super().__init__()
		self.eventListToListen = eventListToListen

	def _getEvent(self,eventList):
		NotImplemented("You should implement EventDistributor getEvent(%s)" % self)

	def distribute(self):
		NotImplemented("You should implement EventDistributor distribute(%s)" % self)



def appendOnTickEventPygame(func):
	def wrapper(*args):
		pygame.event.post(pygame.event.Event(ON_TICK))
		return func(*args)
	return wrapper

class pygameEventDistributor(EventDistributor):
	def __init__(self, eventListToListen):
		super().__init__(eventListToListen)

		pygame.event.set_allowed(None)
		pygame.event.set_allowed(self.eventListToListen)

	@appendOnTickEventPygame
	def _getEvent(self,eventList):
		self.__eventCache = pygame.event.get(eventList)
		# print("[EventDistributor] : " + str(self.__eventCache), self)
		pygame.event.clear()
		return self.__eventCache

	def distribute(self):
		"""This function need to be called once per fame"""
		for pygameEvent in self._getEvent(self.eventListToListen):
			for listenerItem in self._listenerList:
				if pygameEvent.type == listenerItem.getAddtionalTarget():
					self._notifyOne(listenerItem, data = pygameEvent)


def appendOnTickEvent(func):
	def wrapper(self, *args):
		self.queue.put(pygame.event.Event(ON_TICK))
		return func(self, *args)
	return wrapper


class EventQueueDistributor(EventDistributor):
	def __init__(self, EventQueue,  eventListToListen):
		super().__init__(eventListToListen)
		self.queue = EventQueue

		pygame.event.set_allowed(None)

	@appendOnTickEvent
	def _getEvent(self,eventList):
		self.__eventCache = self.queue.get_all()
		# print("[EventDistributor] : " + str(self.__eventCache), self)
		return self.__eventCache

	def distribute(self):
		"""This function need to be called once per fame"""
		for queueEvent in self._getEvent(self.eventListToListen):
			for listenerItem in self._listenerList:
				if queueEvent.type == listenerItem.getAddtionalTarget():
					self._notifyOne(listenerItem, data = queueEvent)





