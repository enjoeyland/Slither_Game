import pygame

class EventCreator(object):
	def createEvent(self, type, *args, **kwargs):
		customEvent = pygame.event.Event(type, *args, **kwargs)
		pygame.event.post(customEvent)


