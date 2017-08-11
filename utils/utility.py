import os
import pygame
from PIL import Image

from event.eventCreators.arrowKeyEventCreator import ArrowKeyEventCreator
from utils.setting import POS_X, POS_Y, LEFT, RIGHT, DOWN, UP

"""Img"""
# pygame.transform.scale(Surface, (width, height), DestSurface = None)
# icon = pygame.image.load('apple.png')


"""Sound"""
# fire_sound=pygame.mixer.Sound("fire.wav")
# pygame.mixer.Sound.play(fire_sound)

soundActive = True


def getPath():
    pathname = os.path.dirname(os.path.abspath(__file__))
    return pathname

def loadImage(name):
    imageTypeList = [".bzi", ".png", ".jpg"]
    for imageType in imageTypeList:
        filePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "data/images/", name + imageType))

        if os.path.isfile(filePath):
            return pygame.image.load(filePath).convert_alpha()

    print ("Failed to load image: %s" % name)
    return None

def loadImageByPil(name):
    imageTypeList = [".bzi", ".png", ".jpg"]
    for imageType in imageTypeList:
        filePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "data/images/", name + imageType))

        if os.path.isfile(filePath):
            img = Image.open(filePath)
            img = img.convert("RGBA")
            return pygame.image.fromstring(img.tobytes(), img.size, img.mode)
    print ("Failed to load image: %s" % name)
    return None

def resizeImage(image, size):
    if image is None:
        return None
    try:
        resizedImg = pygame.transform.smoothscale(image, size)
    except:
        try:
            resizedImg = pygame.transform.scale(image, size)
        except:
            resizedImg = image
            print("fall image resize : %s" % image)
    return resizedImg

# def setImageBackgroundColor(image, backgroundColor):
# 	surface = pygame.Surface(image.get_rect().size)
# 	surface.fill(backgroundColor)
# 	surface.blit(image, (0,0))
# 	return surface

def loadSound(name):
    soundTypeList = [".bza", ".ogg", ".mp3", ".wav"]
    for soundType in soundTypeList:
        filePath = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', "data/sounds/", name + soundType))

        if os.path.isfile(filePath):
            return pygame.mixer.Sound(filePath)

    print ("Failed to load sound: %s" % name)
    return None

def playSound(sound, channelNumber = None, loops = 0):
    sound.play(loops = loops)

# def playMusic(music, forceNext = True):
# 	if settingList[MUSIC] and soundActive:
# 		if forceNext:
# 			pygame.mixer.Channel(MUSIC_CHANNEL).queue(music)
# 		elif not pygame.mixer.Channel(MUSIC_CHANNEL).get_queue():
# 			pygame.mixer.Channel(MUSIC_CHANNEL).queue(music)

def executeFunction(func, name = "", *args, **kwargs):
    try:
        func(*args, **kwargs)
    except TypeError:
        print("error occurs : %s" % name)
        raise

# class ExecuteFunctionError(Exception):





