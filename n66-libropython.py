from math import sqrt
n1=float(raw_input("primer numero? "))
n2=float(raw_input("segundo numero? "))
if sqrt(n2) == n1:
	print "el segundo numero es el cuadrado del primero"
else:
	if sqrt(n1) == n2:
		print "el primero es cuadrado del segundo"
	else :
		if sqrt(n2) > n1 :
			print "el segundo es mayor que el cuadrado del primero "
		else:
			if sqrt(n1) > n2 :
				print "el primero es que el cuadrado del segundo "
			else:
				if sqrt(n2)<n1 :
					print "el segundo es menor que el cuadrado del primero "
				else:
					print "el primero es menor que el cuadrado del segundo "
			
