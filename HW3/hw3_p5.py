#hw3_p5
#經濟系大三 D54101039朱郁庭

#輸入值，並轉換成數字形式<順便紀錄最大值以及總數
seats=input("Input sequence of seats: ")
seats=seats.split(" ")
i=0
max=0
total=0
length=len(seats)
while i<length:
	num=int(seats[i])
	total+=num
	if num>max:
		max=num
	del seats[i]
	seats.insert(i,num)
	i+=1

#一開始先假設全部面積都是水
water=max*length

#再從高到低扣除空白的部分
j=max
while j>0:
	a=length
	b=0
	k=0
	while k<length:
		if seats[k]>=j:
			if a>k:
				a=k
			if b<k:
				b=k
		k+=1
	water-=(length-(b-a+1))
	j-=1

#最後扣除黑色總數，結果就會是水
water-=total

#輸出結果
print("Water: ",water)

