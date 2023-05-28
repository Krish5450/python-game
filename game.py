import tkinter as tk
from tkinter import messagebox

ROWS = 6
COLS = 7
PLAYER1 = "X"
PLAYER2 = "O"

# Create the main window
window = tk.Tk()
window.title("Connect Four")
window.geometry("650x570")
window.resizable(False,False)

# Create the game board
board = [["" for _ in range(COLS)] for _ in range(ROWS)]

# Create the current player variable
current_player = PLAYER1

# Create the game status variable
game_over = False


def check_winner(player):
    """Check if the specified player has won the game."""
    # Check horizontally
    for row in range(ROWS):
        for col in range(COLS - 3):
            if (
                board[row][col] == player
                and board[row][col + 1] == player
                and board[row][col + 2] == player
                and board[row][col + 3] == player
            ):
                return True

    # Check vertically
    for col in range(COLS):
        for row in range(ROWS - 3):
            if (
                board[row][col] == player
                and board[row + 1][col] == player
                and board[row + 2][col] == player
                and board[row + 3][col] == player
            ):
                return True

    # Check diagonally (positive slope)
    for row in range(ROWS - 3):
        for col in range(COLS - 3):
            if (
                board[row][col] == player
                and board[row + 1][col + 1] == player
                and board[row + 2][col + 2] == player
                and board[row + 3][col + 3] == player
            ):
                return True

    # Check diagonally (negative slope)
    for row in range(3, ROWS):
        for col in range(COLS - 3):
            if (
                board[row][col] == player
                and board[row - 1][col + 1] == player
                and board[row - 2][col + 2] == player
                and board[row - 3][col + 3] == player
            ):
                return True

    return False


def handle_click(col):
    """Handle button click event."""
    global current_player, game_over

    if not game_over:
        for row in range(ROWS - 1, -1, -1):
            if board[row][col] == "":
                board[row][col] = current_player
                button = buttons[row][col]
                button.config(text=current_player, state="disabled")
                button.config(bg="red" if current_player == PLAYER1 else "yellow")
                break

        if check_winner(current_player):
            game_over = True
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
        elif all(board[row][col] != "" for row in range(ROWS) for col in range(COLS)):
            game_over = True
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            current_player = PLAYER2 if current_player == PLAYER1 else PLAYER1


def restart_game():
    """Reset the game board and variables for a new game."""
    global board, current_player, game_over

    board = [["" for _ in range(COLS)] for _ in range(ROWS)]
    current_player = PLAYER1
    game_over = False

    for row in range(ROWS):
        for col in range(COLS):
            button = buttons[row][col]
            button.config(text="", state="normal", bg="SystemButtonFace")


# Create the buttons for the game board
buttons = []
for row in range(ROWS):
    button_row = []
    for col in range(COLS):
        button = tk.Button(
            window,
            text="",
            width=10,
            height=4,
            relief="ridge",
            bd=4,
            command=lambda c=col: handle_click(c),
            state="normal",
        )
        button.grid(row=row, column=col, padx=4, pady=4)
        button_row.append(button)
    buttons.append(button_row)

# Create the restart button
restart_button = tk.Button(
    window,
    text="Restart",
    width=10,
    height=2,
    relief="ridge",
    bd=4,
    command=restart_game,
)
restart_button.grid(row=ROWS, columnspan=COLS, padx=4, pady=8)

# Start the main loop
window.mainloop()
