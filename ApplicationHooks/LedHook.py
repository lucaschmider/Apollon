import time
from typing import List, Tuple

import board
from neopixel import NeoPixel
from ApplicationHooks.ApplicationHookBase import ApplicationHookBase


class LedHook(ApplicationHookBase):
    __DEFAULT_FRAME__: List[int] = None
    __SPEECH_FRAMES__: List[List[int]] = None
    __COLOR_THEME__: List[Tuple[int, int, int]] = None
    __FRAME_DURATION__ = 0.1
    __pixels__: NeoPixel = None
    __animation_running__ = False

    def __init__(self, configuration):
        super().__init__()
        self.__DEFAULT_FRAME__ = configuration["FRAMES"]["DEFAULT"]
        self.__SPEECH_FRAMES__ = configuration["FRAMES"]["SPEECH"]
        self.__COLOR_THEME__ = configuration["THEME"]
        self.__pixels__ = NeoPixel(board.D18, configuration["LED_COUNT"])

    def before_consumers_started(self) -> None:
        self.__animation_running__ = True

    def after_consumers_finished(self) -> None:
        self.__animation_running__ = False
        time.sleep(5 * self.__FRAME_DURATION__)
        self.__restore_default_frame__()

    def application_ready(self) -> None:
        self.__restore_default_frame__()

    def __restore_default_frame__(self):
        for led_index in range(len(self.__DEFAULT_FRAME__)):
            self.__pixels__[led_index] = self.__COLOR_THEME__[self.__DEFAULT_FRAME__[led_index]]

    def run(self) -> None:
        while True:
            if self.__animation_running__:
                for frame in self.__SPEECH_FRAMES__:
                    for led_index in range(len(frame)):
                        self.__pixels__[led_index] = self.__COLOR_THEME__[frame[led_index]]
                    time.sleep(self.__FRAME_DURATION__)