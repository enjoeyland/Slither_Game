"""default values"""
import pygame
import sys
import os


"""Base Values"""
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
PINK = (255, 102, 204)
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

"""Sound"""
PLAY_ONE_TIME = 0
PLAY_INFINITELY = -1
SOUND_LIST = ["Apple_Bite", "BGM"]

"""Wall"""
SIDE_WALL_SIZE = (0, 0)

"""Screen"""
_executor = os.path.split(os.path.abspath(sys.argv[0]))[1]
if _executor == "training.py":
	SCREEN_SCALE = 1
	FRAMES_PER_SECOND = 10.0
elif _executor == "eval.py":
	SCREEN_SCALE = 5
	FRAMES_PER_SECOND = 10.0
else:
	SCREEN_SCALE = 10
	FRAMES_PER_SECOND = 200.0

FULL_SCREEN = False
SCREEN_WIDTH = 80 * SCREEN_SCALE
SCREEN_HEIGHT = 60 * SCREEN_SCALE
# SCORE_BAR_HEIGHT = int(2 * (10/SCREEN_SCALE + 3))

SPRITE_OFFSET = ((SIDE_WALL_SIZE[POS_X], SCREEN_WIDTH - SIDE_WALL_SIZE[POS_X]) ,(SIDE_WALL_SIZE[POS_Y], SCREEN_HEIGHT - SIDE_WALL_SIZE[POS_Y]))
SCREEN_MID = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)


ITEM_MARGIN = 2 * SCREEN_SCALE
ANTI_ALIAS = True

"""Text"""
if _executor == "training.py":
	DEFAULT_FONT_SIZE = 0
else:
	DEFAULT_FONT_SIZE = 2 * SCREEN_SCALE

DEFAULT_FONT_TYPE = "comicsansms"

"""Snake"""
SNAKE_HEAD = -1
SNAKE_TAIL = 0
DIRECTION = 2

DEFAULT_SPEED = 60 * SCREEN_SCALE
DEFAULT_THICK = 2 * SCREEN_SCALE

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
DEFAULT_ITEM_SIZE = (3 * SCREEN_SCALE, 3 * SCREEN_SCALE)
ITEM_LIST = ["apple"]
APPLE = 0

"""User Event"""
ON_TICK = pygame.USEREVENT + 1
CRASH_WALL = pygame.USEREVENT + 2
CRASH_ITEM = pygame.USEREVENT + 3
CRASH_ITSELF = pygame.USEREVENT + 4
CRASH_OTHER_SNAKE = pygame.USEREVENT + 5

"""Files"""
READ = "r"
WRITE = "w"
APPEND = "a"

"""Game State"""
EXIT = -1
INTRO = 0
PLAYER1_HIGH_SCORE = 1
PLAYER2_HIGH_SCORE = 2
PLAYER2_COMPETE = 3

"""Eevnt to listen list for each game state"""
P1_HIGH_SCORE_LISTENING_EVENT = [pygame.QUIT, pygame.KEYDOWN, ON_TICK, CRASH_WALL, CRASH_ITEM, CRASH_ITSELF]
P2_HIGH_SCORE_LISTENING_EVENT = [pygame.QUIT, pygame.KEYDOWN, ON_TICK, CRASH_WALL, CRASH_ITEM, CRASH_OTHER_SNAKE]
P2_COMPETE_LISTENING_EVENT = [pygame.QUIT, pygame.KEYDOWN, ON_TICK, CRASH_WALL, CRASH_ITEM, CRASH_OTHER_SNAKE]


"""Level"""
LEVEL_0 = 0
LEVEL_1 = 1
LEVEL_2 = 2
LEVEL_3 = 3
LEVEL_4 = 4
LEVEL_5 = 5
LEVEL_6 = 6
LEVEL_7 = 7
LEVEL_8 = 8
MAX_LEVEL = "max level"
LEVEL = {PLAYER1_HIGH_SCORE :
			{LEVEL_0 : {"level": 0,
						"score": 0,
						"setting": {"snake": {"speed": 20 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
									"item": {"apple": {"num" : 8, "probability": FRAMES_PER_SECOND,"lifeTimer": CONTINUANCE}}
									}
						},
			# LEVEL_1 : {"level": 1,
			# 		   "score": 500,
			# 		   "setting": {"snake": {"speed": 40 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
			# 					   "item": {"apple": {"num" : 2, "probability": 80,"lifeTimer": CONTINUANCE}}
			# 					   }
			# 		   },
			# LEVEL_2 : {"level": 2,
			# 		   "score": 1500,
			# 		   "setting": {"snake": {"speed": 60 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
			# 					   "item": {"apple": {"num" : 2, "probability": 30,"lifeTimer": CONTINUANCE}}
			# 					   }
			# 		   },
			# LEVEL_3 : {"level": 3,
			# 		   "score": 3000,
			# 		   "setting": {"snake": {"speed": 70 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
			# 					   "item": {"apple": {"num" : 3, "probability": 10,"lifeTimer": 4 * FRAMES_PER_SECOND}}
			# 					   }
			# 		   },
			# LEVEL_4 : {"level": 4,
			# 		   "score": 4500,
			# 		   "setting": {"snake": {"speed": 80 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
			# 					   "item": {"apple": {"num" : 4, "probability": 5,"lifeTimer": 2 * FRAMES_PER_SECOND}}
			# 					   }
			# 		   },
			# LEVEL_5 : {"level": 5,
			# 		   "score": 6000,
			# 		   "setting": {"snake": {"speed": 90 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
			# 					   "item": {"apple": {"num" : 3, "probability": 3,"lifeTimer": 1 * FRAMES_PER_SECOND}}
			# 					   }
			# 		   },
			# LEVEL_6 : {"level": 6,
			# 		   "score": 7500,
			# 		   "setting": {"snake": {"speed": 100 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
			# 					   "item": {"apple": {"num" : 6, "probability": 10,"lifeTimer": 0.1 * FRAMES_PER_SECOND}}
			# 					   }
			# 		   },
			# LEVEL_7 :  {"level": 7,
			# 			"score": 10000,
			# 			"setting": {"snake": {"speed": 110 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
			# 						"item": {"apple": {"num" : 4, "probability": 0.5,"lifeTimer": 0.5 * FRAMES_PER_SECOND}}
			# 						}
			# 			},
			# LEVEL_8 :  {"level": 8,
			# 			"score": 12000,
			# 			"setting": {"snake": {"speed": 115 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
			# 						"item": {"apple": {"num" : 3, "probability": 0.6,"lifeTimer": 0.5 * FRAMES_PER_SECOND}}
			# 						}
			# 			},
			# MAX_LEVEL : {"level": 8,
			# 			 "score": 12000,
			# 			 "setting": {"snake": {"speed": 115 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
			# 						 "item": {"apple": {"num" : 3, "probability": 0.6,"lifeTimer": 0.5 * FRAMES_PER_SECOND}}
			# 						 }
			# 			 }
			MAX_LEVEL : {"level": 0,
						 "score": 0,
						 "setting": {"snake": {"speed": 20 * SCREEN_SCALE, "thick" : 2 * SCREEN_SCALE},
									 "item": {"apple": {"num" : 8, "probability": FRAMES_PER_SECOND,"lifeTimer": CONTINUANCE }}
									 }
						 }
			},
		PLAYER2_HIGH_SCORE : {},
		PLAYER2_COMPETE : {}}
