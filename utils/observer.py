class Observer(object):
	def observeUpdate(self):
		raise NotImplementedError( "Should have implemented update %s" % self )