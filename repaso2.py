cp=int(raw_input("consumo promedio"))
cm=int(raw_input("consumo mensual"))
veb=int(raw_input("valor de energia base"))
vea=int(raw_input("valor de energia adicional"))

if cm<=430 : 
    if cp<350:
        li=350
    else:
        li=cp*1.2
        
    
    if cm>li:
        ad=(cm-li)*vea
        vpagar=(cm*veb)+ad
    else:
        vpagar=cm*veb
else:
    vpagar=cm*veb
    
print vpagar
