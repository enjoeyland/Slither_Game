from utils.setting import MAX_LEVEL, LEVEL


class Level():
	def __init__(self):
		self.settingPerLevel = LEVEL

	def setSettingPerLevel(self, settingPerLevel):
		self.settingPerLevel = settingPerLevel

	def getLevel(self, score, gameName = None):
		for level in range(self.settingPerLevel[gameName][MAX_LEVEL]["level"]):
			if self.settingPerLevel[gameName][level]["score"] <= score < self.settingPerLevel[gameName][level + 1]["score"]:
				return self.settingPerLevel[gameName][level]["level"]
		else:
			if self.settingPerLevel[gameName][MAX_LEVEL]["score"] <= score:
				return self.settingPerLevel[gameName][MAX_LEVEL]["level"]

	def getLevelSetting(self):
		return self.settingPerLevel

class GameHandler():
	def __init__(self, mSnake, mItemGenerators, levelClass = Level, gameName = None):
		self.mLevel = levelClass()
		self.gameName = gameName
		self.mSnake = mSnake
		self.mItemGenerators = mItemGenerators

		self.lastLevel = 0

	def update(self, score):
		currentLevel = self.getLevel(score)
		self.checkLevelChange(currentLevel)

	def checkLevelChange(self, level):
		if self.lastLevel != level:
			print("Level %s" % level)

		self.lastLevel = level

	def setLevel(self, score):
		level = self.getLevel(score)
		levelSetting = self.mLevel.getLevelSetting()
		setting = levelSetting[self.gameName][level]["setting"]

		self.mSnake.setAttributes(speed = setting["snake"]["speed"], thick = setting["snake"]["thick"])

		for itemGenerator in self.mItemGenerators.keys():
			self.mItemGenerators[itemGenerator].setItemMaximumNum(setting["item"][itemGenerator]["num"])
			self.mItemGenerators[itemGenerator].setDropProbability(setting["item"][itemGenerator]["probability"])
			self.mItemGenerators[itemGenerator].setItemLifeTimer(setting["item"][itemGenerator]["lifeTimer"])
		return level

	def getLevel(self, score):
		return self.mLevel.getLevel(score, self.gameName)