cm = int(raw_input("Consumo mensual "))
cp = int(raw_input("comsumo promedio "))
vb = int(raw_input("valor base "))
va = int(raw_input("valor adicional "))
x=(cp*0.2)+cp
if cm>430 :
	if cm>x:
		p = (cm-x)*va + (x*vb)
	else :
		p = cm*vb
else :
	p = cm*vb
print ("Valor total "), p	
