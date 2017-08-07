import json

from event.eventCreators.arrowKeyEventCreator import ArrowKeyEventCreator
from utils.setting import LEFT, RIGHT, DOWN, UP


def actionExecute(action):
    if action == LEFT:
        ArrowKeyEventCreator().onKeyLeft()
    if action == RIGHT:
        ArrowKeyEventCreator().onKeyRight()
    if action == DOWN:
        ArrowKeyEventCreator().onKeyDown()
    if action == UP:
        ArrowKeyEventCreator().onKeyUp()

def renderTrainer2EnvMsg(msg):
    msgStr = msg.decode("utf-8")
    result = json.loads(msgStr)
    return result["image"], result["reward"], result["done"], result["info"]

def renderEnv2TrainerMsg(msg):
    action = int.from_bytes(msg, byteorder='big')
    return action

def renderTrainer2EnvMsgReset(msg):
    msgStr = msg.decode("utf-8")
    result = json.loads(msgStr)
    return result["image"]