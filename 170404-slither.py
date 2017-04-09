import pygame, threading
pygame.init()

#value
"""Screen"""
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
SCREEN_MID = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

FRAMES_PER_SECOND = 30.0

"""Direction"""
LEFT = 1
DOWN = 2
RIGHT = 3
UP = 4

"""Color"""
GREEN = (0,255,0)

"""Snake"""
SNAKE_HEAD = -1
SNAKE_TAIL = 0
POS_X = 0
POS_Y = 1
DIRECTION = 2

"""Skin"""
SKIN_HEAD = 0
SNAKE_BODY = 1
SNAKE_TAIL = 2

"""Item"""
CONTINUANCE = -1

"""Img"""
# icon = pygame.image.load('apple.png')

"""Sound"""
# fire_sound=pygame.mixer.Sound("fire.wav")
	# pygame.mixer.Sound.play(fire_sound)


clock=pygame.time.Clock()

		# pygame.display.update()
		# clock.tick(FRAMES_PER_SECOND)
#magnification #배울


class GameSetting():
	def __init__(self):
		self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))#surface화면
		# screen = pygame.display.set_mode((640,480),SWSURFACE|FULLSCREEN)
		pygame.display.set_caption('Slither')
		pygame.display.set_icon(icon)
	def getScreen(self):
		return self.screen

class Screen():
	def __init__(self):
		self.screen = GameSetting.getScreen()
	@property
	def screen(self):
		return self.screen


# class Text():
	# pass
class GameDisplay():
	def display_text():
		pass

class Event():
	pass

class KeyboardEventHandler(Event):
	def __init__(self):
		pass
	def process(self, event, gameState):
		if event.key==pygame.K_q:
			pygame.quit()
			quit()
		if event.key==pygame.K_c:
			intro=False

class IOEventHandler(Event, threading.Thread):
	def __init__(self):
		threading.Thread.__init__(self)
		self.__suspend = False
		self.__exit = False
		self.keh = KeyboardEventHandler()

	def threadRun(self):
		while True:
			### Suspend ###
			while self.__suspend:
				time.sleep(0.5)
			### Process ###
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					pygame.quit()
					quit()
				elif event.type==pygame.KEYDOWN:
					self.keh.process(event, self.gameState)
			### Exit ###
			if self.__exit:
				break
	def threadSuspend(self): self.__suspend = True
	def threadResume(self): self.__suspend = False	
	def threadExit(self): self.__exit = True


class Score():
	def __init__(self, score = 0):
		self.score = score
	def up(self, change):
		self.score += change
	def down(self, change):
		self.score -= change

class ScoreDisplayHandler(Score):
	def whenEvent(self):
		pass

class Skin():
	def __init__(self):
		skinDic = {}
		skin = {"head" : None, "body" : None , "tail" : None}
		skinList["skin"] = skin
	def getSkin(self, skinName):
		return skinDic["skin"]
	def getSkinDic(self):
		return skinDic


class Observer():
	def observeUpdate(self):
		raise NotImplementedError( "Should have implemented update %s" % self )

class Snake():
	def __init__(self, snakeID, speed, thick, skinName = None, firstHeadDirection = RIGHT, headPos = SCREEN_MID, color = GREEN, length = 1,):
		self.snakeID = snakeID
		self.color = color
		self.speed = speed
		self.thick = thick
		self.length = length
		self.snakeList = [(headPos[posX],headPos[posY],firstHeadDirection)]
		self.setOfObserver = set()
		#img
		if skinName != None:
			skin = Skin.getSkin(skinName)
			self.headImg = skin["head"]
			self.bodyImg = skin["body"]
			self.tailImg = skin["tail"]

	# def update(self, newHeadPos):
	# 	self.snake_list.append(newHeadPos)
	# 	if len(self.snake_list) > self.length:
	# 		del self.snake_list[0]
	def addLength(self, length = 1):
		self.length += length
		# self.snakeList.append((snakeList[-1]))
		notify()
	def addSpeed(self, speed):
		self.speed += speed
		notify()
	def getState(self):
		snakeState = {}
		snakeState["snakeID"] = self.snakeID
		snakeState["color"] = self.color
		snakeState["speed"] = self.speed
		snakeState["thick"] = self.thick
		snakeState["length"] = length
		snakeState["snakeList"] = self.snakeList
		return snakeState
	def setState(self, snakeState):
		self.color = snakeState["color"]
		self.speed = snakeState["speed"]
		self.thick = snakeState["thick"]
		self.length = snakeState["length"]
		self.snakeList = snakeState["snakeList"]
	def getImg(self):
		snakeImg = {}
		snakeImg["head"] = self.headImg
		snakeImg["body"] = self.bodyImg
		snakeImg["tail"] = self.tailImg

	# def getcolor(self): return self.color
	# def getLength(self): return self.length
	# def getSpeed(self): return self.speed
	def getSnakeState(self):
		return snakeState
	def attach(self, observer):
		self.setOfObserver.add(observer)
	def dettach(self, observer):
		self.setOfObserver.remove(observer)
	def notify():
		for observer in setOfObserver:
			observer.observeUpdate()

