import utility
from setting import *

class Skin():
	def __init__(self):
		skin_default = ["default_head", None, "default_tail","default_first"]
		self.skinList = [skin_default]

	def getSkin(self, skinNum):
		return self.loadSkin(skinNum)

	def loadSkin(self, skinNum):
		self.skinDic = {}
		self.skinDic["head"] = utility.loadImage(self.skinList[skinNum][SKIN_HEAD])
		if self.skinList[skinNum][SKIN_BODY] != None:
			self.skinDic["body"] = utility.loadImage(self.skinList[skinNum][SKIN_BODY])
		else:
			self.skinDic["body"] = None
		self.skinDic["tail"] = utility.loadImage(self.skinList[skinNum][SKIN_TAIL])
		if self.skinList[skinNum][SKIN_FIRST] != None:
			self.skinDic["first"] = utility.loadImage(self.skinList[skinNum][SKIN_FIRST])
		else:
			self.skinDic["first"] = None
		return self.skinDic