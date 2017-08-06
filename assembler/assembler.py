class Assembler_NotCreatedError(Exception):
	def __init__(self, funcName):
		self.funcName = funcName
	def __str__(self):
		return "function '%s' is not created" % self.funcName

class Assembler(object):
	pass