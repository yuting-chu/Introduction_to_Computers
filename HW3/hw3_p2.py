#hw3_p2
#經濟系大三 D54101039朱郁庭

#輸入需要的值
Input=input("Input polynomial: ")
X=int(input("Input the value of X: "))

#建立串列存取輸入的數字與符號
polynomial=[]
number_list=[]
i=0
while i<len(Input):
	#將多項式中的X直接存成輸入的數字
	if Input[i]=="X":
		polynomial+=[X]
	#將連續的數字連接起來，變成多位數的數字
	elif Input[i]>="0" and Input[i]<="9":
		number_list+=[Input[i]]
		#把最後一串數字存入polynomial串列
		if i==len(Input)-1:
			number="".join(number_list)
			polynomial+=[int(number)]
	else:
		#將數字存入polynomial串列
		if number_list!=[]:
			number="".join(number_list)
			polynomial+=[int(number)]
			number_list=[]
		polynomial+=[Input[i]]
	i+=1

#計算次方
j=0
while j<len(polynomial):
	if polynomial[j]=="^":
		a=polynomial[j-1]**polynomial[j+1]
		del polynomial[j-1:j+2]
		polynomial.insert(j-1,a)
	j+=1

#計算乘法
j=0
while j<len(polynomial):
	if polynomial[j]=="*":
		b=polynomial[j-1]*polynomial[j+1]
		del polynomial[j-1:j+2]
		polynomial.insert(j-1,b)
	j+=1

#遇到"-"時將後面的數字乘以-1
j=0
c=0
while j<len(polynomial):
	if polynomial[j]=="‐":
		c=polynomial[j+1]*(-1)
		del polynomial[j:j+2]
		polynomial.insert(j,c)
	j+=1

#將所有數字加起來
j=0
d=0
while j<len(polynomial):
	if polynomial[j]!="+":
		d+=polynomial[j]
	j+=1

#輸出答案
print("Evaluated Result: ",d)
