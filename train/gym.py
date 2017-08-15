import os
import platform
import random
import threading
import time
from itertools import count

import mainForTraining
from train.env import Environment


class Gym(object):
    _ids = count(1)
    def make(self, gameName, *args, **kwargs):
        self._id = next(self._ids)
        server_address = ''
        if platform.system() == "Windows":
            server_address = ('localhost', 3000 + self._id)
        elif platform.system() == "Linux":
            server_address = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'data/socket_address/socket_%s'% random.randint(0,10) * 100 + self._id))
        gameThread = threading.Thread(name = ("SlitherGame%s" % self._id), target = mainForTraining.main, args = (server_address, ))
        gameThread.daemon = True
        gameThread.start()
        time.sleep(0.1)
        return Environment(server_address)
