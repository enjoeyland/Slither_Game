from utils import listener
from utils.setting import *

#
# class IOEventHandler(object):
# 	def __init__(self,keyboardEventHandler , onTickListenerHandler, mScore, screen):
# 		self.keyboardEventHandler = keyboardEventHandler
# 		onTickListenerHandler.listen("eventHandler", self.handleEvent)
# 		self.pygameTickEventList = []
#
# 		self.mScore = mScore
# 		self.screen = screen
#
# 	def handleEvent(self):
# 		# while pygame.event.peek(ON_TICK):
# 		self.pygameTickEventList = pygame.event.get()
# 		for pygameEvent in self.pygameTickEventList:
# 			if pygameEvent.type == pygame.QUIT:
# 				pygame.quit()
# 				quit()
#
# 			elif pygameEvent.type == pygame.KEYDOWN:
# 				self.keyboardEventHandler.process(pygameEvent)
#
# 			elif pygameEvent.type == ON_TICK:
# 				pass
#
# 			elif pygameEvent.type == CRASH_WALL:
# 				pass
#
# 			elif pygameEvent.type == CRASH_ITEM:
# 				if pygameEvent.item.type == APPLE:
# 					#여기 있으면 않됨
# 					pygameEvent.item.effect(self.screen, self.mScore, pygameEvent.snake)
#
# 			elif pygameEvent.type == CRASH_ITSELF:
# 				pass
#
# 			elif pygameEvent.type == CRASH_OTHER_SNAKE:
# 				pass
#
#
# 	def getPygameTickEvent(self):
# 		return self.pygameTickEventList

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
					# self.listenedEventList.append(pygameEvent.type)

		# for listenerItem in self._listenerList:
		# 	if listenerItem.getAddtionalTarget() == "wholeEvent":
		# 		listenerItem.notify(data = pygameWholeEvent)
        #
		# 	elif listenerItem.getAddtionalTarget() == "listenedEvent":
		# 		listenerItem.notify(data = list(set(self.listenedEventList)))
	# def atPause(self):
	# 	eventList = [pygame.QUIT,pygame.KEYDOWN,ON_TICK]
	# 	pygame.event.wait()
	# 	if pygame.event.peek(eventList):
	# 		for pygameEvent in self._getEvent(eventList):
	# 			for listenerItem in self._listenerList:
	# 				if pygameEvent.type == listenerItem.getAddtionalTarget():
	# 					self._notifyOne(listenerItem, data = pygameEvent)

# import threading, time
from queue import Queue
# thread를 쓰지 말기
# observer pattern를 쓰는게 좋을 것 같음
# listener에게 notify해주고 listener는 queue에서 get하게 함
# import threading
# class pygameEventDistributor(threading.Thread):
# 	def __init__(self, pygameEventListenerHandler, queue):
# 		threading.Thread.__init__(self)
# 		self.listerHandler = pygameEventListenerHandler
# 		self.queue = queue
# 		self.listenedEventList = []
# 		self.__suspend = False
# 		self.__exit = False
#
# 	def run(self):
# 		while True:
# 			while self.__suspend:
# 				time.sleep(0.1)
#
# 			# process
# 			self.listenedEventList = []
# 			self.pygameWholeEvent = self.queue.get()
#
# 			for pygameEvent in self.pygameWholeEvent:
# 				for listener in self.listerHandler.listenerList:
# 					if pygameEvent.type == listener["target"]:
# 						try:
# 							listener["func"](pygameEvent)
# 							self.listenedEventList.append(pygameEvent.type)
# 						except TypeError:
# 							try:
# 								listener["func"]()
# 								self.listenedEventList.append(pygameEvent.type)
# 							except Exception as e:
# 								print(listener["description"])
# 								raise e
#
# 			for listener in self.listerHandler.listenerList:
# 				if listener["target"] == "WholeEvent":
# 					listener["func"](self.pygameWholeEvent)
#
# 				elif listener["target"] == "ListenedEvent":
# 					listener["func"](list(set(self.listenedEventList)))
#
# 			self.queue.task_done()
#
#
# 			# Exit
# 			if self.__exit:
# 				break
#
# 	def suspend(self):
# 		self.__suspend = True
#
# 	def resume(self):
# 		self.__suspend = False
#
# 	def exit(self):
# 		self.__exit = True
