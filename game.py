import pygame

from event import event, keyboardEventHandler, io_eventHandler, snakeEventHandler
from event import listener
from gameObject import skin
from gameObject.items import item, apple
from player import snake, snakeDisplayHandler, snakeStateHandler
from utils.setting import *

class Game(object):
	def __init__(self, screen):
		self.screen = screen

	def setGameRunningToFalse(self):
		self.gameIsRunning = False
	# def setGameOverTrue(self):
	# 	self.gameOver = True
	def display_intro(self):
		return 0


	def player1_highScore_gameLoop(self):
		defaultSpeed = 30
		defaultThick = 20

		self.gameIsRunning = True

		# setting
		mOnKeyListenerHandler = listener.ListenerHandler()
		mOnTickListenerHandler = listener.ListenerHandler()

		mKeyboardEventHandler = keyboardEventHandler.KeyboardEventHandler(mOnKeyListenerHandler)
		mIOEventHandler = io_eventHandler.IOEventHandler(mKeyboardEventHandler, mOnTickListenerHandler)
		mSnakeEventHandler = snakeEventHandler.SnakeEventHandler()
		mEvent = event.Event(mOnTickListenerHandler)

		player = snake.Snake(1, defaultSpeed, defaultThick, skin.Skin())
		mSnakeStateHandler = snakeStateHandler.SnakeStateHandler(player, mOnKeyListenerHandler, mOnTickListenerHandler, mIOEventHandler)
		mSnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(player)
		itemAppleGenerator = item.ItemGenerator(apple.Apple, 1)

		GroupApple = pygame.sprite.Group()
		GroupItem = pygame.sprite.Group()
		GroupWall = pygame.sprite.Group()
		allSprites = pygame.sprite.Group()

		itemAppleGenerator.setItemMaximumNum(2)
		while self.gameIsRunning:
			mEvent.onTick()

			objectApple = itemAppleGenerator.dropItem()
			if objectApple:
				GroupApple.add(objectApple)
			print(GroupApple.sprites()[0].getLocation())
			# Group Update
			try:
				GroupItem.add(GroupApple.sprites())
				allSprites.add(GroupItem.sprites(), GroupWall.sprites())
			except:
				pass


			self.screen.fill((100,200,255))
			mSnakeEventHandler.crashWall(player, self.setGameRunningToFalse)

			mSnakeDisplayHandler.update()
			mSnakeDisplayHandler.draw(self.screen)

			allSprites.update()
			allSprites.draw(self.screen)

			pygame.display.update()
			pygame.time.Clock().tick(FRAMES_PER_SECOND)

	def player2_highScore_gameLoop(self):
		pass
	def player2_compete_gameLoop(self):
		pass