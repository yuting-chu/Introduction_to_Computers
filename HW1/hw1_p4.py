#hw1_p4
#經濟系大三 D54101039朱郁庭

#輸入height1,m1,m2的值，並轉換成float
height1=float(input("Input the height of the 1st ball: "))
m1=float(input("Input the mass of the 1st ball: "))
m2=float(input("Input the mass of the 2nd ball: "))

#根據輸入的值計算兩球的速率，並印出結果
v1=(2*9.8*height1)**0.5
v2=(m1*v1**2/m2)**0.5
print("The velocity of the 1st ball after slide: ",v1," m/s") 
print("The velocity of the 2nd ball after collision: ",v2," m/s")