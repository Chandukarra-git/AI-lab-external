from collections import deque

# Define the initial and goal states
INITIAL_STATE = {'farmer': 'left', 'fox': 'left', 'goose': 'left', 'beans': 'left'}
GOAL_STATE = {'farmer': 'right', 'fox': 'right', 'goose': 'right', 'beans': 'right'}

# Define the valid moves
VALID_MOVES = [
    ['fox'],
    ['goose'],
    ['beans'],
    ['fox', 'goose'],
    ['goose', 'beans']
]

def is_valid(state):
    if state['goose'] == state['beans'] and state['farmer'] != state['goose']:
        return False
    if state['fox'] == state['goose'] and state['farmer'] != state['fox']:
        return False
    return True

def generate_next_states(current_state):
    next_states = []
    for move in VALID_MOVES:
        new_state = current_state.copy()
        new_state['farmer'] = 'right' if current_state['farmer'] == 'left' else 'left'
        for item in move:
            new_state[item] = 'right' if current_state[item] == 'left' else 'left'
        if is_valid(new_state):
            next_states.append(new_state)
    return next_states

def bfs_search():
    queue = deque([(INITIAL_STATE, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(current_state.items()))

        if current_state == GOAL_STATE:
            return path

        next_states = generate_next_states(current_state)
        for state in next_states:
            if tuple(state.items()) not in visited:
                queue.append((state, path + [state]))

    return None

def main():
    solution_path = bfs_search()

    if solution_path is None:
        print("No solution found.")
    else:
        print("Solution:")
        for step, state in enumerate(solution_path):
            print(f"Step {step + 1}: {state}")
        print("Crossed the river successfully!")

if __name__ == "__main__":
    main()


