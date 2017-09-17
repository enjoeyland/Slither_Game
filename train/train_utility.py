import json
import numpy

from utils.setting import LEFT, RIGHT, DOWN, UP, SNAKE_HEAD, POS_X, DIRECTION, POS_Y, SNAKE_RIGHT_AFTER_HEAD


def actionExecute(ArrowKeyEventCreator, action):
    if action == LEFT:
        ArrowKeyEventCreator.onKeyLeft()
    elif action == RIGHT:
        ArrowKeyEventCreator.onKeyRight()
    elif action == DOWN:
        ArrowKeyEventCreator.onKeyDown()
    elif action == UP:
        ArrowKeyEventCreator.onKeyUp()
    else: pass

def renderTrainer2EnvMsg(msg):
    msgStr = msg.decode("utf-8")
    result = json.loads(msgStr)
    image = numpy.asarray(result["image"])
    # image = result["image"]
    return image, result["reward"], result["done"], result["info"]

def renderEnv2TrainerMsg(msg):
    action = int(msg.decode("utf-8"))
    # print("tranformed action : " + str(action))
    return action

def renderTrainer2EnvMsgReset(msg):
    msgStr = msg.decode("utf-8")
    result = json.loads(msgStr)
    image = numpy.asarray(result["image"])
    # image = result["image"]
    return image

def getDirectionTowardItemReward(snake, groupItem):
    positiveReward = 0
    negativeReward = -0.01
    snakeHead = snake.snakeList[SNAKE_HEAD]
    snakeHeadDirection = snakeHead[DIRECTION]
    for item in groupItem.sprites():
        if snakeHeadDirection == RIGHT:
            if snakeHead[POS_X] - item.location[POS_X] <= 0:
                return positiveReward
        elif snakeHeadDirection == LEFT:
            if snakeHead[POS_X] - item.location[POS_X] > 0:
                return positiveReward
        elif snakeHeadDirection == UP:
            if snakeHead[POS_Y] - item.location[POS_Y] >= 0:
                return positiveReward
        elif snakeHeadDirection == DOWN:
            if snakeHead[POS_Y] - item.location[POS_Y] < 0:
                return positiveReward
    else:
        return negativeReward

def getGoOppositeDirectionReward(snake):
    positiveReward = 0
    negativeReward = -0.1
    isOppositeDirection = abs(snake.snakeList[SNAKE_HEAD][DIRECTION] - snake.snakeList[SNAKE_RIGHT_AFTER_HEAD][DIRECTION]) == 2
    if isOppositeDirection:
        return negativeReward
    else:
        return positiveReward
