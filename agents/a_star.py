from funcs import is_legal, move, check_winning, is_blocked
from copy import deepcopy

steps = ((0, 1), (1, 0), (0, -1), (-1, 0))  # Down, Right, Up, Left


def heuristic(state):
    coins = [(i, j) for i in range(state.num_rows) for j in range(state.num_cols) if state.grid[i][j] == 2]
    chests = [(i, j) for i in range(state.num_rows) for j in range(state.num_cols) if state.grid[i][j] == 3]

    x, y = state.player_x, state.player_y

    if chests:
        closest_chest, min_player_to_chest = min(
            ((chest_x, chest_y), abs(x - chest_x) + abs(y - chest_y)) for chest_x, chest_y in chests
        )
    else:
        return 0

    if coins:
        min_chest_to_coin = min(
            abs(closest_chest[0] - coin_x) + abs(closest_chest[1] - coin_y) for coin_x, coin_y in coins
        )
    else:
        min_chest_to_coin = 0

    return min_player_to_chest + min_chest_to_coin


def a_star(game_state):
    pqueue = [(0, game_state)]
    visited = []

    while pqueue:

        pqueue.sort(key=lambda x: x[0])
        _, current_state = pqueue.pop(0)

        if check_winning(current_state):
            return current_state

        state_visited = (current_state.player_x, current_state.player_y, current_state.grid)
        if state_visited in visited:
            continue
        visited.append(state_visited)

        for step in steps:
            next_state = deepcopy(current_state)
            if is_legal(next_state, step) and not is_blocked(next_state, step):
                move(next_state, step)
                new_cost = len(next_state.move_history) + 1
                priority = new_cost + heuristic(next_state)
                pqueue.append((priority, next_state))

    return game_state
