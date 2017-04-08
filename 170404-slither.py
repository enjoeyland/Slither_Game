import pygame, threading
pygame.init()

#value
#game
DISPLAY_HEIGHT = 600
DISPLAY_WIDTH = 800
DISPLAY_MID = (DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2)
FRAMERATE = 20

#direction
LEFT = 1
DOWN = 2
RIGHT = 3
UP = 4

#color
green = (0,255,0)

#snake
SNAKE_HEAD = -1
SNAKE_TAIL = 0
POS_X = 0
POS_Y = 1
DIRECTION = 2

#skin
SKIN_HEAD = 0
SNAKE_BODY = 1
SNAKE_TAIL = 2

#img
# icon = pygame.image.load('apple.png')

#sound
# fire_sound=pygame.mixer.Sound("fire.wav")
	# pygame.mixer.Sound.play(fire_sound)


clock=pygame.time.Clock()

		# pygame.display.update()
		# clock.tick(FP)
#magnification #배울


class GameSetting():
	def __init__(self):
		self.screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))#surface화면
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
		pass
	def getSkin(self, skinNum):
		skin = {"head" : None, "body" : None , "tail" : None}
		return skin


class Observer():
	def update(self):
		raise NotImplementedError( "Should have implemented update %s" % self )

class Snake():
	def __init__(self, snakeID, speed, thick, skinNum = None, firstHeadDirection = RIGHT, headPos = DISPLAY_MID, color = green, length = 1,):
		self.snakeID = snakeID
		self.color = color
		self.speed = speed
		self.thick = thick
		self.length = length
		self.snakeList = [(headPos[posX],headPos[posY],firstHeadDirection)]
		self.setOfObserver = set()
		#img
		if skinNum != None:
			skin = Skin.getSkin(skinNum)
			self.head_img = skin["head"]
			self.body_img = skin["body"]
			self.tail_img = skin["tail"]

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
		snakeImg["head"] = self.head_img
		snakeImg["body"] = self.body_img
		snakeImg["tail"] = self.tail_img

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
			observer.update()

class SnakeStateHandler(Observer):
	def __init__(self, snake):
		snake.attach(self)
		self.snakeState = snake.getState()
	def update(self):
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
		self.head_img = self.snakeImg["head"]
		self.body_img = self.snakeImg["body"]
		self.tail_img = self.snakeImg["tail"]
	def update(self):
		self.snakeState = snake.getState()
		self.color = self.snakeState["color"]
		self.thick = self.snakeState["thick"]
		self.snakeList = self.snakeState["snakeList"]

	def draw(self):
		#img rotate
		head = pygame.transform.rotate(self.head_img, 90 * self.snakeList[SNAKE_HEAD][DIRECTION])
		Screen.screen.blit(head, (self.snakeList[SNAKE_HEAD][POS_X],self.snakeList[SNAKE_HEAD][POS_Y]))
		tail = pygame.transform.rotate(self.tail_img, 90 * self.snakeList[SNAKE_TAIL][DIRECTION])
		Screen.screen.blit(tail, (self.snakeList[SNAKE_TAIL][POS_X],self.snakeList[SNAKE_TAIL][POS_Y]))

		if self.body_img == None: 
			for posX, posY, direction in snakeList[1:-1]:
				pygame.draw.rect(Screen.screen, color, [posX, posY, self.thick, self.thick])
		else:
			for posX, posY, direction in snakeList[1:-1]:
				skin = pygame.transform.rotate(self.body_img, 90 * direction)
				Screen.screen.blit(skin, (posX, posY))

# pygame.sprite.Sprite
class Item():
	def __init__(self, form, duration = -1, form_type = "img"):
		self.type = form_type # "img" / "color"
		self.form = form
		self.duration = duration
	def display(self, location):
		pass
	def effect(self):
		raise NotImplementedError( "Should have implemented update %s" % self )

class Apple(Item):
	def __init__(self):
		# appleImg = 
		Item.__init__(self, appleImg, -1)
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
print ("hello")