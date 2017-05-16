from event import listener, io_eventHandler, keyboardEventHandler
from gameObject import score
from ui import scoreTable
from utils import dataSavor

class NotAssemblerCreatedError(Exception):
	def __init__(self, funcName):
		self.funcName = funcName
	def __str__(self):
		return "function '%s' is not created" % self.funcName

class Assembler(object):
	def __init__(self):
		self._Score = score.Score()
		self.createEventDistributor()

	def getScore(self):
		return self._Score



	def createScoreDisplay(self):
		""" create related to score display """
		self._ScoreDisplayHandler = score.ScoreDisplayHandler(self._Score)
		self._ScoreSavor = dataSavor.ScoreSavor()

	def getScoreDisplayHandler(self):
		if self._ScoreDisplayHandler is not None:
			return self._ScoreDisplayHandler
		else:
			raise NotAssemblerCreatedError("createScoreDisplay")

	def getScoreSavor(self):
		if self._ScoreSavor is not None:
			return self._ScoreSavor
		else:
			raise NotAssemblerCreatedError("createScoreDisplay")



	def createScoreTable(self):
		""" create related to score table at the end of game """
		self._ScoreTable = scoreTable.ScoreTable()

	def getScoreTable(self):
		if self._ScoreTable is not None:
			return self._ScoreTable
		else:
			raise NotAssemblerCreatedError("createScoreTable")



	def createListenerHandler(self):
		""" create listener handler """
		self.__listener = listener.ListenerHandler()

	def getListenerHandler(self):
		if self.__listener is not None:
			self.__listener = None
			return self.__listener
		else:
			raise NotAssemblerCreatedError("createScoreTable")



		# mOnKeyListenerHandler = listener.ListenerHandler()
		# mOnTickListenerHandler = listener.ListenerHandler()
		# mPygameEventListenerHandler = listener.ListenerHandler()

		# mPygameEventQueue = queue.Queue()
	def createEventDistributor(self):
		""" create event distributor """
		self.createListenerHandler()
		self._PygameEventListenerHandler = self.getListenerHandler()
		self._PygameEventDistributor = io_eventHandler.pygameEventDistributor(self._PygameEventListenerHandler)

	def getPygameEventListenerHandler(self):
		if self._PygameEventListenerHandler is not None:
			return self._PygameEventListenerHandler
		else:
			raise NotAssemblerCreatedError("createEventDistributor")

	def getPygameEventDistributor(self):
		if self._PygameEventDistributor is not None:
			return self._PygameEventDistributor
		else:
			raise NotAssemblerCreatedError("createEventDistributor")

	def createKeyboardEventHandler(self):
		""" create keyboard event handler """
		self.createListenerHandler()
		self._OnKeyListenerHandler = self.getListenerHandler()
		self._KeyboardEventHandler = keyboardEventHandler.KeyboardEventHandler(self._OnKeyListenerHandler)

	def getOnKeyListenerHandler(self):
		if self._OnKeyListenerHandler is not None:
			return self._OnKeyListenerHandler
		else:
			raise NotAssemblerCreatedError("createKeyboardEventHandler")

	def getKeyboardEventHandler(self):
		if self._KeyboardEventHandler is not None:
			return self._KeyboardEventHandler
		else:
			raise NotAssemblerCreatedError("createKeyboardEventHandler")


		_IOEventHandler = io_eventHandler.IOEventHandler(_KeyboardEventHandler, _OnTickListenerHandler, _Score, self.screen)

		# event creator
		_SnakeEventCreator = snakeEventCreator.SnakeEventCreator()
		_Event = event.Event(_OnTickListenerHandler)

		# player
		player = snake.Snake(1, DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(), skinNum= SKIN_DEFAULT)
		_SnakeStateHandler = snakeStateHandler.SnakeStateHandler(player, _OnKeyListenerHandler, _OnTickListenerHandler, _IOEventHandler)
		_SnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(player)

		# puase page
		_PausePage = popUp.PausePage()

		# item
		itemAppleGenerator = item.ItemGenerator(apple.Apple)

		# level
		_GameHandler = level.GameHandler(player, {"apple": itemAppleGenerator}, gameName= PLAYER1_HIGH_SCORE)
