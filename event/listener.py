import pygame
import event

class ListenerHandler(object):
	def __init__(self):
		self._listenerList = []

	def listen(self, listenerName, func, group = None, groupNotifyFunc = None):
		self._listenerList.append({"keyType" : listenerName, "func" : func,
									"group" : group, "groupNotifyFunc" : groupNotifyFunc})

	def endListen(self, **kwargs):
		for key, value in kwargs.items():
			for listener in self._listenerList:
				if listener[key] == value:
					self._listenerList.remove(listener)
		else:
			print("No listener matched")

	@property
	def listenerList(self):
		return self._listenerList

# class OnKeyListenerHandler(ListenerHandler):
# 	pass
#
# class OnTickListenerHandler(ListenerHandler):
# 	pass

