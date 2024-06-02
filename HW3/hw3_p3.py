#hw3_p3
#經濟系大三 D54101039朱郁庭

#建立新的6*7串列
ans=[[' ']*6,[' ']*6,[' ']*6,[' ']*6,[' ']*6,[' ']*6,[' ']*6]

#預設X先開始
xo="X"
col=7
winner=0
draw=0

#進入遊戲
while True:
	#畫出遊戲狀態
	i=0
	while i<7:
		print("+---+---+---+---+---+---+---+")
		if i==6:
			print("  0   1   2   3   4   5   6")
		else:
			print("|",ans[0][5-i],"|",ans[1][5-i],"|",ans[2][5-i],"|",ans[3][5-i],"|",ans[4][5-i],"|",ans[5][5-i],"|",ans[6][5-i],"|")
		i+=1

	#如果有贏家或平手則退出while迴圈結束遊戲
	print("\n")
	if winner=="X" or winner=="O":
		break
	if draw==42:
		break
	
	#檢查X連線
	if xo=="O":	
		while True:
			#檢查直線有沒有連線
			a=0
			while a<7:
				count=0
				max=0
				num=0
				b=0
				while b<6:
					if ans[a][b]==("X" or "x"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[a][num-c]
						ans[a].insert(num-c,"x")
					winner="X"
				a+=1

			#檢查橫線有沒有連線
			a=0
			while a<6:
				count=0
				max=0
				num=0
				b=0
				while b<7:
					if ans[b][a]==("X" or "x"):
						count+=1
						if max<count:
							max=count
						num=b					
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[num-c][a]
						ans[num-c].insert(a,"x")
					winner="X"
				a+=1

			#檢查左下右上有沒有連線
			#[1,0]->[6,5],[2,0]->[6,4],[3,0]->[6,3]
			a=0
			while a<3:
				count=0
				max=0
				num=0
				b=0
				while b<6-a:
					if ans[a+b+1][b]==("X" or "x"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[a+num-c+1][num-c]
						ans[a+num-c+1].insert(num-c,"x")
					winner="X"
				a+=1
			#[0,0]->[5,5],[0,1]->[4,5],[0,2]->[3,5]
			a=0
			while a<3:
				count=0
				max=0
				num=0
				b=0
				while b<6-a:
					if ans[b][a+b]==("X" or "x"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[num-c][a+num-c]
						ans[num-c].insert(a+num-c,"x")
					winner="X"
				a+=1

			#檢查右下左上有沒有連線
			#[5,0]->[0,5],[4,0]->[0,4],[3,0]->[0,3]
			a=0
			while a<3:
				count=0
				max=0
				num=0
				b=0
				while b<6-a:
					if ans[5-a-b][b]==("X" or "x"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[a+5-num+c][num-c]
						ans[a+5-num+c].insert(num-c,"x")
					winner="X"
				a+=1

			#[6,0]->[1,5],[6,1]->[2,5],[6,2]->[3,5]
			a=0
			while a<3:
				count=0
				max=0
				num=0
				b=0
				while b<6-a:
					if ans[6-b][a+b]==("X" or "x"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[6-num+c][a+num-c]
						ans[6-num+c].insert(a+num-c,"x")
					winner="X"
				a+=1
			break

	#檢查O連線
	if xo=="X":	
		while True:
			#檢查直線有沒有連線
			a=0
			while a<7:
				count=0
				max=0
				num=0
				b=0
				while b<6:
					if ans[a][b]==("O" or "o"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[a][num-c]
						ans[a].insert(num-c,"o")
					winner="O"
				a+=1

			#檢查橫線有沒有連線
			a=0
			while a<6:
				count=0
				max=0
				num=0
				b=0
				while b<7:
					if ans[b][a]==("O" or "o"):
						count+=1
						if max<count:
							max=count
						num=b					
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[num-c][a]
						ans[num-c].insert(a,"o")
					winner="O"
				a+=1

			#檢查左下右上有沒有連線
			#[1,0]->[6,5],[2,0]->[6,4],[3,0]->[6,3]
			a=0
			while a<3:
				count=0
				max=0
				num=0
				b=0
				while b<6-a:
					if ans[a+b+1][b]==("O" or "o"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[a+num-c+1][num-c]
						ans[a+num-c+1].insert(num-c,"o")
					winner="O"
				a+=1

			#[0,0]->[5,5],[0,1]->[4,5],[0,2]->[3,5]
			a=0
			while a<3:
				count=0
				max=0
				num=0
				b=0
				while b<6-a:
					if ans[b][a+b]==("O" or "o"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[num-c][a+num-c]
						ans[num-c].insert(a+num-c,"o")
					winner="O"
				a+=1

			#檢查右下左上有沒有連線
			#[5,0]->[0,5],[4,0]->[0,4],[3,0]->[0,3]
			a=0
			while a<3:
				count=0
				max=0
				num=0
				b=0
				while b<6-a:
					if ans[5-a-b][b]==("O" or "o"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
					b+=1
				if max>=4:
					for c in range(max):
						del ans[a+5-num+c][num-c]
						ans[a+5-num+c].insert(num-c,"o")
					winner="O"
				a+=1

			#[6,0]->[1,5],[6,1]->[2,5],[6,2]->[3,5]
			a=0
			while a<3:
				count=0
				max=0
				num=0
				b=0
				while b<6-a:
					if ans[6-b][a+b]==("O" or "o"):
						count+=1
						if max<count:
							max=count
						num=b						
					else:
						count=0
						b+=1
				if max>=4:
					for c in range(max):
						del ans[6-num+c][a+num-c]
						ans[6-num+c].insert(a+num-c,"o")
					winner="O"
				a+=1
			break

	#沒有贏家的話讓玩家輸入
	if winner!="X" and winner!="O":
		col=7
		if xo=="X":
			while True:
				col=input("Player X >> ")
				#print("\n")
				if col[0]>="0" and col[0]<="9":
					col=int(col)
				else:
					print("\nInvalid input, try again [0‐6].\n")
					continue
				if col>6 or col<0:
					print("\nOut of range, try again [0‐6].\n")
					continue
				if ans[col][5]!=" ":
					print("\nThis column is full. Try another column.\n")
					continue
				else:
					j=0
					while ans[col][j]!=" ":
						j+=1
					ans[col][j]="X"
					xo="O"
					draw+=1
				break


		elif xo=="O":
			while True:
				col=input("Player O >> ")
				#print("\n")
				if col[0]>="0" and col[0]<="9":
					col=int(col)
				else:
					print("Invalid input, try again [0‐6].")
					continue
				if col>6 or col<0:
					print("Out of range, try again [0‐6].")
					continue
				if ans[col][5]!=" ":
					print("This column is full. Try another column.")
					continue
				else:
					j=0
					while ans[col][j]!=" ":
						j+=1
					ans[col][j]="O"
					xo="X"
					draw+=1
				break

if draw==42:
	print("Draw")
else:
	print("Winner: ",winner)

