Python 3.12.0 (v3.12.0:0fb18b02c8, Oct  2 2023, 09:45:56) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
def print_board(grid):
    print("---------")
    print(f"| {' '.join(grid[0])} | \n| {' '.join(grid[1])} | \n| {' '.join(grid[2])} |")
    print("---------")

def is_valid_coordinates(x, y):
    return 1 <= x <= 3 and 1 <= y <= 3

def is_cell_empty(grid, x, y):
    return grid[x - 1][y - 1] == ' '

def make_move(grid, x, y, player):
    grid[x - 1][y - 1] = player

start = "         "  # Empty grid to start
grid = [list(start[i:i + 3]) for i in range(0, len(start), 3)]  # Create the 3x3 grid

print_board(grid)
... 
... players = ['X', 'O']
... current_player = players[0]
... 
... for _ in range(9):  # Maximum of 9 moves
...     while True:
...         try:
...             move = input(f"Enter the coordinates for {current_player} (row column): ")
...             x, y = map(int, move.split())
... 
...             if not is_valid_coordinates(x, y):
...                 print("Coordinates should be from 1 to 3!")
...                 continue
... 
...             if not is_cell_empty(grid, x, y):
...                 print("This cell is occupied! Choose another one!")
...                 continue
... 
...             break
...         except ValueError:
...             print("You should enter numbers!")
... 
...     make_move(grid, x, y, current_player)
...     print_board(grid)
... 
...     # Check for a winner
...     if any(all(cell == current_player for cell in row) for row in grid) or \
...        any(all(grid[i][j] == current_player for i in range(3)) for j in range(3)) or \
...        all(grid[i][i] == current_player for i in range(3)) or \
...        all(grid[i][2 - i] == current_player for i in range(3)):
...         print(f"{current_player} wins!")
...         break
... 
...     # Switch to the next player
...     current_player = players[1] if current_player == players[0] else players[0]
... else:
...     print("Draw!")
