import curses
import random

try:
    import curses
except ImportError:
    import windows_curses as curses

def main(stdscr):
    # Initialize curses
    curses.curs_set(0)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Grey color for the snake
    sh, sw = stdscr.getmaxyx()
    w = curses.newwin(sh, sw, 0, 0)
    w.keypad(1)
    w.timeout(100)

    # Snake initial position and size
    snk_x = sw // 4
    snk_y = sh // 2
    snake = [
        [snk_y, snk_x],
        [snk_y, snk_x - 1],
        [snk_y, snk_x - 2]
    ]

    # Initial food position
    food = [sh // 2, sw // 2]
    special_food = [sh // 4, sw // 4]
    w.addch(food[0], food[1], 'π')
    w.addch(special_food[0], special_food[1], 'X')

    # Obstacles
    obstacles = []
    num_obstacle_cells = (sh * sw) // 20  # 5% of the game screen
    while len(obstacles) < num_obstacle_cells:
        if random.choice([True, False]):
            # Horizontal obstacle
            start_y = random.randint(1, sh - 2)
            start_x = random.randint(1, sw - 6)
            new_obstacle = [[start_y, start_x + i] for i in range(5)]
        else:
            # Vertical obstacle
            start_y = random.randint(1, sh - 6)
            start_x = random.randint(1, sw - 2)
            new_obstacle = [[start_y + i, start_x] for i in range(5)]

        if all(cell not in obstacles and cell not in snake for cell in new_obstacle):
            obstacles.extend(new_obstacle)

    for obstacle in obstacles:
        w.addch(obstacle[0], obstacle[1], ' ', curses.color_pair(1))

    # Game control variables
    key = curses.KEY_RIGHT
    prev_key = key
    paused = False
    normal_food_eaten = 0
    special_food_eaten = 0
    game_end_reason = ""

    # Game loop
    while True:
        next_key = w.getch()
        key = key if next_key == -1 else next_key

        if key == ord(' '):
            paused = not paused

        if paused:
            key = prev_key
            continue

        if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, 27]:
            key = prev_key

        # Calculate the new head position
        y = snake[0][0]
        x = snake[0][1]
        if key == curses.KEY_DOWN:
            y += 1
        if key == curses.KEY_UP:
            y -= 1
        if key == curses.KEY_LEFT:
            x -= 1
        if key == curses.KEY_RIGHT:
            x += 1

        # Wrap around the screen boundaries
        y = y % sh
        x = x % sw

        # Insert new head
        new_head = [y, x]

        # Check for collision with self or obstacles
        if new_head in snake:
            game_end_reason = "Hit Self"
            break
        if new_head in obstacles:
            game_end_reason = "Hit Obstacle"
            break

        snake.insert(0, new_head)

        # Check if snake eats food
        if snake[0] == food:
            normal_food_eaten += 1
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                food = nf if nf not in snake and nf not in obstacles else None
            w.addch(food[0], food[1], 'π')
        else:
            tail = snake.pop()
            w.addch(tail[0], tail[1], ' ')

        # Check if snake eats special food
        if snake[0] == special_food:
            special_food_eaten += 1
            if len(snake) > 1:
                tail = snake.pop()
                w.addch(tail[0], tail[1], ' ')  # Remove the tail segment immediately
            special_food = None
            while special_food is None:
                sf = [
                    random.randint(1, sh - 2),
                    random.randint(1, sw - 2)
                ]
                special_food = sf if sf not in snake and sf not in obstacles else None
            w.addch(special_food[0], special_food[1], 'X')

        # Display the snake in grey
        w.addch(snake[0][0], snake[0][1], '#', curses.color_pair(2))

        prev_key = key

    # End of game
    curses.endwin()
    print(f"Game over because of {game_end_reason}")
    print(f"You ate {normal_food_eaten} normal foods and {special_food_eaten} special foods.")

# Run the game
curses.wrapper(main)
