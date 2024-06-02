#hw3_p1
#經濟系大三 D54101039朱郁庭

#輸入需要的值並轉換成整數型態
n=int(input("Input the total number of students (n>0): "))

#建立n人的數列
ID=[]
i=1
while len(ID)<n:
	ID=ID+[i]
	i+=1

#用迴圈每三個人就刪除一個，刪到只剩下一個
k=0
while len(ID)>1:
	del ID[2-k:n:3]
	#用k紀錄總數除以三的餘數，在下一次計算時就可以知道從第幾位開始算
	k+=n%3
	k=k%3
	n=len(ID)

#印出結果
print("The last ID is: ",ID[0])
