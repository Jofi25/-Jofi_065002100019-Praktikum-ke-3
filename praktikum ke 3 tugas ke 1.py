# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:14:16 2021
Praktikum ke 3

@author: jofi
"""

a = float(input('Masukkan Panjang Sisi A: '))
b = float(input('Masukkan Panjang Sisi B: '))
c = float(input('Masukkan Panjang Sisi C: '))


if a == b == c :
    print('Ini Merupakan Segitiga sama sisi')
    
elif (a + b <= c) or (b + c <= a) or (a + c <= b) :
    print('Ini Bukan Segitiga')
    
elif a == b or a == c or b == c:
    print('Ini Merupakan Segitiga sama kaki')
    
else : 
    print('Ini Merupakan Segitiga Sembarang')
    