class SnakeStateHandler(Observer):
	def __init__(self, snake):
		snake.attach(self)
		self.snakeState = snake.getState()
	def observeUpdate(self):
		self.snakeState = snake.getState()
	def commit(self):
		snake.setState(self.snakeState)
	def move(self, newHeadPos, direction):
		self.snakeState["snakeList"].append((newHeadPos[POS_X],newHeadPos[POS_Y],direction))
		if len(self.snakeState["snakeList"]) > self.snakeState["length"]:
			del self.snakeState["snakeList"][0]
		self.commit()

class SnakeDisplayControler(Observer):
	def __init__(self, snake):
		snake.attach(self)
		self.snakeState = snake.getState()
		self.color = self.snakeState["color"]
		self.thick = self.snakeState["thick"]
		self.snakeList = self.snakeState["snakeList"]
		self.snakeImg = snake.getImg()
		self.headImg = self.snakeImg["head"]
		self.bodyImg = self.snakeImg["body"]
		self.tailImg = self.snakeImg["tail"]

	def observeUpdate(self):
		self.snakeState = snake.getState()
		self.color = self.snakeState["color"]
		self.thick = self.snakeState["thick"]
		self.snakeList = self.snakeState["snakeList"]

	def update(self):
		self.headClone = pygame.transform.rotate(self.headImg, 90 * self.snakeList[SNAKE_HEAD][DIRECTION])
		self.tailClone = pygame.transform.rotate(self.tailImg, 90 * self.snakeList[SNAKE_TAIL][DIRECTION])
		if self.bodyImg != None:
			self.bodyClone = pygame.transform.rotate(self.bodyImg, 90 * direction)

	def draw(self, screen):
		screen.blit(self.headClone, (self.snakeList[SNAKE_HEAD][POS_X],self.snakeList[SNAKE_HEAD][POS_Y]))
		screen.blit(self.tailClone, (self.snakeList[SNAKE_TAIL][POS_X],self.snakeList[SNAKE_TAIL][POS_Y]))

		if self.bodyImg == None: 
			for posX, posY, direction in snakeList[1:-1]:
				pygame.draw.rect(screen, color, [posX, posY, self.thick, self.thick])
		else:
			for posX, posY, direction in snakeList[1:-1]:
				screen.blit(self.bodyClone, (posX, posY))

# pygame.sprite.Sprite
class Item(pygame.sprite.Sprite):
	def __init__(self, form, lifeTimer = CONTINUANCE, form_type = "img"):
		pygame.sprite.Sprite.__init__(self)
		self.type = form_type # "img" / "color"
		self.form = form
		self.lifeTimer = lifeTimer
	def display(self, location):
		pass
	def effect(self):
		raise NotImplementedError( "Should have implemented update %s" % self )
	def update(self):
		if not (self.lifeTimer == -1):
			if not self.lifeTimer:
				self.kill()

			self.lifeTimer -= 1


class Apple(Item):
	def __init__(self):
		# appleImg = 
		Item.__init__(self, appleImg, CONTINUANCE)

	def effect(self,score):
		point = 100
		score.up(100)


class GamePlay():
	def display_intro():
		pass
	def player1_highscore_gameloop():
		pass
	def player2_highscore_gameloop():
		pass
	def player2_compete_gameloop():
		pass
# if __name__ == '__main__':
	# pass