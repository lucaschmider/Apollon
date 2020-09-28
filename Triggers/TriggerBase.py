from threading import Thread
from typing import Callable
from Exceptions.CallbackNotInitializedException import CallbackNotInitializedException


class TriggerBase(Thread):
    """Provides basic functionality and a common interface for triggers"""
    __callback__: Callable[[], None] = None

    def register_callback(self, callback: Callable[[None], None]):
        """Registers an action that is executed when the trigger is activated"""
        self.__callback__ = callback

    def trigger(self):
        """Calls the associated callback function"""
        if self.__callback__ is None:
            raise CallbackNotInitializedException()
        self.__callback__()

    def run(self):
        pass
