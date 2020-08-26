from Triggers.TriggerBase import TriggerBase
from gpiozero import Button


class ButtonTrigger(TriggerBase):
    __pin_number__: int = 0
    __trigger_button__: Button = None

    def __init__(self, pin: int):
        super().__init__()
        self.__pin_number__ = pin

    def run(self):
        self.__trigger_button__ = Button(self.__pin_number__)
        self.__trigger_button__.when_pressed = self.trigger
