import platform
import random
import mainForTraining
from train.env import Environment


class Gym(object):
    def make(self, gameName, *args, **kwargs):
        server_address = ''
        if platform.system() == "Windows":
            server_address = ('localhost', random.randrange(2000,4000))
        elif platform.system() == "Linux":
            server_address = '/data/socket_address/socket_%s'% random.randrange(0,2000)
        mainForTraining.main(server_address)
        return Environment(server_address)
