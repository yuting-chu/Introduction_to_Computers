#hw6_2
#經濟系大三 D54101039朱郁庭

import random

#根據長寬設置一個全部都是0的板子
def initialize_board(height, width):
    return [[0 for _ in range(width)] for _ in range(height)]

#印出現在遊戲狀況
def print_board(board):
    for row in board:
        print(" ".join(f"{num:2d}" for num in row))
    print()

#只要數字為0就填隨機數字
def fill_board(board, candy_types):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                board[i][j] = random.randint(1, candy_types)

#尋找可以消除的糖果
def find_candies_to_crush(board):
    to_crush = set()
    height, width = len(board), len(board[0])

    #找水平方向相連的糖果
    for i in range(height):
        for j in range(width - 2):
            if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i][j+2]:
                to_crush.update([(i, j), (i, j+1), (i, j+2)])

    #找垂直方向相連的糖果
    for i in range(height - 2):
        for j in range(width):
            if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i+2][j]:
                to_crush.update([(i, j), (i+1, j), (i+2, j)])
                
    return to_crush

#將消除的糖果設為0
def crush_candies(board, to_crush):
    for i, j in to_crush:
        board[i][j] = 0

#讓0上面的糖果掉下去
def drop_candies(board, candy_types):
    width = len(board[0])
    for j in range(width):
        idx = len(board) - 1
        for i in range(len(board) - 1, -1, -1):
            if board[i][j] != 0:
                board[idx][j] = board[i][j]
                idx -= 1
        for i in range(idx, -1, -1):
            board[i][j] = random.randint(1, candy_types)

#主要遊戲程式
def play_game(height, width, candy_types, max_moves):
    #先根據輸入的值建立一個全部都是0的空白板子
    board = initialize_board(height, width)
    #填滿數字
    fill_board(board, candy_types)
    #開始玩遊戲並紀錄次數和分數
    score = 0
    moves = 0
    while moves < max_moves:
        print("\n")
        print_board(board)
        print(f"Score: {score}\n")
        
        #輸入要交換的位置，如果不符合格式，則重新輸入
        try:
            x1, y1, x2, y2 = map(int, input("Enter the coordinates of the two adjacent candies to switch (col1 row1 col2 row2): ").split())
        except ValueError:
            print("Invalid input. Please enter four integers separated by spaces.")
            continue
        
        #如果並非兩個相鄰的格子，則重新輸入
        if not ((x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1)):
            print("Invalid move. Candies must be adjacent.")
            continue
        
        #交換糖果
        board[x1][y1], board[x2][y2] = board[x2][y2], board[x1][y1]
        
        #如果有三個以上的糖果相連則消掉
        while True:
            #找相連的糖果，如果沒有就結束
            to_crush = find_candies_to_crush(board)
            if not to_crush:
                break
            #分數計算為消掉多少數量的糖果
            score += len(to_crush)
            #將消掉的糖果設為0
            crush_candies(board, to_crush)
            #將0上面的數字向下移動
            drop_candies(board, candy_types)
        
        moves += 1
    
    #遊戲結束
    print("Game over!")
    print(f"Final Score: {score}")
    print_board(board)

#輸入想要的高度、寬度以及糖果的種類數
height = int(input("Enter the height of the board: "))
width = int(input("Enter the width of the board: "))
candy_types = int(input("Enter the number of candy types: "))
max_moves = 100
    
#開始遊戲
play_game(height, width, candy_types, max_moves)