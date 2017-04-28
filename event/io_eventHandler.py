import pygame

class IOEventHandler(object):
	def __init__(self,keyboardEventHandler , onTickListenerHandler):
		self.keyboardEventHandler = keyboardEventHandler
		onTickListenerHandler.listen("eventHandler", self.delegateEventHandler)
		self.pygameTickEventList = []

	def delegateEventHandler(self):
		self.pygameTickEventList = pygame.event.get()
		for pygameEvent in self.pygameTickEventList:
			if pygameEvent.type == pygame.QUIT:
				pygame.quit()
				quit()
			elif pygameEvent.type == pygame.KEYDOWN:
				self.keyboardEventHandler.process(pygameEvent)

	def getPygameTickEvent(self):
		return self.pygameTickEventList