from typing import Callable

from Exceptions.CallbackNotInitializedException import CallbackNotInitializedException


class TriggerBase:
    __callback__ = None  # type: Callable[[None], None]

    def register_callback(self, callback: Callable[[None], None]):
        self.__callback__ = callback

    def trigger(self):
        if self.__callback__ is None:
            raise CallbackNotInitializedException()
        self.__callback__()

    def run(self):
        pass
