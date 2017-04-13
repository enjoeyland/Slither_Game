import pygame
import threading
import time
from setting import *

class Event():
	pass

class KeyboardEventHandler(Event):
	def __init__(self):
		self.listenerBuffer = {}
		self.listenDic = {}


	def onKey(self, keyType, func):
		self.listenerBuffer[keyType] = func
		# self.buffer.append((keyType, func))

	def listen(self):
		tempDic = {}
		for key in set(self.listenDic.keys() + self.listenerBuffer.keys()):
			try:
				tempDic.setdefault(key,[]).append(self.listenDic[key])
			except KeyError:
				pass
			try:
				tempDic.setdefault(key,[]).append(self.listenerBuffer[key])
			except KeyError:
				pass
		self.listenDic = tempDic
		self.listenerBuffer = {}

	def endListen(self, keyType):
		self.listenDic.pop(keyType)

	def process(self, keyEvent):
		for keyType in self.listenDic.keys():
			if keyEvent.type == keyType:
				for func in self.listenDic[keyType]:
					func()

class snakeEventHandler(Event, threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.wallListenerBuffer = {}
		self.wallListenDic = {}
		self.__suspend = False
		self.__exit = False

	def crashWall(self, snake, func):
		thick = snake.getThick()
		snakeList = snake.getSnakeList()
		snakeHead = snakeList[SNAKE_HEAD]
		if  snakeHead[POS_X] > SCREEN_WIDTH - thick or SNAKE_HEAD[POS_X] < 0 \
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

	def run(self):
		while True:
			### Suspend ###
			while self.__suspend:
				time.sleep(0.5)
			### Process ###
			# self.crashWall(snake, func)
			### Exit ###
			if self.__exit:
				break
	def threadSuspend(self):
		self.__suspend = True

	def threadResume(self):
		self.__suspend = False

	def threadExit(self):
		self.__exit = True

	def onCrashWall(self, snake, func):
		self.wallListenerBuffer[snake] = func

		tempDic = {}
		for key in set(self.wallListenDic.keys() + self.wallListenerBuffer.keys()):
			try:
				tempDic.setdefault(key,[]).append(self.wallListenDic[key])
			except KeyError:
				pass
			try:
				tempDic.setdefault(key,[]).append(self.wallListenerBuffer[key])
			except KeyError:
				pass
		self.wallListenDic = tempDic
		self.wallListenerBuffer = {}
		self.crashWallThreadRun(snake, func)



class IOEventHandler(Event, threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__suspend = False
		self.__exit = False
		self.keh = KeyboardEventHandler()

	def run(self):
		while True:
			### Suspend ###
			while self.__suspend:
				time.sleep(0.5)
			### Process ###
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type == pygame.KEYDOWN:
					self.keh.process(event)

			### Exit ###
			if self.__exit:
				break



	def threadSuspend(self):
		self.__suspend = True

	def threadResume(self):
		self.__suspend = False

	def threadExit(self):
		self.__exit = True