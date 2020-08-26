from threading import Thread
from typing import Callable
from Exceptions.CallbackNotInitializedException import CallbackNotInitializedException


class TriggerBase(Thread):
    __callback__ = None  # type: Callable[[], None]

    def register_callback(self, callback: Callable[[None], None]):
        self.__callback__ = callback

    def trigger(self):
        if self.__callback__ is None:
            raise CallbackNotInitializedException()
        self.__callback__()

    def run(self):
        pass
