#hw2_p3
#經濟系大三 D54101039朱郁庭

#輸入需要的值
year=int(input("Please input Year: "))
month=int(input("Please input Month: "))

#先印出所有星期幾
print("Sun Mon Tue Wed Thu Fri Sat")

#用公式計算當年當月的一號是星期幾，可能會因為閏年和月份會有不同的計算方式
c=2*(3-year//100%4)
leap_year=29
if year%4==0 and year%100!=0 and (month==1 or month==2):
	y=((5*year%100%28/4)//1)%7-1
elif year%400==0 and (month==1 or month==2):
	y=((5*year%100%28/4)//1)%7-1
else:
	y=((5*year%100%28/4)//1)%7
	leap_year=0

if month==1 or month==2:
	m=((3.4+(month-3)%12*2.6)//1-1)%7
else:
	m=(3.4+(month-3)%12*2.6)//1%7
mod=(int(c)+int(y)+int(m)+1)%7

#開始印出月曆，用mod來判斷從星期幾開始
calendar=""
calendar+="    "*mod

#分成不同的月份印出不同的天數
if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
	for i in range(31):
		i+=1
		format="%02d "
		calendar+=format%i
		mod+=1
		if mod==7:
			calendar+="\n"
			mod=0
		else:
			calendar+=" "
		i+=1

elif month==4 or month==6 or month==9 or month==11:
	for i in range(30):
		i+=1
		format="%02d "
		calendar+=format%i
		mod+=1
		if mod==7:
			calendar+="\n"
			mod=0
		else:
			calendar+=" "
		i+=1

#再把二月分成閏年何不是閏年
elif leap_year==29:
	for i in range(29):
		i+=1
		format="%02d "
		calendar+=format%i
		mod+=1
		if mod==7:
			calendar+="\n"
			mod=0
		else:
			calendar+=" "
		i+=1

else:
	for i in range(28):
		i+=1
		format="%02d "
		calendar+=format%i
		mod+=1
		if mod==7:
			calendar+="\n"
			mod=0
		else:
			calendar+=" "
		i+=1

#印出結果
print(calendar)