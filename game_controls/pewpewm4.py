# SPDX-FileCopyrightText: Copyright (c) 2025 Tim C
#
# SPDX-License-Identifier: MIT

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/foamyguy/CircuitPython_GameControls.git"

try:
    from typing import Dict
except ImportError:
    pass

import board
import keypad
from digitalio import DigitalInOut, Direction, Pull
from micropython import const

from game_controls.game_controls_base import ControlsDictionary, GameControlsBase, KeyStates

_BTN_B = const(0)
_BTN_A = const(1)
_BTN_Y = const(2)
_BTN_RIGHT = const(3)
_BTN_DOWN = const(4)
_BTN_UP = const(5)
_BTN_LEFT = const(6)


KEY_PINS = (
    board.BUTTON_X,
    board.BUTTON_O,
    board.BUTTON_Z,
    board.BUTTON_RIGHT,
    board.BUTTON_DOWN,
    board.BUTTON_UP,
    board.BUTTON_LEFT,
)


class PewPewM4GameControls(GameControlsBase):
    def __init__(self):
        self._keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)

        self._buttons = KeyStates(self._keys)
        self._pressed_dict = ControlsDictionary(
            {
                "a": False,
                "b": False,
                "Y": False,
                "up": False,
                "down": False,
                "left": False,
                "right": False,
            }
        )

    def _update_dict(self):
        self._pressed_dict["b"] = self._buttons.was_pressed(_BTN_B)
        self._pressed_dict["a"] = self._buttons.was_pressed(_BTN_A)
        self._pressed_dict["y"] = self._buttons.was_pressed(_BTN_Y)

        self._pressed_dict["up"] = self._buttons.was_pressed(_BTN_UP)
        self._pressed_dict["down"] = self._buttons.was_pressed(_BTN_DOWN)
        self._pressed_dict["left"] = self._buttons.was_pressed(_BTN_LEFT)
        self._pressed_dict["right"] = self._buttons.was_pressed(_BTN_RIGHT)

    @property
    def button_state(self) -> Dict:
        """
        The current state of all the buttons.

        :return: A dictionary containing the button states.
          Keys are the strings "up", "down", "left", "right",
          "a", "b", "y". Values are Booleans.
        """
        self._buttons.update()
        self._update_dict()
        return self._pressed_dict


game_controls = PewPewM4GameControls()
