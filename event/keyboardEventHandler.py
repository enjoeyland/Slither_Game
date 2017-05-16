from event.listener import Request


class KeyboardEventHandler(object):
	def __init__(self, onKeyListenerHandler, pygameEventDistributor):
		self.onKeyListenerHandler = onKeyListenerHandler
		self.pygameEventDistributor = pygameEventDistributor

		self.groupListenedDic = {}

		self.request = Request("KeyboardEventHandler", self.process, description= "handle keyboard event")
		self.pygameEventDistributor.listen(self.request)

	def process(self, keyEvent):
		for listenerItem in self.onKeyListenerHandler.listenerList:
			if keyEvent.key == listenerItem["listenerName"]:
				listenerItem["func"]()
				self.groupListenedDic[listenerItem["group"]] = listenerItem["groupNotifyFunc"]
		self.groupNotify()

	def groupNotify(self):
		for group in list(self.groupListenedDic.keys()):
			if self.groupListenedDic[group]:
				self.groupListenedDic[group]()