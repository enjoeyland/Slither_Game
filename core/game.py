import pygame
import time

from event import event, keyboardEventHandler, io_eventHandler, snakeEventCreator
from event import listener
from gameObject import skin, score
from gameObject.items import item, apple
from player import snake, snakeDisplayHandler, snakeStateHandler
from ui import scoreTable, popUp
from utils import dataSavor
from utils.setting import FRAMES_PER_SECOND, SCREEN_BACKGROUND


class Game(object):
	def __init__(self, screen):
		self.screen = screen

	def setGameSessionToFalse(self):
		self.gameSession = False

	def setGameRunningToFalse(self):
		self.isGameRunning = False

	def pause(self):
		if not self.isPause:
			self.isGameRunning = False
			self.isPause = True
		else:
			self.isGameRunning = True
			self.isPause = False

	# def clickMenuButton(self, buttonSprite):
	# 	if buttonSprite.isClicked():
	# 		pass
	## 다시 button 만들기
	def setButtonSprite(self, name, buttonSprite):
		self.buttonSprite = buttonSprite
		if name == "replay":
			return self.clickReplayButton
		elif name == "menu":
			pass

	def clickReplayButton(self):
		if self.buttonSprite.isClicked():
			self.gameReplay = True

	# def setGameOverTrue(self):
	# 	self.gameOver = True
	def display_intro(self):
		return 0


	def player1_highScore_gameLoop(self):
		defaultSpeed = 30
		defaultThick = 20

		self.isGameRunning = True
		self.gameSession = True
		self.gameReplay = False
		self.isPause = False

		# Create Group
		groupApple = pygame.sprite.Group()
		groupItem = pygame.sprite.Group()
		groupWall = pygame.sprite.Group()
		groupText = pygame.sprite.Group()
		allSprites = pygame.sprite.Group()

		# Setting
		mScore = score.Score()
		mScoreDisplayHandler = score.ScoreDisplayHandler(mScore)
		mScoreSavor = dataSavor.ScoreSavor()
		mScoreTable = scoreTable.ScoreTable(self.screen)

		mOnKeyListenerHandler = listener.ListenerHandler()
		mOnTickListenerHandler = listener.ListenerHandler()

		mKeyboardEventHandler = keyboardEventHandler.KeyboardEventHandler(mOnKeyListenerHandler)
		mIOEventHandler = io_eventHandler.IOEventHandler(mKeyboardEventHandler, mOnTickListenerHandler, mScore)
		mSnakeEventCreator = snakeEventCreator.SnakeEventCreator()
		mEvent = event.Event(mOnTickListenerHandler)

		player = snake.Snake(1, defaultSpeed, defaultThick, skin.Skin())
		mSnakeStateHandler = snakeStateHandler.SnakeStateHandler(player, mOnKeyListenerHandler, mOnTickListenerHandler, mIOEventHandler)
		mSnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(player)

		mPausePage = popUp.PausePage(self.screen)

		itemAppleGenerator = item.ItemGenerator(apple.Apple, 1)

		groupText.add(mScoreDisplayHandler.draw())
		itemAppleGenerator.setItemMaximumNum(2)
		mOnKeyListenerHandler.listen(pygame.K_p, self.pause)

		menuButton = {"name" : "menu", "listener" : mOnTickListenerHandler, "func": self.setButtonSprite}
		replayButton = {"name" : "replay", "listener" : mOnTickListenerHandler, "func": self.setButtonSprite}

		while self.gameSession:

			while self.isGameRunning:
				# Make Event
				mEvent.onTick()

				# mIOEventHandler.handleEvent()
				mSnakeEventCreator.crashWall(player, self.setGameRunningToFalse)
				mSnakeEventCreator.crashItem(player, groupItem)

				# Drop Item
				objectApple = itemAppleGenerator.dropItem()
				if objectApple:
					groupApple.add(objectApple)

				# Group Update
				try:
					groupItem.add(groupApple.sprites())
					allSprites.add(groupItem.sprites(), groupWall.sprites(), groupText.sprites())
				except:
					pass

				# Build Screen
				self.screen.fill(SCREEN_BACKGROUND)

				mSnakeDisplayHandler.update()
				mSnakeDisplayHandler.draw(self.screen)

				allSprites.update()
				allSprites.draw(self.screen)

				# Update Screen
				pygame.display.update()
				pygame.time.Clock().tick(FRAMES_PER_SECOND)

			if self.isPause:
				# End Listen

				mSnakeStateHandler.endListen()

				pauseSprite = mPausePage.draw()
				groupText.add(pauseSprite)
				allSprites.add(groupText.sprites())

				groupText.update()
				groupText.draw(self.screen)
				pygame.display.update()

				while self.isPause:
					mEvent.onTick()
					pygame.time.Clock().tick(3)

				pauseSprite.kill()

				#listen
				mSnakeStateHandler.setListener()

			else:
				self.setGameSessionToFalse()
				mScoreSavor.saveScore(mScore.getScore())

				scoreTextSprites = mScoreTable.draw(mScoreSavor.getTopScore(10), mScore.getScore(), replayButton)
				groupText.add(scoreTextSprites)
				allSprites.add(groupText.sprites())

				groupText.update()
				groupText.draw(self.screen)
				pygame.display.update()

				while not self.gameReplay:
					mEvent.onTick()
					pygame.time.Clock().tick(3)

				for scoreTextSprite in scoreTextSprites:
					scoreTextSprite.kill()

		return self.gameReplay

	def player2_highScore_gameLoop(self):
		pass
	def player2_compete_gameLoop(self):
		pass