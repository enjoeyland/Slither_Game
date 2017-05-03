import pygame
import event

class ListenerHandler(object):
	def __init__(self):
		self._listenerList = []

	def listen(self, listenerName, func, group = None, groupNotifyFunc = None, target = None, description = None):
		self._listenerList.append({"listenerName" : listenerName, "func" : func,
									"group" : group, "groupNotifyFunc" : groupNotifyFunc,
								   "target" : target, "description" : description})

	def endListen(self, **kwargs):
		for key, value in kwargs.items():
			listToRemove = []
			for listener in self._listenerList:
				if listener[key] == value:
					listToRemove.append(listener)
			self._listenerList = [i for i in self._listenerList if i not in listToRemove]
			if len(listToRemove) == 0:
				print("No listener matched")
	@property
	def listenerList(self):
		return self._listenerList

	def notify(self):
		for listenerItem in self.listenerList:
			listenerItem["func"]()

# class OnKeyListenerHandler(ListenerHandler):
# 	pass
#
# class OnTickListenerHandler(ListenerHandler):
# 	pass

