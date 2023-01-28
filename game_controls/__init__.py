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