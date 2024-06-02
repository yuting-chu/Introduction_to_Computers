#hw2_p5_2
#經濟系大三 D54101039朱郁庭

#輸入字串
string=input("Enter the string: ")

#新增空字串palindrome來存取答案以及其他方便計算的變數
palindrome=""
i=0
j=-1
a=0
b=0

#找答案
while i<len(string):
	while len(palindrome)==0:
		#18-21用來找答案的開頭跟結尾
		if string[i] == string[j] and i!=len(string)+j:
			palindrome+=string[i]
			a=i+1
			b=j-1

			#找到開頭結尾後確認中間字母全部都符合，如果不符合就將答案清空，回到上一層迴圈找新的開頭跟結尾
			while a<=len(string)+j:
				if string[a]!=string[b]:
					palindrome=""
					break
				else:
					palindrome+=string[a]						
				a+=1
				b-=1
		j-=1
		if -j==len(string):
			j=-1
			break
	i+=1

#輸出結果
print("Longest palidrome substring is:",palindrome)
print("Length is:",len(palindrome))