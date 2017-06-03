import queue

import pygame

from event import eventDistributor
from event.eventCreators import eventCreator, snakeEventCreator
from event.eventHandlers import keyboardEventHandler
from gameObject import skin, score, level
from gameObject.items import item, apple
from player import snake, snakeDisplayHandler, snakeStateHandler
from ui import scoreTable, popUp
from utils import dataSavor, utility, listener
from utils.setting import FRAMES_PER_SECOND, SCREEN_BACKGROUND, DEFAULT_SPEED, DEFAULT_THICK, SKIN_DEFAULT, \
	PLAYER1_HIGH_SCORE, PLAY_INFINITELY


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

	def clickReplayButton(self):
		self.gameReplay = True

	def clickQuitButton(self):
		pygame.quit()
		quit()

	# def setGameOverTrue(self):
	# 	self.gameOver = True
	def display_intro(self):
		return PLAYER1_HIGH_SCORE


	def player1_highScore_gameLoop(self):
		self.isGameRunning = True
		self.gameSession = True
		self.gameReplay = False
		self.isPause = False

		# Load Image
		appleImg = utility.loadImage("apple")

		# Load Sound
		soundAppleBite = utility.loadSound("Apple_Bite")
		soundAppleBite.set_volume(1)
		soundBGM = utility.loadSound("BGM")
		soundBGM.set_volume(0.3)

		# Create Group
		groupApple = pygame.sprite.Group()
		groupItem = pygame.sprite.Group()
		groupWall = pygame.sprite.Group()
		groupText = pygame.sprite.Group()
		groupPopUp = pygame.sprite.Group()
		allSprites = pygame.sprite.Group()

		# Setting
		mScore = score.Score()
		mScoreDisplayHandler = score.ScoreDisplayHandler(mScore)
		mScoreSavor = dataSavor.ScoreSavor()
		mScoreTable = scoreTable.ScoreTable()

		mOnKeyListenerHandler = listener.ListenerHandler()
		mOnTickListenerHandler = listener.ListenerHandler()
		mPygameEventListenerHandler = listener.ListenerHandler()

		mPygameEventQueue = queue.Queue()
		mPygameEventDistributor = eventDistributor.pygameEventDistributor(mPygameEventListenerHandler, mPygameEventQueue)


		mKeyboardEventHandler = keyboardEventHandler.KeyboardEventHandler(mOnKeyListenerHandler)
		mIOEventHandler = eventDistributor.IOEventHandler(mKeyboardEventHandler, mOnTickListenerHandler, mScore, self.screen)
		mSnakeEventCreator = snakeEventCreator.SnakeEventCreator()
		mEvent = eventCreator.Event(mOnTickListenerHandler)

		player = snake.Snake(1, DEFAULT_SPEED, DEFAULT_THICK, skin.Skin(), skinNum= SKIN_DEFAULT)
		mSnakeStateHandler = snakeStateHandler.SnakeStateHandler(player, mOnKeyListenerHandler, mOnTickListenerHandler, mIOEventHandler)
		mSnakeDisplayHandler = snakeDisplayHandler.SnakeDisplayHandler(player)

		mPausePage = popUp.PausePage()

		itemAppleGenerator = item.ItemGenerator(apple.Apple)

		mGameHandler = level.GameHandler(player, {"apple": itemAppleGenerator}, gameName= PLAYER1_HIGH_SCORE)

		mPygameEventDistributor.start()
		groupText.add(mScoreDisplayHandler.draw())
		mGameHandler.update(mScore.getScore())

		mOnKeyListenerHandler.listen(pygame.K_p, self.pause)

		# menuButton = {"name" : "menu", "listener" : mOnTickListenerHandler, "func": self.setButtonSprite}
		replayButton = {"name" : "replay", "listener" : mOnTickListenerHandler, "func": self.clickReplayButton}
		quitButton = {"name" : "quit", "listener" : mOnTickListenerHandler, "func" : self.clickQuitButton}

		while self.gameSession:
			utility.playSound(soundBGM, loops= PLAY_INFINITELY)

			while self.isGameRunning:

				# Make Event
				mEvent.onTick()

				mPygameEventQueue.put(pygame.event.get())
				mPygameEventQueue.join()

				mSnakeEventCreator.crashWall(player, self.setGameRunningToFalse)
				mSnakeEventCreator.crashItself(player, self.setGameRunningToFalse)
				mSnakeEventCreator.crashItem(player, groupItem)

				mGameHandler.update(mScore.getScore())

				# Drop Item
				objectApple = itemAppleGenerator.dropItem(image= appleImg, sound= soundAppleBite)
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

			### Out of Gam running loop ###
			soundBGM.fadeout(2)

			if self.isPause:
				# End Listen
				mSnakeStateHandler.endListen()

				groupPopUp.add(mPausePage)
				allSprites.add(groupPopUp.sprites())

				groupPopUp.update()
				groupPopUp.draw(self.screen)
				pygame.display.update()

				while self.isPause:
					mEvent.onTick()

					pygame.display.update()
					pygame.time.Clock().tick(3)

				mPausePage.kill()

				#listen
				mSnakeStateHandler.setListener()

			else:
				self.setGameSessionToFalse()
				# End Listen
				mSnakeStateHandler.endListen()

				mScoreSavor.saveScore(mScore.getScore())
				mScoreTable.buildImage(mScoreSavor.getTopScore(10), mScore.getScore(), replayButton)

				groupPopUp.add(mScoreTable)
				groupPopUp.draw(self.screen)
				groupPopUp.update()
				pygame.display.update()

				while not self.gameReplay:
					mEvent.onTick()

					self.screen.fill(SCREEN_BACKGROUND)
					mSnakeDisplayHandler.draw(self.screen)
					allSprites.draw(self.screen)

					groupPopUp.draw(self.screen)
					groupPopUp.update()

					pygame.display.update()
					pygame.time.Clock().tick(10)

				mScoreTable.kill()

		return self.gameReplay

	def player2_highScore_gameLoop(self):
		pass
	def player2_compete_gameLoop(self):
		pass