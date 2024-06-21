#hw6_1
#經濟系大三 D54101039朱郁庭

#消掉糖果的函式
def candyCrush(board):
    while True:
        to_crush = set()
        
        #消掉水平部分的糖果
        for i in range(len(board)):
            for j in range(len(board[0]) - 2):
                if board[i][j] != 0 and board[i][j] == board[i][j+1] == board[i][j+2]:
                    to_crush.update([(i, j), (i, j+1), (i, j+2)])
        
        #消掉垂直部分的糖果
        for i in range(len(board) - 2):
            for j in range(len(board[0])):
                if board[i][j] != 0 and board[i][j] == board[i+1][j] == board[i+2][j]:
                    to_crush.update([(i, j), (i+1, j), (i+2, j)])
        
        # I全部刪完就結束函式
        if not to_crush:
            break
        
        #把消掉的糖果變成0
        for i, j in to_crush:
            board[i][j] = 0
        
        #當0上面有其他糖果，則讓上面所有糖果往下移
        for j in range(len(board[0])):
            idx = len(board) - 1
            for i in range(len(board) - 1, -1, -1):
                if board[i][j] != 0:
                    board[idx][j] = board[i][j]
                    idx -= 1
            for i in range(idx, -1, -1):
                board[i][j] = 0

    return board

#輸入要讀的檔案
filename = input("Input candy file name (e.g., candy_input1.txt or candy_input2.txt): ")

#將檔案中的資料用逗點隔開，存到input_board變數中
input_board = []
with open(filename, 'r') as file:
    for line in file:
        row = list(map(int, line.strip().split(',')))
        input_board.append(row)

#透過函式寫出跑完的結果
output_board = candyCrush(input_board)

#把結果存成txt，並加入逗點變成跟input一樣的格式
output_filename = f"candy_output{filename[-5]}.txt"  # Use the penultimate character to determine the output file name
with open(output_filename, 'w') as file:
    for row in output_board:
        file.write(','.join(map(str, row)) + '\n')

print(f"Output written to {output_filename}")