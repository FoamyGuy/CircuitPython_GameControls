# SPDX-FileCopyrightText: Copyright (c) 2025 Tim C
#
# SPDX-License-Identifier: MIT

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/foamyguy/CircuitPython_GameControls.git"

import array
import time

import usb.core

from game_controls.game_controls_base import ControlsDictionary, GameControlsBase

B_BTN_INDEX = 12
A_BTN_INDEX = 13
Y_BTN_INDEX = 11
X_BTN_INDEX = 14

RIGHT_BTN_INDEX = 7
LEFT_BTN_INDEX = 8
UP_BTN_INDEX = 9
DOWN_BTN_INDEX = 10

START_SELECT_BTN_INDEX = 1


class USBHIDControls(GameControlsBase):
    def __init__(self, ignore_indexes=None):
        self.ignore_indexes = ignore_indexes
        self.device = None
        while self.device is None:
            for d in usb.core.find(find_all=True):
                self.device = d
            time.sleep(0.1)

        self.device.set_configuration()

        buf = array.array("B", [0] * 64)
        _count = self.device.read(0x81, buf)
        self.buf = array.array("B", [0] * _count)
        _count = self.device.read(0x81, self.buf)
        self.idle_state = self.buf[:]

        self._pressed_dict = ControlsDictionary(
            {
                "a": False,
                "b": False,
                "x": False,
                "y": False,
                "select": False,
                "start": False,
                "up": False,
                "down": False,
                "left": False,
                "right": False,
            }
        )

    def _update_dict(self):
        _count = self.device.read(0x81, self.buf)
        # USBHIDControls.print_array(self.buf)
        self._pressed_dict["b"] = self.buf[B_BTN_INDEX] > 0
        self._pressed_dict["a"] = self.buf[A_BTN_INDEX] > 0
        self._pressed_dict["x"] = self.buf[X_BTN_INDEX] > 0
        self._pressed_dict["y"] = self.buf[Y_BTN_INDEX] > 0

        self._pressed_dict["select"] = (
            self.buf[START_SELECT_BTN_INDEX] == 1 or self.buf[START_SELECT_BTN_INDEX] == 3
        )
        self._pressed_dict["start"] = (
            self.buf[START_SELECT_BTN_INDEX] == 2 or self.buf[START_SELECT_BTN_INDEX] == 3
        )

        self._pressed_dict["up"] = self.buf[UP_BTN_INDEX] > 0
        self._pressed_dict["down"] = self.buf[DOWN_BTN_INDEX] > 0
        self._pressed_dict["left"] = self.buf[LEFT_BTN_INDEX] > 0
        self._pressed_dict["right"] = self.buf[RIGHT_BTN_INDEX] > 0

    @property
    def button_state(self) -> ControlsDictionary:
        """
        The current state of all the buttons.

        :return: A dictionary containing the button states.
          Keys are the strings "up", "down", "left", "right",
          "a", "b", "x", "y", "select". Values are Booleans.
        """

        self._update_dict()
        return self._pressed_dict

    @staticmethod
    def print_array(arr, fmt="hex"):
        out_str = ""
        for i in range(len(arr)):
            if fmt == "hex":
                out_str += f"{int(arr[i]):02x} "
            elif fmt == "bin":
                out_str += f"{int(arr[i]):08b} "
        print(out_str)

    def reports_equal(self, report_a, report_b):
        if report_a is None and report_b is not None or report_b is None and report_a is not None:
            return False
        for i in range(len(report_a)):
            if self.ignore_indexes is not None and i not in self.ignore_indexes:
                if report_a[i] != report_b[i]:
                    return False
        return True
