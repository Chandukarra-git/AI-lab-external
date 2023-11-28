from collections import deque
def bfs_water_jug_problem(capacity_jug1, capacity_jug2, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        current_state = queue.popleft()
        jug1, jug2 = current_state

        if current_state == target:
            return True

        visited.add(current_state)

        if jug1 < capacity_jug1:
            new_state = (capacity_jug1, jug2)
            if new_state not in visited:
                queue.append(new_state)

        
        if jug2 < capacity_jug2:
            new_state = (jug1, capacity_jug2)
            if new_state not in visited:
                queue.append(new_state)

        # Empty jug 1
        if jug1 > 0:
            new_state = (0, jug2)
            if new_state not in visited:
                queue.append(new_state)

        # Empty jug 2
        if jug2 > 0:
            new_state = (jug1, 0)
            if new_state not in visited:
                queue.append(new_state)

        # Pour water from jug 1 to jug 2
        if jug1 > 0 and jug2 < capacity_jug2:
            pour = min(jug1, capacity_jug2 - jug2)
            new_state = (jug1 - pour, jug2 + pour)
            if new_state not in visited:
                queue.append(new_state)

        # Pour water from jug 2 to jug 1
        if jug2 > 0 and jug1 < capacity_jug1:
            pour = min(jug2, capacity_jug1 - jug1)
            new_state = (jug1 + pour, jug2 - pour)
            if new_state not in visited:
                queue.append(new_state)

    return False

# Get user inputs for jug capacities and target state
jug1_capacity = int(input("Enter capacity of Jug 1: "))
jug2_capacity = int(input("Enter capacity of Jug 2: "))
target_jug1 = int(input("Enter target amount of water in Jug 1: "))
target_jug2 = int(input("Enter target amount of water in Jug 2: "))
target_state = (target_jug1, target_jug2)

# Use BFS to solve
result = bfs_water_jug_problem(jug1_capacity, jug2_capacity, target_state)

# Print result
print("BFS: Can we measure {} liters of water? {}".format(target_state, result))

