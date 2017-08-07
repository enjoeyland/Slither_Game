import pygame

class EventCreator(object):
	def createEvent(self, type, **kwargs):
		customEvent = pygame.event.Event(type, **kwargs)
		pygame.event.post(customEvent)

