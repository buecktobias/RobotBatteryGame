import abc


class Controllable(abc.ABC):
    def on_event(self, event):
        pass