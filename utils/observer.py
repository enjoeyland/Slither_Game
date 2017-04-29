class Observer(object):
	def observeUpdate(self):
		raise NotImplementedError( "Should have implemented update %s" % self )

class Publisher(object):
	def __init__(self):
		self.setOfObserver = set()

	def attach(self, observer):
		self.setOfObserver.add(observer)

	def detach(self, observer):
		self.setOfObserver.remove(observer)

	def notify(self):
		for observer in self.setOfObserver:
			observer.observeUpdate()