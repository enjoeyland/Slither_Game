import pygame

from utils.setting import *


class EventCreator(object):
	def createEvent(self, type, *args, **kwargs):
		customEvent = pygame.event.Event(type, *args, **kwargs)
		pygame.event.post(customEvent)

class Event(EventCreator):
	def __init__(self, onTickListenerHandler):
		self.onTickListenerHandler = onTickListenerHandler

	def onTick(self):
		self.createEvent(ON_TICK)
		for listenerItem in self.onTickListenerHandler.listenerList:
			listenerItem["func"]()
