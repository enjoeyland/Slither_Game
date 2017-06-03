from event import eventDistributor
from event.eventCreators import snakeEventCreator, tickEventCreator
from event.eventHandlers import keyboardEventHandler, tickEventHandler
from gameObject import score, skin, level
from gameObject.items import item, apple
from player import snake, snakeStateHandler, snakeDisplayHandler
from ui import scoreTable, popUp
from utils import dataSavor, listener
from utils.setting import DEFAULT_SPEED, DEFAULT_THICK, SKIN_DEFAULT, PLAYER1_HIGH_SCORE


class NotAssemblerCreatedError(Exception):
	def __init__(self, funcName):
		self.funcName = funcName
	def __str__(self):
		return "function '%s' is not created" % self.funcName

class Assembler(object):
	def __init__(self):
		self.createScore()
		self.createEventDistributor()
		self.createKeyboardEventHandler()
		self.createTickEventHandler()
		self.createPlayer()

		#
		self.createScoreDisplay()
		self.createScoreTable()

		self.createSnakeEventCreator()
		self.createTickEventCreator()

		self.createPausePage()
		self.createAppleItemGenerator()
		self.createGameHandler(PLAYER1_HIGH_SCORE)

	def createScore(self):
		""" create score """
		self._Score = score.Score()

	def getScore(self):
		if self._Score is not None:
			return self._Score
		else:
			raise NotAssemblerCreatedError("createScore")



	def createScoreDisplay(self):
		""" create related to score display """
		self._ScoreDisplayHandler = score.ScoreDisplayHandler(self.getScore())
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



	def createEventDistributor(self):
		""" create event distributor """
		self._PygameEventDistributor = eventDistributor.pygameEventDistributor()

	def getPygameEventDistributor(self):
		if self._PygameEventDistributor is not None:
			return self._PygameEventDistributor
		else:
			raise NotAssemblerCreatedError("createEventDistributor")



	def createKeyboardEventHandler(self):
		""" create keyboard event handler """
		self._KeyboardEventHandler = keyboardEventHandler.KeyboardEventHandler(self.getPygameEventDistributor())

	def getKeyboardEventHandler(self):
		if self._KeyboardEventHandler is not None:
			return self._KeyboardEventHandler
		else:
			raise NotAssemblerCreatedError("createKeyboardEventHandler")



	def createTickEventHandler(self):
		""" create tick event handler """
		self._TickEventHandler = tickEventHandler.TickEventHandler(self.getPygameEventDistributor())

	def getTickEventHandler(self):
		if self._TickEventHandler is not None:
			return self._TickEventHandler
		else:
			raise NotAssemblerCreatedError("createTickEventHandler")



	def createSnakeEventCreator(self):
		""" create snake event creator """
		self._SnakeEventCreator = snakeEventCreator.SnakeEventCreator()

	def getSnakeEventCreator(self):
		if self._SnakeEventCreator is not None:
			return self._SnakeEventCreator
		else:
			raise NotAssemblerCreatedError("createSnakeEventCreator")



	def createTickEventCreator(self):
		""" create tick event creator """
		self._TickEventCreator = tickEventCreator.TickEventCreator()

	def getTickEventCreator(self):
		if self._TickEventCreator is not None:
			return self._TickEventCreator
		else:
			raise NotAssemblerCreatedError("createTickEventCreator")



	def createPlayer(self):
		""" create player """
		self._player = snake.Snake(1, DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(), skinNum= SKIN_DEFAULT)
		self._SnakeStateHandler = snakeStateHandler.SnakeStateHandler(self._player, self.getKeyboardEventHandler(), self.getTickEventHandler(), self.getPygameEventDistributor())
		self._SnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(self._player)

	def getPlayer(self):
		if self._player is not None:
			return self._player
		else:
			raise NotAssemblerCreatedError("createPlayer")

	def getSnakeStateHandler(self):
		if self._SnakeStateHandler is not None:
			return self._SnakeStateHandler
		else:
			raise NotAssemblerCreatedError("createPlayer")

	def getSnakeDisplayHandler(self):
		if self._SnakeDisplayHandler is not None:
			return self._SnakeDisplayHandler
		else:
			raise NotAssemblerCreatedError("createPlayer")



	def createPausePage(self):
		""" create pause page """
		self._PausePage = popUp.PausePage()

	def getPausePage(self):
		if self._PausePage is not None:
			return self._PausePage
		else:
			raise NotAssemblerCreatedError("createPausePage")



	def createAppleItemGenerator(self):
		""" create apple item generator """
		self._itemAppleGenerator = item.ItemGenerator(apple.Apple)

	def getItemAppleGenerator(self):
		if self._itemAppleGenerator is not None:
			return self._itemAppleGenerator
		else:
			raise NotAssemblerCreatedError("createAppleItemGenerator")



	def createGameHandler(self, gameName):
		""" create game state handler """
		self._GameHandler = level.GameHandler(self.getPlayer(), {"apple": self.getItemAppleGenerator()}, gameName= gameName)


	def getGameHandler(self):
		if self._GameHandler is not None:
			return self._GameHandler
		else:
			raise NotAssemblerCreatedError("createGameHandler")