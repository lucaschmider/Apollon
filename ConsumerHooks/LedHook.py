import time
import board
import neopixel
from ConsumerHooks.ConsumerHookBase import ConsumerHookBase


class LedHook(ConsumerHookBase):
    __DEFAULT_FRAME__ = [2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 0, 0]
    __SPEECH_FRAMES__ = [
        [1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 2, 3, 3],
        [2, 2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 3, 3],
        [2, 2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 3, 3],
        [2, 1, 2, 2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 2, 3, 3]
    ]
    __COLOR_THEME__ = [(0, 0, 0), (0, 0, 255), (0, 162, 20), (255, 0, 0)]
    __FRAME_DURATION__ = 0.1
    __pixels__ = neopixel.NeoPixel(board.D18, 20)
    __animation_running__ = False

    def before_consumers_started(self) -> None:
        self.__animation_running__ = True

    def after_consumers_finished(self) -> None:
        self.__animation_running__ = False
        time.sleep(5 * self.__FRAME_DURATION__)
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