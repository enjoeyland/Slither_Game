from utils import utility, listener
from utils.listener import Request
from utils.setting import SKIN_DEFAULT, RIGHT, SCREEN_MID, GREEN, POS_X, POS_Y, ON_TICK


class Snake(listener.ListenerHandler):
	def __init__(self, pygameEventDistributor, snakeID, speed, thick, skin, skinNum = SKIN_DEFAULT, firstHeadDirection = RIGHT, headPos = SCREEN_MID, color = GREEN, length = 1,):
		listener.ListenerHandler.__init__(self)

		self.pygameEventDistributor = pygameEventDistributor
		self.pygameEventDistributor.listen(Request("Snake", self.tickNotify, addtionalTarget = ON_TICK))

		self.snakeID = snakeID
		self.color = color
		self.speed = speed
		self.thick = thick
		self.length = length
		self.snakeList = [[headPos[POS_X], headPos[POS_Y], firstHeadDirection]]

		#img
		self.snakeSkin = skin.getSkin(skinNum)
		self.headImg = utility.resizeImage(self.snakeSkin["head"],(self.thick, self.thick))
		self.bodyImg = utility.resizeImage(self.snakeSkin["body"], (self.thick, self.thick))
		self.tailImg = utility.resizeImage(self.snakeSkin["tail"], (self.thick, self.thick))
		self.firstImg = utility.resizeImage(self.snakeSkin["first"], (self.thick, self.thick))

		self.attributeChanged = False

	def isAttributeChanged(self):
		return self.attributeChanged

	def tickNotify(self,**kwargs):
		if self.isAttributeChanged():
			self._notify()
			self.attributeChanged = False

	def getAttributes(self):
		snakeState = {}
		snakeState["snakeID"] = self.snakeID
		snakeState["color"] = self.color
		snakeState["speed"] = self.speed
		snakeState["thick"] = self.thick
		snakeState["length"] = self.length
		snakeState["snakeList"] = self.snakeList
		return snakeState

	def setAttributes(self, **kwargs):
		self.color = kwargs["color"] if kwargs["color"] else self.color
		self.speed = kwargs["speed"] if kwargs["speed"] else self.speed
		self.thick = kwargs["thick"] if kwargs["thick"] else self.thick
		self.length = kwargs["length"] if kwargs["length"] else self.length
		self.snakeList = kwargs["snakeList"] if kwargs["snakeList"] else self.snakeList
		self.attributeChanged = True


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
		self.attributeChanged = True


	def getSpeed(self):
		return self.speed

	def setSpeed(self, speed):
		self.speed = speed
		self.attributeChanged = True

	def addSpeed(self, speed):
		"""pixel per second"""
		self.speed += speed
		self.attributeChanged = True

	def getThick(self):
		return self.thick

	def setThick(self, thick):
		self.thick = thick
		self.attributeChanged = True

	def getSnakeList(self):
		return  self.snakeList

	def setSnakeList(self, snakeList):
		self.snakeList = snakeList
		self.attributeChanged = True
