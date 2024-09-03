import copy

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def find_empty_space(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def is_valid_move(i, j):
    return 0 <= i < 3 and 0 <= j < 3

def hill_climbing(initial_board, goal_board):
    current_board = copy.deepcopy(initial_board)
    current_cost = calculate_cost(current_board, goal_board)

    while True:
        print("Current State:")
        print_board(current_board)
        if current_cost == 0:
            print("Goal State Reached!")
            break

        neighbors = generate_neighbors(current_board)
        best_neighbor = min(neighbors, key=lambda x: calculate_cost(x, goal_board))

        if calculate_cost(best_neighbor, goal_board) >= current_cost:
            print("Local minimum reached.")
            break

        current_board = best_neighbor
        current_cost = calculate_cost(current_board, goal_board)

    print("Final State:")
    print_board(current_board)

def calculate_cost(board, goal_board):
    cost = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != goal_board[i][j]:
                cost += 1
    return cost

def generate_neighbors(board):
    neighbors = []
    empty_i, empty_j = find_empty_space(board)

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    for move in moves:
        new_i, new_j = empty_i + move[0], empty_j + move[1]

        if is_valid_move(new_i, new_j):
            new_board = copy.deepcopy(board)
            new_board[empty_i][empty_j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[empty_i][empty_j]
            neighbors.append(new_board)

    return neighbors

# Take input from the user for initial state
initial_state = []
print("Enter the Initial State (3x3 grid):")
for _ in range(3):
    row = list(map(int, input().split()))
    initial_state.append(row)

# Take input from the user for goal state
goal_state = []
print("Enter the Goal State (3x3 grid):")
for _ in range(3):
    row = list(map(int, input().split()))
    goal_state.append(row)

print("\nInitial State:")
print_board(initial_state)

hill_climbing(initial_state, goal_state)
