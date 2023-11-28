import itertools

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def total_distance(route, points):
    total = 0
    for i in range(len(route) - 1):
        total += distance(points[route[i]], points[route[i + 1]])
    total += distance(points[route[-1]], points[route[0]])
    return total

def traveling_salesperson_dfs(points, current_route, current_distance, visited):
    num_points = len(points)

    if len(current_route) == num_points:
        current_distance += distance(points[current_route[-1]], points[current_route[0]])
        return current_route, current_distance

    min_distance = float('inf')
    optimal_route = []

    for next_point in range(num_points):
        if next_point not in visited:
            new_route = current_route + (next_point,)
            new_dist = current_distance + distance(points[current_route[-1]], points[next_point])
            new_visited = visited | {next_point}

            route, dist = traveling_salesperson_dfs(points, new_route, new_dist, new_visited)
            if dist < min_distance:
                min_distance = dist
                optimal_route = route

    return optimal_route, min_distance

def main():
    num_points = int(input("Enter the number of points: "))
    points = []
    for i in range(num_points):
        x, y = map(float, input(f"Enter coordinates for point {i+1} (x y): ").split())
        points.append((x, y))

    start_point = 0
    start_route = (start_point,)
    start_distance = 0
    start_visited = {start_point}

    optimal_route, min_distance = traveling_salesperson_dfs(points, start_route, start_distance, start_visited)
    print("\nOptimal route:", optimal_route)
    print("Minimum distance:", min_distance)

if __name__ == "__main__":
    main()


