#D54101039_Quiz6
#經濟系大三 D54101039朱郁庭

import random
#隨機選數字，數字代表小寫英文字母
ans=random.randint(97,122)
tries=0
guessing=[0,0,0,0,0,0,0]
while True:
	alphabet=input("Guess the lowercase alphabet: ")
	#如果不是小寫英文字母，就重新輸入
	if ord(alphabet)<97 or ord(alphabet)>122:
		print("Please enter a lowercase alphabet.")
		continue
	else:
		#每次嘗試都加一
		tries+=1
		#紀錄分配狀況
		record=(ord(alphabet)-97)//4
		guessing[record]+=1
		#猜得比較大
		if ord(alphabet)>ans:
			print("The alphabet you are looking for is alphabetically lower.")
			continue
		#猜得比較小
		elif ord(alphabet)<ans:
			print("The alphabet you are looking for is alphabetically higher.")
			continue
		#猜到正確答案，並印出需要的東西，然後跳出循環
		elif ord(alphabet)==ans:
			correct='Congratulations! You guessed the alphabet "'+alphabet+'" in '+str(tries)+' tries.\n'
			print(correct)
			print("Guess Histogram:")
			print("a - d:","*"*guessing[0])
			print("e - h:","*"*guessing[1])
			print("i - l:","*"*guessing[2])
			print("m - p:","*"*guessing[3])
			print("q - t:","*"*guessing[4])
			print("u - x:","*"*guessing[5])
			print("y - z:","*"*guessing[6])
			break
			