#hw1_p2
#經濟系大三 D54101039朱郁庭

#輸入force,m1,distance的值，並轉換成float
force = float(input("Input the force: "))
m1 = float(input("Input the mass of m1: "))
distance = float(input("Input the distance: "))

#輸入的值計算出m2,energy
m2 = force*distance**2/m1/(6.67*10**-11)
energy = m2*299792458**2

#印出結果
print("The mass of m2 = ",m2)
print("The energy of m2 = ",energy)