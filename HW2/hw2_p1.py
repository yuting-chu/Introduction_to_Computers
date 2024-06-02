thief = 1 
while thief <= 4:
	one=thief!=1
	two=thief==3
	three=thief==4
	four=thief==3
	if int(one)+int(two)+int(three)+int(four)==3: 
		print('The thief is', thief)  
	thief = thief + 1 