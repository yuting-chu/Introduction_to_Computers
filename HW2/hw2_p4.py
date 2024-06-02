#hw2_p4
#經濟系大三 D54101039朱郁庭

#輸入需要的值並轉換成整數形式
n=int(input("Enter the number of layers(2 to 5) = "))
top=int(input("Enter the side length of the top layer = "))
growth=int(input("Enter the growth of each layer = "))
trunk_w=int(input("Enter the trunk width (odd number , 3 to 9) = "))
trunk_h=int(input("Enter the trunk height (4 to 10) = "))

#印出最上面三角形的頂點
blank=top-1+growth*(n-1)
print(' '*blank+'#')

#畫出第一顆三角形的其他部份以及下面的三角形
i=n
while i>0:
	j=1
	while j<top-1+growth*(n-i):
		print(' '*(blank-j)+'#'+'@'*(2*j-1)+'#')
		j+=1
	print(' '*(blank-j)+"#"*(2*j+1))
	i-=1

#畫出樹幹
while trunk_h>0:
	print(' '*(blank-trunk_w//2)+'|'*trunk_w)
	trunk_h-=1