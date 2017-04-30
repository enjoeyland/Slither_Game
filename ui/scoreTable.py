from ui.popUp import PopUp
from ui.text import Text
from utils.setting import TOP_MIDDLE, SCREEN_WIDTH, POS_X, POS_Y, RED, BLUE, BOTTOM_LEFT


class DrawTable():
	def __init__(self):
		pass
	def draw(self, data, key, basePoint = (0,0), width = SCREEN_WIDTH, highLight = None):
		textSpriteList = []
		fontSize = 20
		margin = fontSize + 10
		one = True
		for index, datum in enumerate(data):
			if datum[key] == highLight and one == True:
				textSpriteList.append(Text(color= RED,text= "%s. %s" % (index + 1, datum[key]),fontSize= 20,location= (basePoint[POS_X] + width / 2, basePoint[POS_Y] + margin * index),alignment= TOP_MIDDLE))
				one = False
			else:
				textSpriteList.append(Text(text= "%s. %s" % (index + 1, datum[key]),fontSize= 20,location= (basePoint[POS_X] + width / 2, basePoint[POS_Y] + margin * index),alignment= TOP_MIDDLE))
		return  textSpriteList


class ScoreTable(PopUp):
	def __init__(self, screen, pageSize= (500,300)):
		self.pageSize = pageSize
		PopUp.__init__(self, screen, pageSize= self.pageSize)
		self.key = "score"

	def drawContent(self, data, thisSessionScore, appendButton = None):

		result = []
		scoreSprites = DrawTable().draw(data, self.key, self.popUpPageBasePoint, self.pageSize[POS_X], thisSessionScore)
		result.extend(scoreSprites)

		if appendButton is not None:
			buttonSprite = Text(color= BLUE,text= appendButton["name"], fontSize= 30,location=(self.popUpPageBasePoint[POS_X], self.popUpPageBasePoint[POS_Y] + self.pageSize[POS_Y])  ,alignment= BOTTOM_LEFT)
			appendButton["listener"].listen(appendButton["name"]+"Button", appendButton["func"](appendButton["name"], buttonSprite))
			result.append(buttonSprite)
		return result
