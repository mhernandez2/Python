# -*- coding: utf-8 -*-
"""
Created on Wed Apr 09 09:53:08 2014

@author: Matias Hernandez
"""

pt1=str(raw_input("Nombre de primera planta: "))
lipt1=int(raw_input("Litros por dias = "))
pt2=str(raw_input("Nombre de segunda planta: "))
lipt2=int(raw_input("Litros por dias = "))
pt3=str(raw_input("Nombre de tercera planta: "))
lipt3=int(raw_input("Litros por dias = "))
if lipt1>lipt2 and lipt1>lipt3 :
    print pt2, pt1, pt3
else :
    if lipt2>lipt1 and lipt2>lipt3 :
        print pt1, pt2, pt3
    else:
        print pt1, pt3, pt2