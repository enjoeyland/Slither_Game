from utils.observer import Publisher
from utils.setting import *

class Snake(Publisher):
	def __init__(self, snakeID, speed, thick, skin, skinNum = SKIN_DEFAULT, firstHeadDirection = RIGHT, headPos = SCREEN_MID, color = GREEN, length = 1,):
		Publisher.__init__(self)
		self.snakeID = snakeID
		self.color = color
		self.speed = speed
		self.thick = thick
		self.length = length
		self.snakeList = [(headPos[POS_X], headPos[POS_Y], firstHeadDirection)]
		self.setOfObserver = set()

		#img
		self.snakeSkin = skin.getSkin(skinNum)
		self.headImg = self.resizeImage(self.snakeSkin["head"])
		self.bodyImg = self.resizeImage(self.snakeSkin["body"])
		self.tailImg = self.resizeImage(self.snakeSkin["tail"])
		self.firstImg = self.resizeImage(self.snakeSkin["first"])

	def resizeImage(self, image):
		try:
			image = pygame.transform.scale(image,(self.thick, self.thick))
			return image
		except Exception as e:
			return  image

	def getState(self):
		snakeState = {}
		snakeState["snakeID"] = self.snakeID
		snakeState["color"] = self.color
		snakeState["speed"] = self.speed
		snakeState["thick"] = self.thick
		snakeState["length"] = self.length
		snakeState["snakeList"] = self.snakeList
		return snakeState

	def setState(self, snakeState):
		self.color = snakeState["color"]
		self.speed = snakeState["speed"]
		self.thick = snakeState["thick"]
		self.length = snakeState["length"]
		self.snakeList = snakeState["snakeList"]
		self.notify()


	def getSnakeID(self):
		return self.snakeID

	def getSkin(self):
		return self.snakeSkin

	def getColor(self):
		return self.color


	def getLength(self):
		return self.length

	def addLength(self, length = 1):
		self.length += length
		self.notify()


	def getSpeed(self):
		return self.speed

	def addSpeed(self, speed):
		"""pixel per second"""
		self.speed += speed
		self.notify()

	def getThick(self):
		return self.thick

	def setThick(self, thick):
		self.thick = thick
		self.notify()

	def getSnakeList(self):
		return  self.snakeList

	def setSnakeList(self, snakeList):
		self.snakeList = snakeList
		self.notify()
