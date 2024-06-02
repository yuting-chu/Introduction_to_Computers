#輸入一開始的歡迎字串
print("Welcome to the simple calculator program!")

#開始迴圈
while True:
	#輸入需要的數字跟符號
	num1=float(input("Enter the first number: "))
	num2=float(input("Enter the second number: "))
	operation=input("Select an arithmetic operation (+, -, *, /): ")

	#不同符號進行不同運算
	if operation=="+":
		result=num1+num2
	elif operation=="-":
		result=num1-num2
	elif operation=="*":
		result=num1*num2
	elif operation=="/":
		if num2!=0:
			result=num1/num2
		#如果除數等於0無法運算，並重新輸入數字
		elif num2==0:
			print("Error:Division by zero!")
			continue

	#印出結果
	print("Result: ",result)

	#詢問是否繼續遊戲
	another=input("Do you want to perform another calculation? (yes or no):")
	#繼續遊戲
	if another=="yes":
		continue
	#退出遊戲
	else:
		print("Goodbye!")
		break
