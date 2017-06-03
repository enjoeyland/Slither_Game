from ui.button import Button
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
	def __init__(self, pageSize= (500,300)):
		self.pageSize = pageSize
		PopUp.__init__(self, pageSize= self.pageSize, buildImageAutomatic = False)
		self.key = "score"

	def drawAdditionalContent(self, data, thisSessionScore, appendButton = None):
		self.allSprites = []
		scoreSprites = DrawTable().draw(data, self.key ,width= self.pageSize[POS_X], highLight= thisSessionScore)
		self.allSprites.extend(scoreSprites)

		if appendButton is not None:
			self.buttonSprite = Button(appendButton["func"], buttonSize=(150,40), text= appendButton["name"], fontSize= 30, location=(0,self.pageSize[POS_Y]), alignment= BOTTOM_LEFT, basePoint = self.popUpPageBasePoint)
			self.buttonSprite.listen(appendButton["listener"])

	def getButtonSprite(self):
		return self.buttonSprite

	def update(self):
		for sprite in self.allSprites:
			sprite.update()
			self.popUpPage.blit(sprite.image, sprite.rect)
		self.buttonSprite.update()
		self.popUpPage.blit(self.buttonSprite.image, self.buttonSprite.rect)
