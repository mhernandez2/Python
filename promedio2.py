suma = 0 
n = 0
x = float(raw_input("promedio "))

while 0 != x :
	suma=suma+x
	n=n+1
	x = float(raw_input("promedio ( 0 = termina programa) "))

p = suma/n
print p
