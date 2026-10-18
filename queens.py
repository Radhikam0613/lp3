N = 8
board = [-1] * N
board[0] = 0

def print_board():
    for r in range(N):
        # so where b[r] is any value of c and not -1 we print Q
        print(" ".join("Q" if board[r] == c else "." for c in range(N)))
    print()

def safe(row, col):
    for r in range(row):
        # Two queens are on the same diagonal when the absolute difference 
        # between their columns equals the absolute difference between their rows.
        if board[r] == col or abs(board[r] - col) == abs(r - row):
            return False
    return True

def solve(row):
    if row == N: return True
    for col in range(N):
        if safe(row, col):
            board[row] = col
            if solve(row + 1):
                return True
            board[row] = -1
    return False
print("Initial Matrix:")
print_board()
if solve(1):
    print("Final Matrix:")
    print_board()
else:print("No solution found")

# N = 8
# board = [-1] * N
# board[0] = 0

# def print_board():
#     for r in range(N):
#         # Print 'Q' for the column where the queen is placed, and '.' for empty spaces
#         print(" ".join("Q" if board[r] == c else "." for c in range(N)))
#     print()

# def safe(row, col):
#     for r in range(row):
#         # Check if the column is already occupied or if the queens are on the same diagonal
#         # Two queens are on the same diagonal when the absolute difference between their 
#           columns equals the absolute difference between their rows.
#         # abs(board[r] - col) == abs(r - row) calculates the diagonal conflict 
#         # by comparing the difference in rows and columns
#         if board[r] == col or abs(board[r] - col) == abs(r - row):
#             return False
#     return True

# def solve(row):
#     # Base case: if all queens are placed, return True
#     if row == N:
#         return True

#     # Try placing a queen in each column of the current row
#     for col in range(N):
#         if safe(row, col):
#             # Place the queen and move to the next row
#             board[row] = col
#             if solve(row + 1):
#                 return True
#             board[row] = -1

#     return False

# print("Initial Matrix:")
# print_board()

# # Start solving from the second row since the first queen is already placed
# if solve(1):
#     print("Final Matrix:")
#     print_board()
# else:
#     print("No solution found")