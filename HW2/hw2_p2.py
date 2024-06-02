#hw2_p2
#經濟系大三 D54101039朱郁庭

#輸入n的值並轉換成整數形式
n=int(input("Input the range number: "))

#先輸出"Perfect numbers:"(因為只出現一次)
print("Perfect numbers:")

#先假設2是perfect number
perfect_number=2

#計算2到n的因數及因數的加總
while perfect_number<=n:
	i=1
	total_sum=0
	#計算perfect number不包含自己的因數，並將因數加總
	while i<perfect_number:
		if perfect_number%i==0:
			total_sum+=i
		i+=1
	#當加總的值等於假設的perfect number，則印出perfect number
	if total_sum==perfect_number:
		print(perfect_number)
	perfect_number+=1