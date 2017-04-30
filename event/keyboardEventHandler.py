class KeyboardEventHandler(object):
	def __init__(self, onKeyListenerHandler):
		self.groupListenedDic = {}
		self.onKeyListenerHandler = onKeyListenerHandler

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