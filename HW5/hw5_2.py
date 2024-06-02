#hw5_2
#經濟系大三 D54101039朱郁庭

import random

#用0.3的機率隨機設定懲罰的位置
def create_board(length=30, penalty_prob=0.3):
    board = {}
    for i in range(length):
        board[i] = 'P' if random.random() < penalty_prob else '_'
    return board

#印出每一局遊戲
def print_board(board, pos_a, pos_b, skip_a, skip_b,roll_a,roll_b):
    board_repr = []
    for i in range(len(board)):
        if i == pos_a and i == pos_b:
            board_repr.append('X' if board[i] == '_' else 'x')
        elif i == pos_a:
            board_repr.append('A' if board[i] == '_' else 'a')
        elif i == pos_b:
            board_repr.append('B' if board[i] == '_' else 'b')
        else:
            board_repr.append('_')
    print(''.join(board_repr),"(A: %d, B: %d)" % (roll_a,roll_b))
    
#隨機投骰子
def roll_dice():
    return random.randint(1, 6)

#主要遊戲程式
def play_game():
    board = create_board()
    pos_a, pos_b = 0, 0
    skip_a, skip_b = False, False
    
    while pos_a < len(board) - 1 and pos_b < len(board) - 1:
        #Ａ先開始
        if not skip_a:
            roll_a = roll_dice()
            pos_a = min(pos_a + roll_a, len(board) - 1)
            skip_a = board[pos_a] == 'P'
        else:
            skip_a = False
            roll_a=0
        
        #Ｂ再開始
        if not skip_b:
            roll_b = roll_dice()
            pos_b = min(pos_b + roll_b, len(board) - 1)
            skip_b = board[pos_b] == 'P'
        else:
            skip_b = False
            roll_b=0
        
        #印出當下結果
        print_board(board, pos_a, pos_b, skip_a, skip_b,roll_a,roll_b)

        #如果有人抵達最後一格，就結束遊戲
        if pos_a==len(board)-1 or pos_b==len(board)-1:
        	break
    
    #印出遊戲結果
    print()
    if pos_a == len(board) - 1 and pos_b == len(board) - 1:
        print("Both players reached the end! It's a tie!")
    elif pos_a == len(board) - 1:
        print("Player A wins!")
    else:
        print("Player B wins!")
    print()
    
    #印出有懲罰的格子
    revealed_board = ['P' if board[i] == 'P' else '_' for i in range(len(board))]
    print(''.join(revealed_board))

#開始遊戲
play_game()
