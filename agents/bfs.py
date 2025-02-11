from funcs import is_legal, move, check_winning, is_blocked
from copy import deepcopy

steps = ((0, 1), (1, 0), (0, -1), (-1, 0))  # Down, Right, Up, Left


def bfs(game_state):
    queue = [game_state]
    visited = []

    while queue:
        current_state = queue.pop(0)

        if check_winning(current_state):
            return current_state

        state_visited = [current_state.player_x, current_state.player_y, current_state.grid]
        if state_visited in visited:
            continue
        visited.append(state_visited)

        for step in steps:
            next_state = deepcopy(current_state)
            if is_legal(next_state, step) and not is_blocked(next_state, step):
                move(next_state, step)
                queue.append(next_state)

    return game_state
