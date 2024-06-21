#D54101039_朱郁庭

#把輸入的矩陣存起來
def parse_matrix(matrix_str):
    #用"|"分行
    rows = matrix_str.split('|')
    n = len(rows)
    #將矩陣用dictionary存起來，key為位置，value為輸入的數字
    matrix = {}
    for i, row in enumerate(rows):
        elements = row.split(',')
        for j, element in enumerate(elements):
            matrix[(i, j)] = int(element)
    return matrix, n

#矩陣相乘
def multiply_matrices(U, V, n):
    #先設定一個空矩陣
    M = {(i, j): 0 for i in range(n) for j in range(n)}
    #再計算每個位置的值
    for i in range(n):
        for j in range(n):
            for k in range(n):
                M[(i, j)] += U[(i, k)] * V[(k, j)]
    
    return M

#印出矩陣
def print_matrix(matrix, n):
    for i in range(n):
        row = [matrix[(i, j)] for j in range(n)]
        print(row)

U_str = input("Enter matrix U: ")
V_str = input("Enter matrix V: ")
    
U, n = parse_matrix(U_str)
V, _ = parse_matrix(V_str)
    
M = multiply_matrices(U, V, n)
    
print("M = U x V")
print_matrix(M, n)