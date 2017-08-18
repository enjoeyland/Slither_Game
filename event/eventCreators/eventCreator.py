import pygame

class EventCreator(object):
	def __init__(self, eventQueue):
		self.queue = eventQueue

	def createEvent(self, type, **kwargs):
		customEvent = pygame.event.Event(type, **kwargs)
		try:
			self.queue.post(customEvent)
		except AttributeError:
			try:
				self.queue.put(customEvent)
			except AttributeError:
				raise AttributeError