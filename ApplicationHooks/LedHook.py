from time import sleep
from typing import List, Tuple, Dict
from board import D18
from neopixel import NeoPixel
from ApplicationHooks.ApplicationHookBase import ApplicationHookBase


class LedHook(ApplicationHookBase):
    __ANIMATIONS__: Dict[str, List[List[int]]] = None
    __COLOR_THEME__: List[Tuple[int, int, int]] = None
    __FRAME_DURATION__ = 0.1
    __pixels__: NeoPixel = None
    __current_animation__ = "DEFAULT"

    def __init__(self, configuration):
        super().__init__()
        self.__ANIMATIONS__ = configuration["ANIMATIONS"]
        self.__COLOR_THEME__ = configuration["THEME"]
        self.__pixels__ = NeoPixel(D18, configuration["LED_COUNT"])

    def before_consumers_started(self) -> None:
        self.__current_animation__ = "SPEECH"

    def after_consumers_finished(self) -> None:
        self.__current_animation__ = "DEFAULT"

    def application_ready(self) -> None:
        self.__current_animation__ = "DEFAULT"

    def report_generation_started(self):
        self.__current_animation__ = "GENERATING"
        
    def run(self) -> None:
        while True:
            for frame in self.__ANIMATIONS__[self.__current_animation__]:
                for led_index in range(len(frame)):
                    self.__pixels__[led_index] = self.__COLOR_THEME__[frame[led_index]]
                sleep(self.__FRAME_DURATION__)
