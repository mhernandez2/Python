n=int(raw_input("Numero? "))
x = n / 2
if n%2 == 0 :
	if x%2 == 0 :
		print "es par "+str(n)+" la mitad es "+str(x)+" es par"
	else:
		print "es par "+str(n)+" la mitad es "+str(x)+" es impar"
else:
	if x%2 == 0 :
		print "es impar "+str(n)+" la mitad es "+str(x)+" es par"
	else:
		print "es impar "+str(n)+" la mitad es "+str(x)+" es impar"
