from utils import utility
from utils.setting import SKIN_BODY, SKIN_TAIL, SKIN_FIRST, SKIN_CURVE, SKIN_HEAD


class Skin(object):
	def __init__(self):
		skin_default = ["default_head", None, "default_tail","default_first", "default_curve"]
		skin_first = ["default_head", "first_body", "first_tail", "default_first", None]
		self.skinList = [skin_default, skin_first]

	def getSkin(self, skinNum):
		return self.loadSkin(skinNum)

	def loadSkin(self, skinNum):
		self.skinDic = {}
		self.skinDic["head"] = utility.loadImage(self.skinList[skinNum][SKIN_HEAD])

		if self.skinList[skinNum][SKIN_BODY] is not None:
			self.skinDic["body"] = utility.loadImage(self.skinList[skinNum][SKIN_BODY])
		else:
			self.skinDic["body"] = None

		self.skinDic["tail"] = utility.loadImage(self.skinList[skinNum][SKIN_TAIL])

		if self.skinList[skinNum][SKIN_FIRST] is not None:
			self.skinDic["first"] = utility.loadImage(self.skinList[skinNum][SKIN_FIRST])
		else:
			self.skinDic["first"] = None

		if self.skinList[skinNum][SKIN_CURVE] is not None:
			self.skinDic["curve"] = utility.loadImage(self.skinList[skinNum][SKIN_CURVE])
		else:
			self.skinDic["curve"] = None

		return self.skinDic