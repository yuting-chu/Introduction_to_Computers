#hw2_p5_1
#經濟系大三 D54101039朱郁庭

#輸入n的值並轉換成整數形式
n=int(input("Input an integer number: "))

#用遞迴的方式運算結果
number=0
a=0
b=1
i=1
while i<n:
	number=a+b
	a=b
	b=number
	i+=1

#輸出結果
print("The",n,"- th Fibonacci sequence number is:",number)