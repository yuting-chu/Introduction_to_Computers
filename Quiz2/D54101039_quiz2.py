#輸入購物價格，並轉換成浮點數形式
amount=float(input("Enter the shopping amount: "))

#輸入會員級別，用字串的形式儲存
level=input("Enter the membership level (Regular or Gold): ")

#先將不同的會員等級分開，再根據不同的消費金額計算折扣
if level=="Regular":
	if amount > 3000:
		amount*=0.8
	elif amount > 2000:
		amount*=0.85
	elif amount > 1000:
		amount*=0.9
	print(level,"$",amount)
elif level =="Gold":
	if amount > 3000:
		amount*=0.75
	elif amount > 2000:
		amount*=0.8
	elif amount > 1000:
		amount*=0.85
	print(level,"$",amount)
else:
	print("Invalid membership level. Please enter 'Regular' or 'Gold'.")