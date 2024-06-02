#輸入芮氏規模，同時轉換成float，並輸出芮氏規模
rsv=float(input("Please input a Richter scale value: "))
print("Richter scale value: ",rsv)

#用輸入的芮氏規模計算能量，並輸出焦耳數
energy=10**(1.5*rsv+4.8)
print("Equivalence in Joules: ",energy)

#用算出的焦耳數計算相同能量的tnt數量，並輸出結果
tnt=energy/(4.184*10**9)
print("Equivalence in tons of TNT: ",tnt)


#用算出的焦耳數計算相同能量的午餐數量，並輸出結果
lunch=energy/2930200
print("Equivalence in the number of nutritious lunches: ",lunch)
