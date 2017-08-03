from utils import listener
from utils.listener import Request
from utils.setting import ON_TICK


class TickEventHandler(listener.ListenerHandler, object):
    def __init__(self, pygameEventDistributor):
        super().__init__()
        self.pygameEventDistributor = pygameEventDistributor
        self.request = Request("TickEventHandler", self.process, description= "handle tick event")
        self.request.setAddtionalTarget(ON_TICK)
        self.pygameEventDistributor.listen(self.request)

    def process(self, data):
        self._notify()