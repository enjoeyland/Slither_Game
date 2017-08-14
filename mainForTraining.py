#-*- coding: utf-8 -*-
import os

import pygame
import sys

from gameStates import train_player1HighScore
from utils import utility
from utils.setting import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER1_HIGH_SCORE, EXIT
from utils.socketClass import SocketServerForOneClient


def main(server_address):
	# pygame init
	pygame.mixer.pre_init(44100, -16, 2, 2048)
	pygame.init()
	pygame.mixer.init()

	if os.path.split(os.path.abspath(sys.argv[0]))[1] == "eval.py":
		screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	else:
		# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
		screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

	# Load Image
	appleImg = utility.loadImageByPil("apple")

	sock = SocketServerForOneClient(server_address)
	sock.accept()
	if b'restart' == sock.receive():
		state = PLAYER1_HIGH_SCORE
		while True:
			if state == PLAYER1_HIGH_SCORE:
				state = train_player1HighScore.TrainPlayer1HighScore(screen, sock, appleImg).process()
			elif state == EXIT:
				break

if __name__ == "__main__":
	main(('localhost',3490))