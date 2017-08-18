import queue


# class Event:
#     def __init__(self, event_type, event_dict=None, **attributes):
#         self.type = event_type
#         if event_dict:
#             for key, value in event_dict.items():
#                 setattr(self, key, value)
#         for key, value in attributes.items():
#             setattr(self, key, value)
#
#         self.dict = self.__dict__


class EventQueue(queue.Queue):
    def __init__(self, maxSize = 1024):
        super().__init__(maxSize)

    def get_all(self):
        items = []
        while True:
            try:
                items.append(self.get_nowait())
            except queue.Empty:
                break
        return items