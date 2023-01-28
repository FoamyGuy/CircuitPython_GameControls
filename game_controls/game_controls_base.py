try:
    from typing import Union
except ImportError:
    pass

from keypad import Keys, ShiftRegisterKeys


class GameControlsBase:

    def __init__(self):
        pass


class KeyStates:
    """Convert `keypad.Event` information from the given `keypad` scanner into key-pressed state.
    :param scanner: a `keypad` scanner, such as `keypad.Keys`
    """

    def __init__(self, scanner: Union[Keys, ShiftRegisterKeys]) -> None:
        self._scanner = scanner
        self._pressed = [False] * self._scanner.key_count
        self.update()

    def update(self) -> None:
        """Update key information based on pending scanner events."""

        # If the event queue overflowed, discard any pending events,
        # and assume all keys are now released.
        if self._scanner.events.overflowed:
            self._scanner.events.clear()
            self._scanner.reset()
            self._pressed = [False] * self._scanner.key_count

        self._was_pressed = self._pressed.copy()

        while True:
            event = self._scanner.events.get()
            if not event:
                # Event queue is now empty.
                break
            self._pressed[event.key_number] = event.pressed
            if event.pressed:
                self._was_pressed[event.key_number] = True

    def was_pressed(self, key_number: int) -> bool:
        """True if key was down at any time since the last `update()`,
        even if it was later released.
        """
        return self._was_pressed[key_number]

    def pressed(self, key_number: int) -> bool:
        """True if key is currently pressed, as of the last `update()`."""
        return self._pressed[key_number]


class ControlsDictionary():
    _VALID_BTNS = ("a", "b", "x", "y", "up", "down", "left", "right", "start", "select")

    def __init__(self, initial_dict = None):
        if initial_dict is not None:
            self._store = initial_dict
        else:
            self._store = {}

    def __getitem__(self, field):

        #print(self._store.keys())
        if field not in self._store.keys():
            if field in self._VALID_BTNS:
                print(f"This device does not have a {field} button.")
                return
            else:
                raise KeyError(field)

        return self._store[field]

    def __setitem__(self, key, value):
        if key not in self._VALID_BTNS:
            raise KeyError(f"{key} is not a valid button name. Valid names are: {self._VALID_BTNS}")
        self._store[key] = value

    def __str__(self):
        return str(self._store)