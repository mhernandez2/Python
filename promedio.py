pn=int(raw_input("ingrese promedio de controles "))
nt=int(raw_input("ingrese la nota de calculo I "))
raw_input("sabiendo que nota promedio es 25% y nota de calculo I es el restante")
x = pn * 0.25
p = nt * 0.75
if (x+p)>=40 :
	print ("tu nota es mayor a 40 "), x+p
else :
	print ("tu nota es menor a 40 "), x+p
