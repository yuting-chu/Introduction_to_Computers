num=input("Input number list: ")
num=num.split(" ")
a=[]
b=[-1]
print(a,b)
for i in range(len(num)):
	if int(num[i])>b[-1]:
		if b[0]==-1:
			del b[0]
		b+=[int(num[i])]
		print(b)
	else:
		if len(b)>len(a):
			a=b
		elif len(b)==len(a):
			if b[-1]>a[-1]:
				a=b
		b=[int(num[i])]
		print(b)
ans=""
for j in range(len(a)):
	ans+=str(a[j])
	if j!=len(a)-1:
		ans+=" "
print(ans)