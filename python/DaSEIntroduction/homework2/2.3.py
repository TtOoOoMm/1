def is_valid_state(state):
    if (state[1] == state[2] and state[0] != state[1]) or (state[2] == state[3] and state[0] != state[2]):
        return False
    return True

def dfs(state, path, visited):
    if state == (0, 0, 0, 0):
        print("找到解决方案：", path)
        return

    for move in moves:
        new_state = tuple(state[i] + move[i] for i in range(4))
        if all(0 <= new_state[i] <= 1 for i in range(4)) and is_valid_state(new_state) and new_state not in visited:
            visited.add(new_state)
            dfs(new_state, path + [new_state], visited)
            visited.remove(new_state)

initial_state = (1, 1, 1, 1)

moves = [
    (-1, 0, 0, 0), 
    (-1, -1, 0, 0),
    (-1, 0, -1, 0),
    (-1, 0, 0, -1),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 0, 1, 0),
    (1, 0, 0, 1) 
]

visited = set()
visited.add(initial_state)

dfs(initial_state, [initial_state], visited)