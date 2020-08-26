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
            if now.minute is self.__configured_trigger_time__[0] and \
               now.hour is self.__configured_trigger_time__[1] and \
               now.second is 0:
                self.trigger()
            sleep(1)
