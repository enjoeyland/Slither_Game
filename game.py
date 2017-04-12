import snake
import snakeDisplayHandler
import snakeStateHandler
import event

class Game():
	def display_intro(self):
		return 0
	def player1_highScore_gameLoop(self):
		defaultSpeed = 10
		defaultThick = 20

		player = snake.Snake(1, defaultSpeed, defaultThick)
		snakeStateHandler.SnakeStateHandler(player, event.KeyboardEventHandler)
		snakeDisplayHandler.SnakeDisplayHandler(player)
	def player2_highScore_gameLoop(self):
		pass
	def player2_compete_gameLoop(self):
		pass