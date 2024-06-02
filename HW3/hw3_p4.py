#hw3_p4
#經濟系大三 D54101039朱郁庭

#輸入需要的變數
Input=input("Enter index x,y,k (seperate by white space): ")
Input=Input.split(" ")

#輸入矩陣，並轉變成二維字串的形式
matrix=[]
print("Enter the matrix by multiple lines:")
while True:
	line=input()
	if line=="q":
		break
	line=line.split(" ")
	#在每個字串前後都加上空格，方便尋找數字
	line.insert(0," ")
	line+=[" "]
	matrix+=[line]

#計算矩陣格式
row=len(matrix)
col=len(matrix[0])-2

#儲存需要用到的數字
num=matrix[int(Input[0])][int(Input[1])+1]
color=Input[2]

#在matrix第一行和最後加入一條空白串列，方便尋找數字
matrix.insert(0,[" "]*(col+2))
matrix+=[[" "]*(col+2)]

#更改指定位置的數字
matrix[int(Input[0])+1][int(Input[1])+1]=color

#開始找附近的數字
i=0
j=0
k=0
while k<row*col:
	while i< row+1:
		while j<col+1:
			#如果matrix[i][j]數字是num且上下左右有出現color，就把matrix[i][j]改成color
			if matrix[i][j]==num and (matrix[i-1][j]==color or matrix [i+1][j]==color or matrix[i][j-1]==color or matrix[i][j+1]==color):
				del matrix[i][j]
				matrix[i].insert(j,color)
			i+=1
		j+=1
	k+=1

#刪掉輔助的空白串列
del matrix[0]
del matrix[-1]

#印出矩陣
l=0
while l<row:
	ans=" ".join(matrix[l][1:col+1])
	print(ans)

