#hw2_p5_3
#經濟系大三 D54101039朱郁庭

#輸入所有需要的變數
n=int(input("The number of the requested element in Fibonacci (n) = "))
s1=input("The first string for Palindromic detection (s1) = ")
s2=input("The second string for Palindromic detection (s1) = ")
word=input("The plaintext to be encrypted: ")

#用遞迴的方式運算費波納契數列的結果
number=0
a=0
b=1
i=1
while i<n:
	number=a+b
	a=b
	b=number
	i+=1

#新增空字串palindrome1來存取答案以及其他方便計算的變數
palindrome1=""
i=0
j=-1
a=0
b=0

#找第一個字串的回文
while i<len(s1):
	while len(palindrome1)==0:
		#31-35用來找答案的開頭跟結尾
		if s1[i] == s1[j] and i!=len(s1)+j:
			palindrome1+=s1[i]
			a=i+1
			b=j-1
			#找到開頭結尾後確認中間字母全部都符合，如果不符合就將答案清空，回到上一層迴圈找新的開頭跟結尾
			while a<=len(s1)+j:
				if s1[a]!=s1[b]:
					palindrome1=""
					break
				else:
					palindrome1+=s1[a]						
				a+=1
				b-=1
		j-=1
		if -j==len(s1):
			j=-1
			break
	i+=1

#新增空字串palindrome2來存取答案以及其他方便計算的變數
palindrome2=""
i=0
j=-1
a=0
b=0

#找第一個字串的回文
while i<len(s2):
	while len(palindrome2)==0:
		#62-65用來找答案的開頭跟結尾
		if s2[i] == s2[j] and i!=len(s2)+j:
			palindrome2+=s2[i]
			a=i+1
			b=j-1
			#找到開頭結尾後確認中間字母全部都符合，如果不符合就將答案清空，回到上一層迴圈找新的開頭跟結尾
			while a<=len(s2)+j:
				if s2[a]!=s2[b]:
					palindrome2=""
					break
				else:
					palindrome2+=s2[a]						
				a+=1
				b-=1
		j-=1
		if -j==len(s2):
			j=-1
			break
	i+=1

#將上面得到的數字帶入公式
encryption=""
for k in range(len(word)):
	w=ord(word[k])
	ans=(((w+number)*len(palindrome1)+len(palindrome2))-65)%26+65
	encryption+=chr(ans)


#輸出結果
print("The",n,"- th Fibonacci sequence number is:",number)
print("Longest palidrome substring within first string is:",palindrome1)
print("Length is:",len(palindrome1))
print("Longest palidrome substring within second string is:",palindrome2)
print("Length is:",len(palindrome2))
print("The plaintext to be encrypted: ",encryption)