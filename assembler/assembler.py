class Assembler_NotCreatedError(Exception):
	# def __init__(self, funcName):
	def __init__(self):
		# self.funcName = funcName
	def __str__(self):
		# return "function '%s' is not created" % self.funcName
		return "function is not created"

def checkNotNone(func):
	def wrapper(*args):
		result = func(*args)
		if result is not None:
			return result
		else:
			raise Assembler_NotCreatedError()
	return 

class Assembler(object):
	pass