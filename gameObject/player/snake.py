from utils import utility, listener
from utils.listener import Request
from utils.setting import SKIN_DEFAULT, RIGHT, SCREEN_MID, GREEN, POS_X, POS_Y, ON_TICK


class Snake(listener.ListenerHandler):
	def __init__(self, pygameEventDistributor, speed, thick, skin, skinNum = SKIN_DEFAULT, firstHeadDirection = RIGHT, headPos = SCREEN_MID, color = GREEN, length = 1):
		super().__init__()

		# to listen
		self.pygameEventDistributor = pygameEventDistributor
		self.pygameEventDistributor.listen(Request("Snake", self.tickNotify, addtionalTarget = ON_TICK))

		# Snake Attributes
		self.color = color
		self.speed = speed
		self.thick = thick
		self.length = length
		self.snakeList = [[headPos[POS_X], headPos[POS_Y], firstHeadDirection]]

		# Snake Skin
		self.snakeSkin = skin.getSkin(skinNum)
		for key in self.snakeSkin:
			self.snakeSkin[key] = utility.resizeImage(self.snakeSkin[key], self.thick)

		self.attributeChanged = False

	def isAttributeChanged(self):
		return self.attributeChanged

	def tickNotify(self,**kwargs):
		if self.isAttributeChanged():
			self._notify()
			self.attributeChanged = False

	def getAttributes(self):
		snakeState = {}
		snakeState["color"] = self.color
		snakeState["speed"] = self.speed
		snakeState["thick"] = self.thick
		snakeState["length"] = self.length
		snakeState["snakeList"] = self.snakeList
		return snakeState

	def setAttributes(self, color = None, speed = None,thick = None, length = None, snakeList = None):
		self.color = color if color else self.color
		self.speed = speed if speed else self.speed
		self.thick = thick if thick else self.thick
		self.length = length if length else self.length
		self.snakeList = snakeList if snakeList else self.snakeList
		self.attributeChanged = True



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
		print("[Snake] : " + str(snakeList))
		self.attributeChanged = True
