import pygame

from train import train_utility
from utils.socketClass import SocketClient


class Environment(object):
    def __init__(self, server_address):
        self.action_space = ActionSpace()
        self.env = Env()
        self._sock = SocketClient()
        self._sock.connect(server_address)

    def step(self, action):
        # print("action : " + str(action))
        self._sock.send(str(action))
        return train_utility.renderTrainer2EnvMsg(self._sock.receive())

    def reset(self):
        self._sock.send("restart")
        return train_utility.renderTrainer2EnvMsgReset(self._sock.receive())

    def render(self):
        pygame.display.update()

class ActionSpace:
    def __init__(self):
        # self.n = 4
        self.n = 5

class Env:
    def __init__(self):
        # self.action_meaning = ["LEFT","DOWN","RIGHT","UP"]
        self.action_meaning = ["NO_OPERATION","LEFT","DOWN","RIGHT","UP"]

    def get_action_meanings(self):
        return self.action_meaning