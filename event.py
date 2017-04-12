import pygame
import threading
import time
from collections import defaultdict

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
		self.listenDic = dict(tempDic)
		self.listenerBuffer = {}

	def endListen(self, keyType):
		self.listenDic.pop(keyType)

	def process(self, keyEvent):
		for keyType in self.listenDic.keys():
			if keyEvent.type == keyType:
				for func in self.listenDic[keyType]:
					func()


class IOEventHandler(Event, threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__suspend = False
		self.__exit = False
		self.keh = KeyboardEventHandler()

	# def setGameState(self, gameState):
	# 	self.gameState = gameState

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