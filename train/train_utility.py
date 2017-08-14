import json

import numpy

from event.eventCreators.arrowKeyEventCreator import ArrowKeyEventCreator
from utils.setting import LEFT, RIGHT, DOWN, UP


def actionExecute(action):
    if action == LEFT:
        ArrowKeyEventCreator().onKeyLeft()
    elif action == RIGHT:
        ArrowKeyEventCreator().onKeyRight()
    elif action == DOWN:
        ArrowKeyEventCreator().onKeyDown()
    elif action == UP:
        ArrowKeyEventCreator().onKeyUp()
    else: pass

def renderTrainer2EnvMsg(msg):
    msgStr = msg.decode("utf-8")
    result = json.loads(msgStr)
    image = numpy.asarray(result["image"])
    return image, result["reward"], result["done"], result["info"]

def renderEnv2TrainerMsg(msg):
    action = int(msg.decode("utf-8"))
    # print("tranformed action : " + str(action))
    return action

def renderTrainer2EnvMsgReset(msg):
    msgStr = msg.decode("utf-8")
    result = json.loads(msgStr)
    image = numpy.asarray(result["image"])
    return image