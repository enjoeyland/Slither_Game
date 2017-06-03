from event.eventCreators import eventCreator
from utils.setting import ON_TICK


class TickEventCreator(eventCreator.EventCreator):
	def onTick(self):
		self.createEvent(ON_TICK)