import analogio

try:
    from typing import Dict, Tuple
except ImportError:
    pass

import board
import keypad
from micropython import const

from game_controls.game_controls_base import GameControlsBase, KeyStates
from digitalio import DigitalInOut, Direction, Pull

_BTN_B = const(0)
_BTN_A = const(1)
_BTN_START = const(2)
_BTN_SELECT = const(3)
_BTN_RIGHT = const(4)
_BTN_DOWN = const(5)
_BTN_UP = const(6)
_BTN_LEFT = const(7)

class PyGamerGameControls(GameControlsBase):



    def __init__(self):
        self._keys = keypad.ShiftRegisterKeys(
            clock=board.BUTTON_CLOCK,
            data=board.BUTTON_OUT,
            latch=board.BUTTON_LATCH,
            key_count=8,
            value_when_pressed=True,
        )
        self._buttons = KeyStates(self._keys)
        self._pressed_dict = {
            'a': False,
            'b': False,
            'start': False,
            'select': False,
            'up': False,
            'down': False,
            'left': False,
            'right': False,
        }

        self._pygamer_joystick_x = analogio.AnalogIn(board.JOYSTICK_X)
        self._pygamer_joystick_y = analogio.AnalogIn(board.JOYSTICK_Y)


    def _update_dict(self):
        x = self._pygamer_joystick_x.value
        y = self._pygamer_joystick_y.value

        self._pressed_dict['b'] = self._buttons.was_pressed(_BTN_B)
        self._pressed_dict['a'] = self._buttons.was_pressed(_BTN_A)
        self._pressed_dict['start'] = self._buttons.was_pressed(_BTN_START)
        self._pressed_dict['select'] = self._buttons.was_pressed(_BTN_SELECT)

        self._pressed_dict['up'] = y < 15000
        self._pressed_dict['down'] = y > 50000
        self._pressed_dict['left'] = x < 15000
        self._pressed_dict['right'] = x > 50000

    @property
    def button(self) -> Dict:
        """
        """
        self._buttons.update()
        self._update_dict()
        return self._pressed_dict



game_controls = PyGamerGameControls()
