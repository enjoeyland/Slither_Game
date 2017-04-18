import pygame
import threading
import listener

from setting import *

try:
	import pygame.fastevent as eventModule
except ImportError:
	import pygame.event as eventModule

class Event(object):
	def __init__(self, onTickListenerHandler):
		self.onTickListenerHandler = onTickListenerHandler
	def onTick(self):
		for listenerItem in self.onTickListenerHandler.listenerList:
			listenerItem["func"]()


class KeyboardEventHandler(object):
	def __init__(self, onKeyListenerHandler):
		self.groupListenedDic = {}
		self.onKeyListenerHandler = onKeyListenerHandler

	def process(self, keyEvent):
		for listenerItem in self.onKeyListenerHandler.listenerList:
			if keyEvent.key == listenerItem["keyType"]:
				listenerItem["func"]()
				self.groupListenedDic[listenerItem["group"]] = listenerItem["groupNotifyFunc"]
		self.groupNotify()

	def groupNotify(self):
		for group in list(self.groupListenedDic.keys()):
			if self.groupListenedDic[group]:
				self.groupListenedDic[group]()

# def eventHandler():
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			pygame.quit()
# 		elif event.type == pygame.KEYDOWN:
# 			KeyboardEventHandler().process(event)

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




class SnakeEventHandler(Event, threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.wallListenerBuffer = {}
		self.wallListenDic = {}
		self.__suspend = False
		self.__exit = False
		# pygame.event.Event(pygame.USEREVNT,  )

	def crashWall(self, snake, func):
		thick = snake.getThick()
		snakeList = snake.getSnakeList()
		snakeHead = snakeList[SNAKE_HEAD]
		if  snakeHead[POS_X] > SCREEN_WIDTH - thick or snakeHead[POS_X] < 0 \
				or snakeHead[POS_Y] > SCREEN_HEIGHT - thick or snakeHead[POS_Y] < 0:
			func()

	def crashItem(self, snake, item, func):
		thick = snake.getThick()
		snakeList = snake.getSnakeList()
		snakeHead = snakeList[SNAKE_HEAD]
		itemSize = item.size()
		itemPos = item.positon()
		if snakeHead[POS_X] > itemPos[POS_X] and snakeHead[POS_X] < itemPos[POS_X] + itemSize \
				or snakeHead[POS_X] + thick > itemPos[POS_X] and snakeHead[POS_X] + thick < itemPos[POS_X] + itemSize:
			if snakeHead[POS_Y] > itemPos[POS_Y] and snakeHead[POS_Y] < itemPos[POS_Y] + itemSize \
					or snakeHead[POS_Y] + thick > itemPos[POS_Y] and snakeHead[POS_Y] + thick < itemPos[POS_Y] + itemSize:
				item.effect()
				func()

	def crashItself(self):
		pass
	def crashOtherSnake(self):
		pass

	# def run(self):
	# 	while True:
	# 		### Suspend ###
	# 		while self.__suspend:
	# 			time.sleep(0.5)
	# 		### Process ###
	# 		# self.crashWall(snake, func)
	# 		### Exit ###
	# 		if self.__exit:
	# 			break
	# def threadSuspend(self):
	# 	self.__suspend = True
    #
	# def threadResume(self):
	# 	self.__suspend = False
    #
	# def threadExit(self):
	# 	self.__exit = True
    #
	# def onCrashWall(self, snake, func):
	# 	self.wallListenerBuffer[snake] = func
    #
	# 	tempDic = {}
	# 	for key in set(list(self.wallListenDic.keys()) + list(self.wallListenerBuffer.keys())):
	# 		try:
	# 			tempDic.setdefault(key,[]).append(self.wallListenDic[key])
	# 		except KeyError:
	# 			pass
	# 		try:
	# 			tempDic.setdefault(key,[]).append(self.wallListenerBuffer[key])
	# 		except KeyError:
	# 			pass
	# 	self.wallListenDic = tempDic
	# 	self.wallListenerBuffer = {}
	# 	self.crashWallThreadRun(snake, func)