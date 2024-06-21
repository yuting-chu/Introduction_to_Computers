import random

def read_maze_file(filename,x_num):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        maze = []
        for i in range(1, len(lines), 2):
            row = []
            line = lines[i]
            for j in range(2, len(line), 4):
                if line[j] == ' ':
                    row.append(0)
                elif line[j] == 'X':
                    row.append(1)
                    x_num+=1
            if row:
                maze.append(row)
        return maze,x_num
    except IOError:
        print("IOEError occured in main function. File not found or could not be read.")
        return None

def get_maze_dimensions(maze):
    N = len(maze)
    M = len(maze[0]) if N > 0 else 0
    return N, M

def generate_path(N, M):
    maze = [[0 for _ in range(M)] for _ in range(N)]
    i, j = 0, 0
    maze[i][j] = 2
    while i < N-1 or j < M-1:
        if i == N-1:
            j += 1
        elif j == M-1:
            i += 1
        else:
            if random.choice([True, False]):
                i += 1
            else:
                j += 1
        maze[i][j] = 2
    return maze

def add_obstacles(maze, num_obstacles):
    count = 0
    while count < num_obstacles:
        row = random.randint(0, len(maze) - 1)
        col = random.randint(0, len(maze[0]) - 1)
        if maze[row][col] == 0:
            maze[row][col] = 1
            count += 1
    return maze

def generate_maze(N, M, num_obstacles):
    maze = generate_path(N, M)
    maze = add_obstacles(maze, num_obstacles)
    return maze

def print_maze(maze):
    print("+" + "---+" * len(maze[0]))
    for row in maze:
        row_str = "|"
        for cell in row:
            if cell == 0:
                row_str += "   "
            elif cell == 1:
                row_str += " X "
            elif cell == 2:
                row_str += " O "
            row_str += "|"
        print(row_str)
        print("+" + "---+" * len(maze[0]))

def set_obstacle(maze, N, M):
    while True:
        try:
            i, j = map(int, input("Enter the coordinates to set an obstacle, e.g. i,j: ").split(","))
            if 0 <= i < N and 0 <= j < M:
                if maze[i][j] == 2:
                    print("Obstsacle cannot be placed on the path.")
                elif maze[i][j] == 1:
                    print("Obstacle already exists at the location.")
                else:
                    maze[i][j] = 1
                    print(f"Obstacle set at ({i}, {j})")
                    print_maze(maze)
                    break
            else:
                print("KeyError in set_obstacle function. 'Invalid coordinates. Please input coordinates within the range.'")
        except ValueError:
            print("ValueError in set_obstacle function. Need to be coordinates")

def remove_obstacle(maze, N, M):
    while True:
        try:
            i, j = map(int, input("Enter the coordinates to remove an obstacle, e.g. i,j: ").split(","))
            if 0 <= i < N and 0 <= j < M:
                if maze[i][j] == 1:
                    maze[i][j] = 0
                    print(f"Obstacle removed at ({i}, {j})")
                    print_maze(maze)
                    break
                else:
                    print("Obstacle does not exist at this location.")
            else:
                print("KeyError in remove_obstacle function. 'Invalid coordinates. Please input coordinates within the range.'")
        except ValueError:
            print("ValueError in remove_obstacle function. Need to be coordinates")

def main():
    while True:
        x_num=0
        filename = input("Enter the filename of the maze blueprint: ")
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
            maze = []
            for i in range(1, len(lines), 2):
                row = []
                line = lines[i]
                for j in range(2, len(line), 4):
                    if line[j] == ' ':
                        row.append(0)
                    elif line[j] == 'X':
                        row.append(1)
                        x_num+=1
                if row:
                    maze.append(row)
        except IOError:
            print("IOEError occured in main function. File not found or could not be read.")
            continue
        break
    
    N, M = get_maze_dimensions(maze)
    max_possible_obs = N * M - (N + M - 1)-x_num
    print_maze(maze)
    while True:
        try:
            num_obstacles = int(input(f"Enter the minimum number of obstacles (0-{max_possible_obs}): "))
            if 0 <= num_obstacles <= max_possible_obs:
                break
            else:
                print(f"ValueError occurred in main function. Invalid number of obstacle.")
        except ValueError:
            print("ValueError occurred in main function. Invalid number of obstacle.")
    
    generated_maze = generate_maze(N, M, num_obstacles)
    print_maze(generated_maze)
    
    while True:
        option = input("Options:\n1. Set obstacle\n2. Remove obstacle\n3. Exit\nEnter your option: ")
        if option == "1":
            set_obstacle(generated_maze, N, M)
            
        elif option == "2":
            remove_obstacle(generated_maze, N, M)
        elif option == "3":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
