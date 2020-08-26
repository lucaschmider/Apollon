from datetime import datetime
from time import sleep
from typing import Tuple

from Triggers.TriggerBase import TriggerBase


class TimeTrigger(TriggerBase):
    __configured_trigger_time__: Tuple[int, int] = None  # Time to trigger (HH, MM)

    def __init__(self, trigger_time: Tuple[int, int]):
        super().__init__()
        self.__configured_trigger_time__ = trigger_time

    def run(self) -> None:
        while True:
            now = datetime.now()
            if now.hour == self.__configured_trigger_time__[0] and \
               now.minute == self.__configured_trigger_time__[1] and \
               now.second == 0:
                self.trigger()
                sleep(1)
