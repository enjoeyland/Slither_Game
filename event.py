class KeyboardEventHandler(Event):
	def __init__(self):
		pass
	def process(self, event, gameState):
		if event.key==pygame.K_q:
			pygame.quit()
			quit()
		if event.key==pygame.K_c:
			intro=False

class IOEventHandler(Event, threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__suspend = False
		self.__exit = False
		self.keh = KeyboardEventHandler()

	def threadRun(self):
		while True:
			### Suspend ###
			while self.__suspend:
				time.sleep(0.5)
			### Process ###
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type==pygame.KEYDOWN:
					self.keh.process(event, self.gameState)
			### Exit ###
			if self.__exit:
				break
	def threadSuspend(self): self.__suspend = True
	def threadResume(self): self.__suspend = False	
	def threadExit(self): self.__exit = True