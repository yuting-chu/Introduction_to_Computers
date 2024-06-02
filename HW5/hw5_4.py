#hw5_4
#經濟系大三 D54101039朱郁庭

def evaluate_expression(expression):
    try:
        # 檢查是否有除了數字、加減乘除、括號以外的字元
        allowed_chars = "0123456789+-*/() "
        for char in expression:
            if char not in allowed_chars:
                raise ValueError("Error: Unsupported character "+char)
        
        # 檢查不平衡的括號
        if expression.count('(') != expression.count(')'):
            raise ValueError("Error: Unbalanced parentheses")
        
        # 計算算式並將結果傳到外面印出
        result = eval(expression)
        return result
    
    # 根據不同的錯誤傳回不同的結果
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Operand error"
    except ValueError as ve:
        return str(ve)

# 用while迴圈一直問問題
while True:
    expression = input("Enter an expression to evaluate or 'q' ro quit: ")
    #當結果為q就結束程式
    if expression.lower() == 'q':
        break
    #將算式放到function判斷是否有問題，並印出結果
    result = evaluate_expression(expression)
    print(result)


