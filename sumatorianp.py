n = int(raw_input("ingrese n numeros "))
i = int(raw_input("ingrese limite de suma "))
suma=0
if n>i :
	print "no se efectuara suma n debe ser < que i"
else :
	while n<=i :
		suma+=n
		n+=1
print suma
