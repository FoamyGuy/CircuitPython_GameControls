# SPDX-FileCopyrightText: Copyright (c) 2025 Tim C
#
# SPDX-License-Identifier: MIT

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/foamyguy/CircuitPython_GameControls.git"

try:
    from typing import Dict
except ImportError:
    pass

from adafruit_featherwing import joy_featherwing

from game_controls.game_controls_base import ControlsDictionary, GameControlsBase


class JoyFeatherwingControls(GameControlsBase):
    def __init__(self):
        self._wing = joy_featherwing.JoyFeatherWing()

        self._pressed_dict = ControlsDictionary(
            {
                "a": False,
                "b": False,
                "x": False,
                "y": False,
                "select": False,
                "up": False,
                "down": False,
                "left": False,
                "right": False,
            }
        )

    def _update_dict(self):
        self._pressed_dict["b"] = self._wing.button_b
        self._pressed_dict["a"] = self._wing.button_a
        self._pressed_dict["x"] = self._wing.button_x
        self._pressed_dict["y"] = self._wing.button_y

        self._pressed_dict["select"] = self._wing.button_select

        y, x = self._wing.joystick
        self._pressed_dict["up"] = y > 30
        self._pressed_dict["down"] = y < -30
        self._pressed_dict["left"] = x < -30
        self._pressed_dict["right"] = x > 30
        # print(f"({x}, {y})")

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


game_controls = JoyFeatherwingControls()
