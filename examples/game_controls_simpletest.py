# SPDX-FileCopyrightText: Copyright (c) 2025 Tim C
#
# SPDX-License-Identifier: Unlicense
from game_controls import game_controls

while True:
    cur_state = game_controls.button
    if cur_state["a"]:
        print("A btn!")

    if cur_state["b"]:
        print("B btn!")

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
