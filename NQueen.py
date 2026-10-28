n = 4
board = [-1] * n

def safe(row, col):
    for i in range(row):
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    if row == n:
        return True

    for col in range(n):
        if safe(row, col):
            board[row] = col

            if solve(row + 1):
                return True

            board[row] = -1

    return False

if solve(0):
    for row in range(n):
        for col in range(n):
            print("Q" if board[row] == col else ".", end=" ")
        print()