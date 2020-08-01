from datetime import datetime, timedelta

from Triggers.TriggerBase import TriggerBase


class TimeTrigger(TriggerBase):
    def run(self) -> None:
        trigger_time = datetime.now()
        while True:
            now = datetime.now()
            if now + timedelta(seconds=-1) <= trigger_time <= now + timedelta(1):
                self.trigger()
            else:
                print("Else")