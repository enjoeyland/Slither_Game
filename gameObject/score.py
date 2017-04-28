class Score(object):
	def __init__(self, score = 0):
		self.score = score
	def up(self, change):
		self.score += change
	def down(self, change):
		self.score -= change

class ScoreDisplayHandler(Score, object):
	def whenEvent(self):
		pass