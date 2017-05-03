"""default values"""
import pygame


""""Base"""
POS_X = 0
POS_Y = 1
BEGIN = 0
END = -1
YES = 1
NO = 0


"""Direction"""
LEFT = 1
DOWN = 2
RIGHT = 3
UP = 4

"""Color"""
BLACK = (0, 0, 0)
WHITE = (255,255,255)
RED = (255, 0, 0)
GREEN = (0,255,0)
DARK_GREEN = (0,100,0)
BLUE = (0, 0, 255)
SCREEN_BACKGROUND = (100,200,255)

"""Font alignment enumerations""" # alignment : 정렬
TOP_LEFT = 0
TOP_MIDDLE = 1
TOP_RIGHT = 2
CENTER_LEFT = 3
CENTER_MIDDLE = 4
CENTER_RIGHT = 5
BOTTOM_LEFT = 6
BOTTOM_MIDDLE = 7
BOTTOM_RIGHT = 8

"""Snake"""
SNAKE_HEAD = -1
SNAKE_TAIL = 0
DIRECTION = 2

DEFAULT_SPEED = 600
DEFAULT_THICK = 20

"""Skin"""
SKIN_HEAD = 0
SKIN_BODY = 1
SKIN_TAIL = 2
SKIN_FIRST = 3
SKIN_CURVE = 4

"""Skin Name"""
SKIN_DEFAULT = 0
FIRST_SKIN = 1


"""Item"""
CONTINUANCE = -1
# DEFAULT_ITEM_SIZE = defaultThick
DEFAULT_ITEM_SIZE = 30
ITEM_LIST = ["apple"]
APPLE = 0

"""User Event"""
ON_TICK = pygame.USEREVENT + 1
CRASH_WALL = pygame.USEREVENT + 2
CRASH_ITEM = pygame.USEREVENT + 3
CRASH_ITSELF = pygame.USEREVENT + 4
CRASH_OTHER_SNAKE = pygame.USEREVENT + 5


"""Screen"""
WALL_TICK = 0
FULL_SCREEN = True
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_MID = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
SPRITE_OFFSET = ((WALL_TICK, SCREEN_WIDTH - WALL_TICK) ,(WALL_TICK, SCREEN_HEIGHT - WALL_TICK))

ITEM_MARGIN = 20
ANTI_ALIAS = True

FRAMES_PER_SECOND = 200.0
SCREEN_AUTO_UPDATE = True

DEFAULT_FONT_SIZE = 20
DEFAULT_FONT_TYPE = "comicsansms"

"""Files"""
READ = "r"
WRITE = "w"
APPEND = "a"

"""game name"""
PLAYER1_HIGH_SCORE = 0
PLAYER2_HIGH_SCORE = 1
PLAYER2_COMPETE = 2

"""Level"""
LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3
LEVEL_4 = 4
LEVEL_5 = 5
LEVEL_6 = 6
LEVEL_7 = 7
MAX_LEVEL = "max level"
LEVEL = {PLAYER1_HIGH_SCORE :
			{LEVEL_0 : {"level": 0,
						"score": 0,
						"setting": {"snake": {"speed": 300, "thick" : 20},
									"item": {"apple": {"num" : 2, "probability": FRAMES_PER_SECOND,"lifeTimer": CONTINUANCE}}
									}
						},
			LEVEL_1 : {"level": 1,
					   "score": 500,
					   "setting": {"snake": {"speed": 500, "thick" : 20},
								   "item": {"apple": {"num" : 2, "probability": 80,"lifeTimer": CONTINUANCE}}
								   }
					   },
			LEVEL_2 : {"level": 2,
					   "score": 1500,
					   "setting": {"snake": {"speed": 600, "thick" : 20},
								   "item": {"apple": {"num" : 2, "probability": 30,"lifeTimer": CONTINUANCE}}
								   }
					   },
			LEVEL_3 : {"level": 3,
					   "score": 3000,
					   "setting": {"snake": {"speed": 700, "thick" : 20},
								   "item": {"apple": {"num" : 2, "probability": 10,"lifeTimer": 4 * FRAMES_PER_SECOND}}
								   }
					   },
			LEVEL_4 : {"level": 4,
					   "score": 4500,
					   "setting": {"snake": {"speed": 800, "thick" : 20},
								   "item": {"apple": {"num" : 2, "probability": 8,"lifeTimer": 3 * FRAMES_PER_SECOND}}
								   }
					   },
			LEVEL_5 : {"level": 5,
					   "score": 6000,
					   "setting": {"snake": {"speed": 900, "thick" : 20},
								   "item": {"apple": {"num" : 1, "probability": 3,"lifeTimer": 2 * FRAMES_PER_SECOND}}
								   }
					   },
			LEVEL_6 : {"level": 6,
					   "score": 7500,
					   "setting": {"snake": {"speed": 1000, "thick" : 20},
								   "item": {"apple": {"num" : 2, "probability": 5,"lifeTimer": 1.3 * FRAMES_PER_SECOND}}
								   }
					   },
			LEVEL_7 :  {"level": 7,
						"score": 10000,
						"setting": {"snake": {"speed": 1100, "thick" : 20},
									"item": {"apple": {"num" : 3, "probability": 3,"lifeTimer": 0.5 * FRAMES_PER_SECOND}}
									}
						},
			MAX_LEVEL : {"level": 7,
						 "score": 10000,
						 "setting": {"snake": {"speed": 1100, "thick" : 20},
									 "item": {"apple": {"num" : 3, "probability": 3,"lifeTimer": 0.5 * FRAMES_PER_SECOND}}
									 }
						 }},
		PLAYER2_HIGH_SCORE : {},
		PLAYER2_COMPETE : {}}
