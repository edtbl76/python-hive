import random


def generate_game_grid(side, bombs):
    grid = [[0 for row in range(side)] for column in range(side)]

    for num in range(bombs):
        x = random.randint(0, side - 1)
        y = random.randint(0, side - 1)
        grid[y][x] = 'X'

        # Center Right
        if 0 <= x <= 3 and 0 <= y <= 4:
            if grid[y][x + 1] != 'X':
                grid[y][x + 1] += 1

        # Center Left
        if 1 <= x <= 4 and 0 <= y <= 4:
            if grid[y][x - 1] != 'X':
                grid[y][x - 1] += 1

        # Top Left
        if 1 <= x <= 4 and 1 <= y <= 4:
            if grid[y - 1][x - 1] != 'X':
                grid[y - 1][x - 1] += 1

        # Top Right
        if 0 <= x <= 3 and 1 <= y <= 4:
            if grid[y - 1][x + 1] != 'X':
                grid[y - 1][x + 1] += 1

        # Top Center
        if 0 <= x <= 4 and 0 <= y <= 3:
            if grid[y - 1][x] != 'X':
                grid[y - 1][x] += 1

        # Bottom Right
        if 0 <= x <= 3 and 0 <= y <= 3:
            if grid[y + 1][x + 1] != 'X':
                grid[y + 1][x + 1] += 1

        # Bottom Left
        if 1 <= x <= 4 and 0 <= y <= 3:
            if grid[y + 1][x - 1] != 'X':
                grid[y + 1][x - 1] += 1

        # Bottom Center
        if 0 <= x <= 4 and 0 <= y <= 3:
            if grid[y + 1][x] != 'X':
                grid[y + 1][x] += 1

    return grid


def generate_player_map(side):
    grid = [['-' for row in range(side)] for column in range(side)]
    return grid


def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))
        print("")


def check_for_winner(grid):
    for row in grid:
        for cell in row:
            if cell == '-':
                return False
    return True


def check_continue_game(score):
    print("Score: {}".format(score))
    is_continue = input("Press n to quit, or any other key to continue")
    return is_continue.lower() == 'n'


def get_difficulty():
    difficulty = input("Select difficulty: (b)eginner, (i)intermediate, or (a)dvanced: ")
    while True:
        if difficulty.lower() == 'b':
            return 5, 3
        elif difficulty.lower() == 'i':
            return 6, 8
        elif difficulty.lower() == 'a':
            return 8, 20


def game_main():
    game_status = True

    while game_status:
        size, bomb_count = get_difficulty()

        game_grid = generate_game_grid(size, bomb_count)
        player_map = generate_player_map(size)
        score = 0

        while True:

            if not check_for_winner(player_map):
                print("Enter Cell: ")
                x = input("X COL (1 to 5) :")
                y = input("Y ROW (1 to 5) :")
                x = int(x) - 1
                y = int(y) - 1

                if game_grid[y][x] == 'X':
                    print("Game Over!")
                    print_grid(game_grid)
                    game_status = check_continue_game(score)
                    break
                else:
                    player_map[y][x] = game_grid[y][x]
                    print_grid(player_map)
                    score += 1

            else:
                print_grid(player_map)
                print("You Won!")
                game_status = check_continue_game(score)
                break


if __name__ == "__main__":
    try:
        game_main()
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')