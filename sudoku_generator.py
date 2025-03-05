import random
import numpy as np

# This function generates nine 3x3 solved sudokus and with respect to selected difficulty it removes some amount of cells from it
def generator(difficulty_num):
    # Converting numeric difficulties to strings
    difficulty_map = {
        1: 'easy',
        2: 'medium',
        3: 'hard',
        4: 'extreme'
    }
    difficulty = difficulty_map.get(difficulty_num, 'easy')

    base = 3
    side = base * base

    # Here r represents rows and c represents columns, the cell values are getting calculated in this sub-function
    def pattern(r, c):
        return (base * (r % base) + r // base + c) % side

    # This function shuffles three lists containing ints from 1-9 so that the sudoku maintains it's integrity across rows and columns
    def shuffle(s):
        return random.sample(s, len(s))

    rows = [g * base + r for g in shuffle(range(base)) for r in shuffle(range(base))]
    cols = [g * base + c for g in shuffle(range(base)) for c in shuffle(range(base))]
    nums = shuffle(range(1, base * base + 1))

    # Converting the shuffled lists into arrays for efficiency
    grid = [[nums[pattern(r, c)] for c in cols] for r in rows]
    grid = np.array(grid)

    # Here the cells are getting removed respectfully with the difficulty selected
    cells_to_remove = {
        'easy': 30,
        'medium': 45,
        'hard': 55,
        'extreme': 65
    }

    # Copying the official generated sudoku for later as the solution
    solution = grid.copy()

    cells_to_remove_count = cells_to_remove.get(difficulty, 30)
    cells = [(i, j) for i in range(9) for j in range(9)]
    cells_to_remove = random.sample(cells, cells_to_remove_count)

    # After declaring which cells to remove, here they are getting set by 0
    for i, j in cells_to_remove:
        grid[i][j] = 0

    return grid, solution

# This is the display function for better understanding of the puzzle, separating every 3x3 sudoku from each other
def psudoku(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + " ", end="")

# Here is the main loop function which takes inputs from the users for sudoku generation and even asks them if they want to see the solution or not
def main():
    while True:
        try:
            difficulty = int(input(
                "Please enter the number of the difficulty of your sudoku to be generated or quit:\n"
                "0. Quit\n"
                "1. Easy\n"
                "2. Medium\n"
                "3. Hard\n"
                "4. Extreme\n"))

            if difficulty == 0:
                print("Thanks for playing!")
                break

            if difficulty not in [1, 2, 3, 4]:
                print("Please enter a valid number (0-4)")
                continue

            puzzle, solution = generator(difficulty)
            print("\nHere's your generated sudoku:")
            psudoku(puzzle)

            while True:
                show_solution = input("\nWould you like to see the solution? (yes/no): ").lower()
                if show_solution in ['yes', 'no']:
                    break
                print("Please enter 'yes' or 'no'")

            if show_solution == 'yes':
                print("\nSolution:")
                psudoku(solution)

        except ValueError:
            print("Please enter a valid number")


if __name__ == "__main__":
    main()