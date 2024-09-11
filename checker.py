
from numpy import random
def build_board(size):
    """
    Create a game board of the given size filled with random checkers.
    Each cell is randomly filled with 'Empty', 'Red', or 'Black'.
    """
    # List of possible values for each cell
    options = ['Empty', 'Red', 'Black']

    # Create a board of the specified size with random choices from the options list
    board = random.choice(options, (size, size))

    return board


def get_count(board, item):
    """
    Count the number of cells with a specific item ('Empty', 'Red', or 'Black') in the board.
    """
    count = 0
    # Loop through each row and cell in the board to count the occurrences
    for row in board:
        count += list(row).count(item)
    return count


# This code runs only if this file is executed directly
if __name__ == "__main__":
    print("checkers.py is not intended to be run as a main script.")

import checkers  # Import everything from checkers.py


def game():
    # Ask the user to enter the size of the board
    while True:
        try:
            size = int(input("Enter the size of the board (between 4 and 16): "))
            if 4 <= size <= 16:
                break
            else:
                print("Please enter a number between 4 and 16.")
        except ValueError:
            print("Invalid input. Please enter a number between 4 and 16.")

    # Create the game board using the build_board function
    board = checkers.build_board(size)

    # Print the game board
    print("\nGenerated Game Board:")
    print(board)

    # Print the count of each type of cell
    print(f"\nNumber of Empty cells: {checkers.get_count(board, 'Empty')}")
    print(f"Number of Red cells: {checkers.get_count(board, 'Red')}")
    print(f"Number of Black cells: {checkers.get_count(board, 'Black')}")


# This code runs only if this file is executed directly
if __name__ == "__main__":
    game()
