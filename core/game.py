import pygame,time

from event import event, keyboardEventHandler, io_eventHandler, snakeEventCreator
from event import listener
from gameObject import skin, score
from gameObject.items import item, apple
from player import snake, snakeDisplayHandler, snakeStateHandler
from utils import dataSavor
from utils.setting import *

class Game(object):
	def __init__(self, screen):
		self.screen = screen

	def setGameSessionToFalse(self):
		self.gameSession = False
	# def setGameOverTrue(self):
	# 	self.gameOver = True
	def display_intro(self):
		return 0


	def player1_highScore_gameLoop(self):
		defaultSpeed = 30
		defaultThick = 20

		self.gameIsRunning = True
		self.gameSession = True

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

		mOnKeyListenerHandler = listener.ListenerHandler()
		mOnTickListenerHandler = listener.ListenerHandler()

		mKeyboardEventHandler = keyboardEventHandler.KeyboardEventHandler(mOnKeyListenerHandler)
		mIOEventHandler = io_eventHandler.IOEventHandler(mKeyboardEventHandler, mOnTickListenerHandler, mScore)
		mSnakeEventCreator = snakeEventCreator.SnakeEventCreator()
		mEvent = event.Event(mOnTickListenerHandler)

		player = snake.Snake(1, defaultSpeed, defaultThick, skin.Skin())
		mSnakeStateHandler = snakeStateHandler.SnakeStateHandler(player, mOnKeyListenerHandler, mOnTickListenerHandler, mIOEventHandler)
		mSnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(player)

		itemAppleGenerator = item.ItemGenerator(apple.Apple, 1)

		groupText.add(mScoreDisplayHandler.draw())
		itemAppleGenerator.setItemMaximumNum(2)


		while self.gameSession:
			# Make Event
			mEvent.onTick()

			# mIOEventHandler.handleEvent()
			mSnakeEventCreator.crashWall(player, self.setGameSessionToFalse)
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
			self.screen.fill((100,200,255))

			mSnakeDisplayHandler.update()
			mSnakeDisplayHandler.draw(self.screen)

			allSprites.update()
			allSprites.draw(self.screen)

			# Update Screen
			pygame.display.update()
			pygame.time.Clock().tick(FRAMES_PER_SECOND)

		mScoreSavor.saveScore(mScore.getScore())
		print(mScoreSavor.getTopScore(10))

	def player2_highScore_gameLoop(self):
		pass
	def player2_compete_gameLoop(self):
		pass