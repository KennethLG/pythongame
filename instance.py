from abc import ABC, abstractmethod

from drawable import Drawable


class Instance(Drawable, ABC):
    def __init__(self):
        self.x = 100
        self.y = 100

    @abstractmethod
    def handle_event(self, event_name, event):
        pass
