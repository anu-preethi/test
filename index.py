import logging


# Configure logging
logging.basicConfig(level=logging.INFO)

INVALID_MOVE_MSG = "Invalid move: That spot is already taken. Try again."

from typing import List

def print_board(board: List[List[str]]) -> None:
    """Print the current state of the board."""

    board_display = []
    for row in board:
        board_display.append(" | ".join(row))
        board_display.append("-" * 9)
    print("\n".join(board_display))


def check_winner(board: List[List[str]], player: str) -> bool:
    """Check if the given player has won."""

    for i in range(3):  # Check rows and columns
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def is_full(board: List[List[str]]) -> bool:
    """Check if the board is full."""

    return all(cell != " " for row in board for cell in row)


def log_invalid_input(message: str) -> None:
    """Log invalid input messages."""
    logging.warning(message)


def get_valid_input(prompt: str) -> int:
    """Get a valid input from the user."""

    while True:
        try:
            value = int(input(prompt))
            if 0 <= value < 3:  # Check if the value is within the valid range
                return value
            else:
                log_invalid_input("Invalid input: Enter a number between 0 and 2.")
        except ValueError:
            log_invalid_input("Invalid input: Please enter an integer.")


def handle_turn(board: List[List[str]], player: str) -> None:
    """Handle the turn for the current player."""

    while True:
        row = get_valid_input("Enter the row (0, 1, 2): ")
        col = get_valid_input("Enter the column (0, 1, 2): ")

        if board[row][col] == " ":
            board[row][col] = player
            break
        else:
            logging.warning(INVALID_MOVE_MSG)


def main() -> None:
    """Main function to play the game."""

    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        logging.info(f"Player {player}'s turn:")

        # Handle player turn
        handle_turn(board, player)

        if check_winner(board, player):
            print_board(board)
            logging.info(f"Player {player} wins!")
            break

        if is_full(board):
            print_board(board)
            logging.info("It's a draw!")
            break

        player = "O" if player == "X" else "X"


if __name__ == "__main__":
    main()
