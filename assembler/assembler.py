import pygame

from event import eventDistributor
from event.eventCreators import snakeEventCreator
from event.eventHandlers import keyboardEventHandler, tickEventHandler, crashItemEventHandler
from gameObject import score, level
from gameObject.items import item, apple
from gameObject.player import snake, snakeAction
from gameObject.player import snakeDisplayHandler
from ui import scoreTable, popUp
from utils import dataSavor, listener
from utils.setting import SKIN_DEFAULT, RIGHT, SCREEN_MID, GREEN


class Assembler_NotCreatedError(Exception):
    # def __init__(self, funcName):
    def __init__(self):
        pass
        # self.funcName = funcName
    def __str__(self):
        # return "function '%s' is not created" % self.funcName
        return "function is not created"

def checkNotNone(func):
    def wrapper(*args):
        result = func(*args)
        if result is not None:
            return result
        else:
            raise Assembler_NotCreatedError()
    return wrapper


class Assembler(object):
    def createGroupItem(self):
        self._groupItem = pygame.sprite.Group()
    @checkNotNone
    def getGroupItem(self):
        return self._groupItem



    def createScore(self):
        """ create score """
        self._Score = score.Score()
    @checkNotNone
    def getScore(self):
        return self._Score



    def createScoreDisplay(self):
        """ create related to score display """
        self._ScoreDisplayHandler = score.ScoreDisplayHandler(self.getScore())
        self._ScoreSavor = dataSavor.ScoreSavor()
    @checkNotNone
    def getScoreDisplayHandler(self):
            return self._ScoreDisplayHandler
    @checkNotNone
    def getScoreSavor(self):
            return self._ScoreSavor



    def createScoreTable(self):
        """ create related to score table at the end of game """
        self._ScoreTable = scoreTable.ScoreTable()
    @checkNotNone
    def getScoreTable(self):
        return self._ScoreTable



    def createListenerHandler(self):
        """ create listener handler """
        self.__listener = listener.ListenerHandler()
    def getListenerHandler(self):
        if self.__listener is not None:
            self.__listener = None
            return self.__listener
        else:
            raise Assembler_NotCreatedError()



    def createEventDistributor(self, eventListToListen):
        """ create event distributor """
        self._PygameEventDistributor = eventDistributor.pygameEventDistributor(eventListToListen)
    @checkNotNone
    def getPygameEventDistributor(self):
        return self._PygameEventDistributor



    def createKeyboardEventHandler(self):
        """ create keyboard event handler """
        self._KeyboardEventHandler = keyboardEventHandler.KeyboardEventHandler(self.getPygameEventDistributor())
    @checkNotNone
    def getKeyboardEventHandler(self):
        return self._KeyboardEventHandler



    def createTickEventHandler(self):
        """ create tick event handler """
        self._TickEventHandler = tickEventHandler.TickEventHandler(self.getPygameEventDistributor())
    @checkNotNone
    def getTickEventHandler(self):
        return self._TickEventHandler

    def createCrashItemEventHandler(self, screen):
        self._CrashItemEventHandler = crashItemEventHandler.CrashItemEventHandler(self.getPygameEventDistributor(), screen, self.getScore())
    @checkNotNone
    def getCrashItemEventHandler(self):
        return self._CrashItemEventHandler



    def createSnakeEventCreator(self):
        """ create snake event creator """
        self._SnakeEventCreator = snakeEventCreator.SnakeEventCreator(self._getSnake(), self.getGroupItem())
    @checkNotNone
    def _getSnakeEventCreator(self):
        return self._SnakeEventCreator


    def createRelatedToSnake(self,speed, thick, skin, control, skinNum = SKIN_DEFAULT, firstHeadDirection = RIGHT, headPos = SCREEN_MID, color = GREEN, length = 1):
        """ create player """
        self._snake = snake.Snake(self.getPygameEventDistributor(), speed, thick, skin, skinNum=skinNum, firstHeadDirection=firstHeadDirection, headPos=headPos, color=color, length=length)
        self._SnakeAction = snakeAction.SnakeAction(self._snake, self.getKeyboardEventHandler(), control)
        self._SnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(self._snake)

    @checkNotNone
    def _getSnake(self):
        return self._snake
    @checkNotNone
    def _getSnakeAction(self):
        return self._SnakeAction
    @checkNotNone
    def _getSnakeDisplayHandler(self):
        return self._SnakeDisplayHandler



    def createPausePage(self):
        """ create pause page """
        self._PausePage = popUp.PausePage()
    @checkNotNone
    def getPausePage(self):
        return self._PausePage



    def createAppleItemSpawner(self, appleImg, appleSound = None):
        """ create apple item generator """
        if appleSound:
            appleSound.set_volume(1)
        self._ApplePrototype = apple.Apple(appleImg, sound = appleSound)
        self._itemAppleSpawner = item.ItemSpawner(self._ApplePrototype)
    @checkNotNone
    def getItemAppleSpawner(self):
        return self._itemAppleSpawner



    def createLevelHandler(self, gameName, ItemSpawners):
        """ create game state handler """
        self._LevelHandler = level.LevelHandler(gameName, self._getSnake(), ItemSpawners)
    @checkNotNone
    def getLevelHandler(self):
        return self._LevelHandler

    def getPlayers(self):
        NotImplementedError("You should implement getPlayers(%s)" % self)
