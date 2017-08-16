import os

import sys

from utils.setting import MAX_LEVEL, LEVEL


class Level():
	def __init__(self):
		self.settingPerLevel = LEVEL

	def setSettingPerLevel(self, settingPerLevel):
		self.settingPerLevel = settingPerLevel

	def getLevel(self, score, gameName):
		for level in range(self.settingPerLevel[gameName][MAX_LEVEL]["level"]):
			if self.settingPerLevel[gameName][level]["score"] <= score < self.settingPerLevel[gameName][level + 1]["score"]:
				return self.settingPerLevel[gameName][level]["level"]
		else:
			if self.settingPerLevel[gameName][MAX_LEVEL]["score"] <= score:
				return self.settingPerLevel[gameName][MAX_LEVEL]["level"]

	def getLevelSetting(self,gameName, level):
		return self.settingPerLevel[gameName][level]

class LevelHandler():
	def __init__(self, gameName, mSnake = None, ItemSpawners = None, levelClass = Level):
		self.mLevel = levelClass()
		self.gameName = gameName
		self.mSnake = mSnake
		self.ItemSpawners = ItemSpawners

		self.lastLevel = -1

	def update(self, score):
		currentLevel = self.getLevel(score)
		if self.isLevelChange(currentLevel):
			self.setLevel(currentLevel)
			self.setLevelSetting(currentLevel)

	def isLevelChange(self, level):
		if self.lastLevel != level:
			return True
		return False
		# self.lastLevel = level

	def setLevel(self, level):
		self.lastLevel = level
		if os.path.split(os.path.abspath(sys.argv[0]))[1] != "training.py" and self.ItemSpawners:
			print("Level %s" % level)

	def setLevelSetting(self, level):
		levelSetting = self.mLevel.getLevelSetting(self.gameName,level)["setting"]

		if self.mSnake:
			self.mSnake.setAttributes(speed = levelSetting["snake"]["speed"], thick = levelSetting["snake"]["thick"])

		if self.ItemSpawners:
			for itemSpawner in self.ItemSpawners.keys():
				self.ItemSpawners[itemSpawner].setItemMaximumNum(levelSetting["item"][itemSpawner]["num"])
				self.ItemSpawners[itemSpawner].setDropProbability(levelSetting["item"][itemSpawner]["probability"])
				self.ItemSpawners[itemSpawner].setItemLifeTimer(levelSetting["item"][itemSpawner]["lifeTimer"])

	def getLevel(self, score):
		return self.mLevel.getLevel(score, self.gameName)