import math

HUMAN = 'X'
AI = 'O'
EMPTY = ' '

def print_board(board):
    print("\n")
    for i in range(3):
        print(f" {board[i][0]} | {board[i][1]} | {board[i][2]} ")
        if i < 2:
            print("---+---+---")
    print("\n")

def check_winner(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != EMPTY:
            return board[row][0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != EMPTY:
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]
    
    if all(cell != EMPTY for row in board for cell in row):
        return 'Draw'
    
    return None

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == AI:
        return 10 - depth
    elif winner == HUMAN:
        return depth - 10
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = AI
                    score = minimax(board, depth + 1, False, alpha, beta)
                    board[row][col] = EMPTY
                    best_score = max(score, best_score)
                    alpha = max(alpha, best_score)
                    if beta <= alpha:
                        break
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = HUMAN
                    score = minimax(board, depth + 1, True, alpha, beta)
                    board[row][col] = EMPTY
                    best_score = min(score, best_score)
                    beta = min(beta, best_score)
                    if beta <= alpha:
                        break
        return best_score

def get_best_move(board):
    best_score = -math.inf
    move = (-1, -1)
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = AI
                score = minimax(board, 0, False, -math.inf, math.inf)
                board[row][col] = EMPTY
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move

def main():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe AI!")
    print("You are 'X', the AI is 'O'.")
    print_board(board)

    while True:
        while True:
            try:
                move = input("Enter your move (row and col: 0, 1, or 2) separated by space: ")
                r, c = map(int, move.split())
                if board[r][c] == EMPTY:
                    board[r][c] = HUMAN
                    break
                else:
                    print("Cell already occupied! Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter two numbers between 0 and 2.")

        print_board(board)
        if check_winner(board):
            break

        print("AI is thinking...")
        r, c = get_best_move(board)
        board[r][c] = AI
        print_board(board)
        
        if check_winner(board):
            break

    winner = check_winner(board)
    if winner == 'Draw':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

if __name__ == "__main__":
    main()