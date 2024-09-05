import checker


def game():
    while True:
        try:
            size = int(input("Enter the size of the board (between 4 and 16): "))
            if 4 <= size <= 16:
                break
            else:
                print("Invalid input. Please enter a number between 4 and 16.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Build the board 
    board = checker.build_board(size)

    # Print the generated board
    print("Generated Board:")
    print(board)

    # Print counts of 'Empty', 'Red', and 'Black' 
    print(f"Empty cells count: {checker.get_count(board, 'Empty')}")
    print(f"Red cells count: {checker.get_count(board, 'Red')}")
    print(f"Black cells count: {checker.get_count(board, 'Black')}")


if __name__ == "__main__":
    game()
