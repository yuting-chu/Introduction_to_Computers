#D54101039_Quiz4
#經濟系大三 D54101039朱郁庭

#輸入一系列整數，並用空格隔開
num=input("Enter a sequence of integers separated by whitespace: ")
#將空格刪除
num=num.split(" ")

#建立兩個串列，第一個用來存最長的連續遞增串列，第二個用來記錄新的串列
#一開始的b串列從num第一個數字開始
a=[]
b=[int(num[0])]

#開始跑所有的數字
for i in range(len(num)):
	#當前數字比前一個數字小就存進b串列
	if int(num[i])>b[-1]:
		b+=[int(num[i])]
	#當前數字比前一個數字大或等於
	else:
		#如果b串列比a串列更長，則將b複製成a
		if len(b)>len(a):
			a=b
		#如果一樣長，則比較最後一個數字大小
		elif len(b)==len(a):
			if b[-1]>a[-1]:
				a=b
		#將b改成當前數字，開始找新的新的串列
		b=[int(num[i])]
	#到最後一個數字時，比較目前b串列和a串列
	if i == len(num)-1:
		if len(b)>len(a):
			a=b
		elif len(b)==len(a):
			if b[-1]>a[-1]:
				a=b

#輸出答案
print("Length:",len(a))
print("LICS:",a)