pm=int(raw_input("Consumo promedio "))
cm=int(raw_input("consumo mensua "))
vb=int(raw_input("valor energia "))
va=int(raw_input("valor adicional "))
li=(pm*1.2)
if cm>430 and cm>li:
    p=(cm-li)*va + (li*vb)
else:
    p=vb*li
print p
