import os
import pygame

"""Img"""
# pygame.transform.scale(Surface, (width, height), DestSurface = None)
icon = pygame.image.load('apple.png')


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
		filePath = os.path.join("data/images/", name, imageType)
		if os.path.isfile(filePath):
			return pygame.image.load(filePath).convert_alpha()

	print ("Failed to load image: %s" % name)
	return None

def loadSound(name):
	soundTypeList = ["bza", ".ogg", ".mp3"]
	for soundType in soundTypeList:
		filePath = os.path.join("data/sounds/", name, soundType)
		if os.path.isfile(filePath):
			return pygame.mixer.Sound(filePath)

	print ("Failed to load sound: %s" % name)
	return None

# def playSound(sound, channelNumber = None):
# 	if settingList[SFX] and soundActive:
# 		if channelNumber:
# 			pygame.mixer.Channel(channelNumber).play(sound)
# 		else:
# 			sound.play()

# def playMusic(music, forceNext = True):
# 	if settingList[MUSIC] and soundActive:
# 		if forceNext:
# 			pygame.mixer.Channel(MUSIC_CHANNEL).queue(music)
# 		elif not pygame.mixer.Channel(MUSIC_CHANNEL).get_queue():
# 			pygame.mixer.Channel(MUSIC_CHANNEL).queue(music)

def readHighScores():
	scoreList = []
	try:
		scoreFile = open(getPath() + "/score.bzd",'r')
		scoreList.append(int(scoreFile.readline()))
		scoreList.append(int(scoreFile.readline()))
		scoreList.append(int(scoreFile.readline()))
		scoreList.append(int(scoreFile.readline()))
		scoreFile.close()

		return scoreList

	except:
		scoreFile = open(getPath() + "/score.bzd",'w')
		scoreFile.write(str(0) + '\n')
		scoreFile.write(str(0) + '\n')
		scoreFile.write(str(0) + '\n')
		scoreFile.write(str(0) + '\n')
		scoreFile.close()

		return [0,0,0,0]

def writeHighScores(arg):
	scoreFile = open(getPath() + "/score.bzd",'w')
	tutorial = arg[0]
	world1 = arg[1]
	world2 = arg[2]
	world3 = arg[3]
	scoreFile.write(str(tutorial) + '\n')
	scoreFile.write(str(world1) + '\n')
	scoreFile.write(str(world2) + '\n')
	scoreFile.write(str(world3) + '\n')
	scoreFile.close()
