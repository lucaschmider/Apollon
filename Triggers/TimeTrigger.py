from datetime import datetime, timedelta
from time import sleep

from Triggers.TriggerBase import TriggerBase


class TimeTrigger(TriggerBase):
    __last_trigger_time__ = None

    def run(self) -> None:
        trigger_time = datetime.now()
        while True:
            now = datetime.now()
            if now + timedelta(seconds=-0.5) <= trigger_time <= now + timedelta(0.5):
                self.trigger()
                self.__last_trigger_time__ = now
            sleep(1)
