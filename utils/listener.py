from utils import utility


# class ListenerHandler(object):
# 	def __init__(self):
# 		self._listenerList = []
#
# 	def listen(self, listenerName, func, group = None, groupNotifyFunc = None, target = None, description = None):
# 		self._listenerList.append({"listenerName" : listenerName, "func" : func,
# 									"group" : group, "groupNotifyFunc" : groupNotifyFunc,
# 								   "target" : target, "description" : description})
#
# 	def endListen(self, **kwargs):
# 		for key, value in kwargs.items():
# 			listToRemove = []
# 			for listener in self._listenerList:
# 				if listener[key] == value:
# 					listToRemove.append(listener)
# 			self._listenerList = [i for i in self._listenerList if i not in listToRemove]
# 			if len(listToRemove) == 0:
# 				print("No listener matched")
# 	@property
# 	def listenerList(self):
# 		return self._listenerList
#
# 	def notify(self):
# 		for listenerItem in self.listenerList:
# 			listenerItem["func"]()

class ListenerHandler(object):
	def __init__(self):
		self._listenerList = []

	def listen(self, request):
		self._listenerList.append(request)

	def endListen(self, listenerName):
		self._listenerList = [listener for listener in self._listenerList if listenerName != listener.getName()]

	def endGroupListen(self, groupName):
		self._listenerList = [listener for listener in self._listenerList if groupName != listener.getGroupName()]

	def _notify(self,*args, **kwargs):
		for listenerItem in self._listenerList:
			listenerItem.notify(*args,**kwargs)

	def _notifyOne(self,listener,*args, **kwargs):
		listener.notify(*args,**kwargs)



class Request(object):
	def __init__(self, listenerName, callbackFunc, description = None, addtionalTarget = None, groupName = None, groupCallbackFunc = lambda *args, **kwargs : None):
		self.name = listenerName
		self.callbackFunc = callbackFunc
		self.description = description
		self.addtionalTarget =  addtionalTarget
		self.groupName = groupName
		self.groupCallbackFunc = groupCallbackFunc

	def getName(self):
		return self.name

	def setCallbackFunc(self, callbackFunc):
		self.callbackFunc = callbackFunc

	def getCallbackFunc(self):
		return self.callbackFunc

	def setGroup(self, groupName, groupCallbackFunc):
		self.groupName = groupName
		self.groupCallbackFunc = groupCallbackFunc

	def getGroupName(self):
		return self.groupName

	def getGroupCallbackFunc(self):
		return self.groupCallbackFunc

	def setAddtionalTarget(self, addtionalTarget):
		self.addtionalTarget = addtionalTarget

	def getAddtionalTarget(self):
		return self.addtionalTarget

	def notify(self,*args, **kwargs):
		utility.executeFunction(self.callbackFunc, name = self.name, *args ,**kwargs)
		self.groupNotify(*args, **kwargs)

	def groupNotify(self,*args, **kwargs):
		utility.executeFunction(self.groupCallbackFunc, name = self.name, *args ,**kwargs)

class ListenerHandler2(object):
	def __init__(self):
		self._listenerList = []

	def listen(self, request):
		self._listenerList.append(request)

	def endListen(self, listenerName):
		self._listenerList = [listener for listener in self._listenerList if listenerName != listener.getName()]

	def endGroupListen(self, groupName):
		self._listenerList = [listener for listener in self._listenerList if groupName != listener.getGroupName()]

	def _notify(self,*args):
		for func in self._listenerList:
			utility.executeFunction(func,*args)