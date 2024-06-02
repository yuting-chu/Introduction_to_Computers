#hw5_1m
#經濟系大三 D54101039朱郁庭

#import需要的模組
import random
import time

#定義各種輸出
def matrix(ans):
	print(' '*4,'a',' ','b',' ','c',' ','d',' ','e',' ','f',' ','g',' ','h',' ','i')
	for i in range(10):
		i+=1
		print(" "*3+"+---"*9+"+")
		if i!=10:
			print("",i,"|",ans[i*100+1],"|",ans[i*100+2],"|",ans[i*100+3],"|",ans[i*100+4],"|",ans[i*100+5],"|",ans[i*100+6],"|",ans[i*100+7],"|",ans[i*100+8],"|",ans[i*100+9],"|")

def help():
	print("\nEnter the column followed by the row (ex: a5). To add or remove a flag,\nadd 'f' to the cell (ex:a5f).")
def cannot_put_flag():
	print("\nCannot put a flag there")
def invalid_cell():
	print("\nInvalid cell. Enter the column followed by the row (ex: a5). To add or remove a flag, add 'f' to the cell (ex: a5f).")
def is_flag():
	print("\nThere is a flag there")
def is_shown():
	print("\nThat cell is already shown")

#進入一局遊戲
while True:
	#開始計時
	start_time=time.time()
	#建立空dictionary，key表示行跟列
	ans={}
	for i in range(11):
		for j in range(11):
			name=i*100+j
			ans[name]=" "
	#設定各種用來判斷的變數
	message=0
	h=0
	mines=[[-1,-1]]
	num=10
	f=0
	end=0
	#進入迴圈
	while True:
		#在需要時印出對應的輸出
		if message==0:
			matrix(ans)
			print("\nEnter the column followed by the row (ex: a5). To add or remove a flag,\nadd 'f' to the cell (ex:a5f). Type 'help' to show this message again.")
			message=1
		#結束遊戲
		if end==1:
			matrix(ans)
			break
		
		#印出需要輸入的問句
		if message==2:
			matrix(ans)
		sentence="\nEnter the cell ("+str(num)+" mines left): "
		cell=input(sentence)
		#輸入help重跑迴圈
		if cell=='help':
			help()
			continue
		#記錄輸入的變數
		x=int(cell[1])
		y=ord(cell[0])-ord("a")+1

		#旗子的操作，並用num紀錄是否有找到地雷
		if len(cell)==3 and cell[2]=='f':
			if ans[x*100+y]==' ':
				ans[x*100+y]='F'
				if base[x][y]=='X':
					num-=1
			elif ans[x*100+y]=='F':
				ans[x*100+y]=' '
				if base[x][y]=='X':
					num+=1
			else:
				cannot_put_flag()

			#如果找到所有的地雷，就結束遊戲
			if num==0:
				#停止計時並計算時間
				end_time=time.time()
				duration=end_time-start_time
				minute=int(duration//60)
				second=int(duration%60)
				print("\nYou win. It took you",minute,"minutes and",second,"seconds\n")
				end=1
			continue

		#正常輸入位置
		elif len(cell)==2:
			if x>10 or x<1 or y>10 or y<1:
				invalid_cell()
				continue
			elif ans[x*100+y]=='F':
				is_flag()
				continue
			elif ans[x*100+y]!=' ':
				is_shown()
				continue

		#第一次進入遊戲用random隨機放地雷，不能在第一次輸入的位置附近
		if message==1:
			i=1
			while i<11:
				row=random.randint(1,9)
				col=random.randint(1,9)
				mines+=[[row,col]]

				j=i-1
				duplicate=0
				while j>0:
					if mines[i]==mines[j]:
						duplicate+=1
					j-=1
				if ((row==x or row==x+1 or row==x-1) and (col==y or col==y+1 or col==y-1)) or duplicate>0:
					del mines[i]
					continue
				i+=1
			#建立變數幫助保留地雷的位置和每個位置的數字
			base=[[0]*11,[0]*11,[0]*11,[0]*11,[0]*11,[0]*11,[0]*11,[0]*11,[0]*11,[0]*11,[0]*11]
			for c in range(10):
				base[mines[c+1][0]][mines[c+1][1]]='X'
			for a in range(9):
				for b in range(9):
					total=0
					if base[a+1][b+1]!='X':
						for a_3 in range(3):
							for b_3 in range(3):
								if base[a+a_3][b+b_3]=='X':
									total+=1
						base[a+1][b+1]=total
			message=2	
		
		#將base[x][y]的數字複製到ans[x*100+y]
		ans[x*100+y]=base[x][y]
	
		#踩到地雷遊戲結束
		if ans[x*100+y]=='X':
			ans=base
			print("\nGame Over\n")
			end=1
			continue

		#踩到0的位置，輸出0附近的所有數字	
		elif ans[x*100+y]==0:
			for l in range(8):
				for k in range(81):
					for i in range(1,10):
						for j in range(1,10):
							if ans[i*100+j]==' ':
								if base[i][j]==l and (ans[(i+1)*100+j]==0 or ans[(i-1)*100+j]==0 or ans[i*100+j+1]==0 or ans[i*100+j-1]==0 or ans[(i-1)*100+j-1]==0 or ans[(i-1)*100+j+1]==0 or ans[(i+1)*100+j-1]==0 or ans[(i+1)*100+j+1]==0):
									ans[i*100+j]=base[i][j]

	#結束遊戲後詢問是否要在玩新的一局
	again=input("\nPlay again? (y/n): ")
	if again=='y':
		continue
	elif again=='n':
		break