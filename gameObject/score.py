from utils.observer import Observer, Publisher
from utils.text import Text


class Score(Publisher):
	def __init__(self, score = 0):
		Publisher.__init__(self)
		self.score = score

	def up(self, change):
		self.score += change
		self.scoreChange()

	def down(self, change):
		self.score -= change
		self.scoreChange()

	def getScore(self):
		return self.score

	def scoreChange(self):
		self.notify()



class ScoreDisplayHandler(Observer):
	def __init__(self, scoreC):
		self.scoreC = scoreC
		self.scoreC.attach(self)

	def draw(self):
		self.scoreSprite = Text("comicsansms", text= self.getText(self.scoreC.score))
		return self.scoreSprite

	def getText(self, score):
		return "score : %s" % score

	def observeUpdate(self):
		self.scoreSprite.setText(self.getText(self.scoreC.score))