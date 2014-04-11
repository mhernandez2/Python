# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 10:10:04 2014

@author: Matias Hernandez
"""
Atl1=str(raw_input("Nombre del atleta: "))
Min1=float(raw_input("Ingrese minuto: "))
Se1=float(raw_input("Ingrese segundos: "))
Atl2=str(raw_input("Nombre atleta: "))
Min2=float(raw_input("Ingrese minuto: "))
Se2=float(raw_input("Ingrese segundos: "))
Atl3=str(raw_input("Nombre atleta: "))
Min3=float(raw_input("Ingrese minuto: "))
Se3=float(raw_input("Ingrese segundos: "))
T1 = (Se1/60)+Min1
T2 = (Se2/60)+Min2
T3 = (Se3/60)+Min3
if T1<T2 and T1<T3 :
    if T2<T3 :
        print Atl2, Atl1, Atl3
    else :
        print Atl3, Atl1, Atl2
if T2<T1 and T2<T3 :
    if T1<T3 :
        print Atl1, Atl2, Atl3
    else:
        print Atl3, Atl2, Atl1
if T3<T1 and T3<T2 :
    if T1<T2 :
        print Atl1, Atl3, Atl2
    else:
        print Atl2, Atl3, Atl1
