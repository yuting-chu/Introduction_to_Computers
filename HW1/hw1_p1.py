a = 2 
b = 5 
c = 2 
q = b*b - 4*a*c 
q_sr = q ** (1/2) 
x1 = (-b + q_sr)/(2*a)
x2 = (-b - q_sr)/(2*a)
print("x1= ", x1, "x2= ", x2)