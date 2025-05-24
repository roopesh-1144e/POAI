def is_safe(board, i, j):
    n = len(board)
    j_left, j_right = j, j
    while i >= 0:
        if (j_left >= 0 and board[i][j_left] == 1) or board[i][j] == 1 or (j_right < n and board[i][j_right] == 1):
            return False
        i -= 1
        j_left -= 1
        j_right += 1
    return True

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell == 1 else "." for cell in row))

def rec(board, i):
    n = len(board)
    if i == n:
        print_board(board)
        return True
    for j in range(n):
        if is_safe(board, i, j):
            board[i][j] = 1
            if rec(board, i + 1):
                return True
            board[i][j] = 0
    return False
def n_queens(n):
    board = [[0] * n for _ in range(n)]
    rec(board, 0)

n_queens(8)
