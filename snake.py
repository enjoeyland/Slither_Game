class Observer():
	def observeUpdate(self):
		raise NotImplementedError( "Should have implemented update %s" % self )

class Snake():
	def __init__(self, snakeID, speed, thick, skinName = None, firstHeadDirection = RIGHT, headPos = SCREEN_MID, color = GREEN, length = 1,):
		self.snakeID = snakeID
		self.color = color
		self.speed = speed
		self.thick = thick
		self.length = length
		self.snakeList = [(headPos[posX],headPos[posY],firstHeadDirection)]
		self.setOfObserver = set()
		#img
		if skinName != None:
			skin = Skin.getSkin(skinName)
			self.headImg = skin["head"]
			self.bodyImg = skin["body"]
			self.tailImg = skin["tail"]

	# def update(self, newHeadPos):
	# 	self.snake_list.append(newHeadPos)
	# 	if len(self.snake_list) > self.length:
	# 		del self.snake_list[0]
	def addLength(self, length = 1):
		self.length += length
		# self.snakeList.append((snakeList[-1]))
		self.notify()
	def addSpeed(self, speed):
		self.speed += speed
		self.notify()
	def getState(self):
		snakeState = {}
		snakeState["snakeID"] = self.snakeID
		snakeState["color"] = self.color
		snakeState["speed"] = self.speed
		snakeState["thick"] = self.thick
		snakeState["length"] = length
		snakeState["snakeList"] = self.snakeList
		return snakeState
	def setState(self, snakeState):
		self.color = snakeState["color"]
		self.speed = snakeState["speed"]
		self.thick = snakeState["thick"]
		self.length = snakeState["length"]
		self.snakeList = snakeState["snakeList"]
	def getImg(self):
		snakeImg = {}
		snakeImg["head"] = self.headImg
		snakeImg["body"] = self.bodyImg
		snakeImg["tail"] = self.tailImg

	# def getcolor(self): return self.color
	# def getLength(self): return self.length
	# def getSpeed(self): return self.speed
	def getSnakeState(self):
		return snakeState
	def attach(self, observer):
		self.setOfObserver.add(observer)
	def dettach(self, observer):
		self.setOfObserver.remove(observer)
	def notify():
		for observer in setOfObserver:
			observer.observeUpdate()