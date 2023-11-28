def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col or \
           board[i] + i == col + row or \
           board[i] - i == col - row:
            return False
    return True


def solve_n_queens_util(n, row, board, solutions):
    if row == n:
        solutions.append(board[:])
    else:
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                solve_n_queens_util(n, row + 1, board, solutions)


def solve_n_queens(n):
    solutions = []
    board = [-1] * n
    solve_n_queens_util(n, 0, board, solutions)
    return solutions


def print_solution(solution):
    for board in solution:
        for row in range(len(board)):
            line = ""
            for col in range(len(board)):
                if col == board[row]:
                    line += "Q "
                else:
                    line += ". "
            print(line)
        print()


if __name__ == "__main__":
    while True:
        try:
            num_queens = int(input("Enter the number of queens: "))
            if num_queens < 1:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    solutions = solve_n_queens(num_queens)

    if solutions:
        print(f"Solutions for {num_queens}-Queens Problem:")
        for idx, solution in enumerate(solutions):
            print("Solution", idx + 1)
            print_solution([solution])
    else:
        print("No solution exists")


monban


import random
class Room:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [['.' for _ in range(cols)] for _ in range(rows)]
        self.monkey_row = random.randint(0, rows - 1)
        self.monkey_col = random.randint(0, cols - 1)
        self.banana_row = random.randint(0, rows - 1)
        self.banana_col = random.randint(0, cols - 1)
        self.chair_row = random.randint(0, rows - 1)
        self.chair_col = random.randint(0, cols - 1)
        self.grid[self.monkey_row][self.monkey_col] = 'M'
        self.grid[self.banana_row][self.banana_col] = 'B'
        self.grid[self.chair_row][self.chair_col] = 'C'
    def print_room(self):
        for row in self.grid:
            print(' '.join(row))
        print()
    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols
    def move_monkey(self, direction):
        new_monkey_row = self.monkey_row
        new_monkey_col = self.monkey_col
        if direction == 'up':
            new_monkey_row -= 1
        elif direction == 'down':
            new_monkey_row += 1
        elif direction == 'left':
            new_monkey_col -= 1
        elif direction == 'right':
            new_monkey_col += 1
        if self.is_valid_move(new_monkey_row, new_monkey_col):
            self.grid[self.monkey_row][self.monkey_col] = ' '
            self.monkey_row = new_monkey_row
            self.monkey_col = new_monkey_col
            self.grid[self.monkey_row][self.monkey_col] = 'M'

def main():
    rows = int(input("Enter Width of Room :"))
    cols = int(input("Enter Length of Room :"))
    room = Room(rows, cols)
    print("Monkey and Banana Problem!")
    steps = 0
    while (room.monkey_row, room.monkey_col) != (room.chair_row, room.chair_col):
        print("Current Room:")
        room.print_room()
        move = input("Enter your Move : ").lower()
        if move in ['up', 'down', 'left', 'right']:
            room.move_monkey(move)
            steps += 1
        else:
            print("Invalid Move!!")
    if (room.monkey_row, room.monkey_col) == (room.chair_row, room.chair_col):
        print("Monkey reached the Chair!")
        print(f"Steps taken : {steps}")
    while (room.monkey_row, room.monkey_col) != (room.banana_row, room.banana_col):
        print("Current Room:")
        room.print_room()
        move = input("Enter your Move : ").lower()
        if move in ['up', 'down', 'left', 'right']:
            room.move_monkey(move)
            steps += 1
        else:
            print("Invalid move!!")
    if (room.monkey_row, room.monkey_col) == (room.banana_row, room.banana_col):
        print("Congratulations, Monkey collected the Banana!!")
        print(f"Total Steps taken : {steps}")
if __name__ == "__main__":
    main()
