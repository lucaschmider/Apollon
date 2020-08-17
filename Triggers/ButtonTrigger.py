from Triggers.TriggerBase import TriggerBase
from gpiozero import Button


class ButtonTrigger(TriggerBase):
    __pin_number__ = 0  # type: int
    __trigger_button__ = None  # type: Button

    def __init__(self, pin: int):
        self.__pin_number__ = pin

    def run(self):
        self.__trigger_button__ = Button(self.__pin_number__)
        self.__trigger_button__.when_pressed = self.trigger
