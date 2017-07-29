from utils.listener import Request
from utils.setting import CRASH_ITEM, APPLE


class CrashItemEventHandler:
    def __init__(self, pygameEventDistributor,    screen, score):
        self.pygameEventDistributor = pygameEventDistributor
        self.request = Request("CrashItemEventHandler", self.process, addtionalTarget = CRASH_ITEM)
        self.pygameEventDistributor.listen(self.request)

        self.screen = screen
        self.score = score

    def process(self, data):
        if data.item.type == APPLE:
            data.item.effect(self.screen, self.score, data.snake)