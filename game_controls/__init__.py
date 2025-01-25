# SPDX-FileCopyrightText: Copyright (c) 2025 Tim C
#
# SPDX-License-Identifier: MIT
"""
`gamecontrols`
================================================================================

An abstraction layer for CircuitPython to access commonly used video game control inputs in a consistent manner across different hardware devices and configurations.


* Author(s): Tim C

Implementation Notes
--------------------

**Hardware:**

* `PewPewM4 <https://circuitpython.org/board/pewpew_m4/>`_
* `Adafruit PyGamer <https://circuitpython.org/board/pygamer/>`_
* `Pimoroni Picosystem <https://circuitpython.org/board/pimoroni_picosystem/>`_
* `Adafruit PyBadge <https://circuitpython.org/board/pybadge/>`_
* `Adafruit Joy Feathering <https://www.adafruit.com/product/3632>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

Joy Featherwing requires BusDevice and Register, other hardware does not.

# * Adafruit's Bus Device library: https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
# * Adafruit's Register library: https://github.com/adafruit/Adafruit_CircuitPython_Register
"""

# imports

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/foamyguy/CircuitPython_GameControls.git"

import board

if board.board_id == "pygamer":
    from .pygamer import game_controls
elif board.board_id == "pybadge":
    from .pybadge import game_controls
elif board.board_id == "pimoroni_picosystem":
    from .picosystem import game_controls
elif board.board_id == "pewpew_m4":
    from .pewpewm4 import game_controls
else:
    print("Supportd hardware was not automatically detected")
    game_controls = None