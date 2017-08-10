import os
import platform
import random
import threading
import time

import mainForTraining
from train.env import Environment


class Gym(object):
    def make(self, gameName, *args, **kwargs):
        server_address = ''
        if platform.system() == "Windows":
            server_address = ('localhost', random.randrange(2000,4000))
        elif platform.system() == "Linux":
            server_address = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/socket_address/socket_%s'% random.randrange(0,2000)))
        gameThread = threading.Thread(target = mainForTraining.main, args = (server_address, ))
        gameThread.daemon = True
        gameThread.start()
        time.sleep(0.1)
        return Environment(server_address)
