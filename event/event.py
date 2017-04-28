class Event(object):
	def __init__(self, onTickListenerHandler):
		self.onTickListenerHandler = onTickListenerHandler
	def onTick(self):
		for listenerItem in self.onTickListenerHandler.listenerList:
			listenerItem["func"]()