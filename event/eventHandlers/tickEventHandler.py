from utils import listener
from utils.setting import ON_TICK


class TickEventHandler(listener.ListenerHandler, object):
    def __init__(self, pygameEventDistributor):
        listener.ListenerHandler.__init__(self)
        self.pygameEventDistributor = pygameEventDistributor
        self.request = listener.Request("TickEventHandler", self.process, description= "handle tick event")
        self.request.setAddtionalTarget(ON_TICK)
        self.pygameEventDistributor.listen(self.request)

    def process(self):
        self.notify()