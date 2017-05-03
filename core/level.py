from utils.setting import MAX_LEVEL, LEVEL


class Level():
	def __init__(self, levelSetting = LEVEL):
		self.levelSetting = levelSetting

	def getLevel(self, score, gameName = None):
		for level in range(LEVEL[gameName][MAX_LEVEL]["level"]):
			if LEVEL[gameName][level]["score"] <= score < LEVEL[gameName][level + 1]["score"]:
				return LEVEL[gameName][level]["level"]
		else:
			if LEVEL[gameName][MAX_LEVEL]["score"] <= score:
				return LEVEL[gameName][MAX_LEVEL]["level"]

	def getLevelSetting(self):
		return self.levelSetting

class GameHandler():
	def __init__(self, mSnake, mItemGenerators, levelClass = Level, gameName = None):
		self.mLevel = levelClass()
		self.gameName = gameName
		self.mSnake = mSnake
		self.mItemGenerators = mItemGenerators

		self.lastLevel = 0

	def update(self, score):
		level = self.setLevel(score)
		self.checkLevelChange(level)

	def checkLevelChange(self, level):
		if self.lastLevel != level:
			print("Level %s" % level)

		self.lastLevel = level

	def setLevel(self, score):
		level = self.mLevel.getLevel(score, self.gameName)
		levelSetting = self.mLevel.getLevelSetting()
		setting = levelSetting[self.gameName][level]["setting"]

		self.mSnake.setSpeed(setting["snake"]["speed"])
		self.mSnake.setThick(setting["snake"]["thick"])

		for itemGenerator in self.mItemGenerators.keys():
			self.mItemGenerators[itemGenerator].setItemMaximumNum(setting["item"][itemGenerator]["num"])
			self.mItemGenerators[itemGenerator].setDropProbability(setting["item"][itemGenerator]["probability"])
			self.mItemGenerators[itemGenerator].setItemLifeTimer(setting["item"][itemGenerator]["lifeTimer"])
		return level