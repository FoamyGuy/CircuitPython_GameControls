Introduction
============


.. image:: https://readthedocs.org/projects/circuitpython-gamecontrols/badge/?version=latest
    :target: https://circuitpython-gamecontrols.readthedocs.io/
    :alt: Documentation Status


.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/foamyguy/CircuitPython_GameControls/workflows/Build%20CI/badge.svg
    :target: https://github.com/foamyguy/CircuitPython_GameControls/actions
    :alt: Build Status


.. image:: https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json
    :target: https://github.com/astral-sh/ruff
    :alt: Code Style: Ruff

An abstraction layer for CircuitPython to access commonly used video game control inputs in a consistent manner across different hardware devices and configurations.


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_
* `Register <https://github.com/adafruit/Adafruit_CircuitPython_Register>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

Installing from PyPI
=====================

On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/circuitpython-gamecontrols/>`_.
To install for current user:

.. code-block:: shell

    pip3 install circuitpython-gamecontrols

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install circuitpython-gamecontrols

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install circuitpython-gamecontrols

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install gamecontrols

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    from game_controls import game_controls

    while True:
        cur_state = game_controls.button
        if (cur_state['a']):
            print("A btn!")

        if (cur_state['b']):
            print("B btn!")

        if (cur_state['start']):
            print("START btn!")

        if (cur_state['select']):
            print("SELECT btn!")

        if (cur_state['up']):
            print("UP btn!")

        if (cur_state['down']):
            print("DOWN btn!")

        if (cur_state['right']):
            print("RIGHT btn!")

        if (cur_state['left']):
            print("LEFT btn!")

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://circuitpython-gamecontrols.readthedocs.io/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/foamyguy/CircuitPython_GameControls/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.
