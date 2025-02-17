# SPDX-FileCopyrightText: Copyright (c) 2025 Tim C
#
# SPDX-License-Identifier: Unlicense


from game_controls.usb_hid_controller import USBHIDControls

game_controls = USBHIDControls()
while True:
    cur_state = game_controls.button_state
    if cur_state["a"]:
        print("A btn!")

    if cur_state["b"]:
        print("B btn!")

    if cur_state["x"]:
        print("X btn!")

    if cur_state["y"]:
        print("Y btn!")

    if cur_state["start"]:
        print("START btn!")

    if cur_state["select"]:
        print("SELECT btn!")

    if cur_state["up"]:
        print("UP btn!")

    if cur_state["down"]:
        print("DOWN btn!")

    if cur_state["right"]:
        print("RIGHT btn!")

    if cur_state["left"]:
        print("LEFT btn!")
