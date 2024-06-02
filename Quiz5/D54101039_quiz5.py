#D54101039_Quiz5
#經濟系大三 D54101039朱郁庭

#輸入n*n的大小
grid=int(input("Enter the size of the grid: "))
#建立空串列並設定初始值為"_"
matrix=[]
for a in range(grid):
	for b in range(grid):
		matrix+="_"
#定義函式印出當前狀況
ans=""
def print_answer(ans,grid):
	for i in range(grid):
		for j in range(grid):
			ans+=matrix[i*grid+j]+" "
		if i!=grid-1:
			ans+="\n"
	print(ans)
#一開始印出初始狀態
print_answer(ans,grid)
#進入迴圈
while True:
	#輸入位置
	cell=input("Enter the cell coordinates to edit: ")
	#結束遊戲
	if cell=="done":
		break
	#分開位置並輸入要印出的東西
	else:
		cell=cell.split(",")
		value=input("Enter the new value for the cell: ")
		#改變位置的東西
		matrix[int(cell[0])*grid+int(cell[1])]=value
		#印出結果
		print_answer(ans,grid)
