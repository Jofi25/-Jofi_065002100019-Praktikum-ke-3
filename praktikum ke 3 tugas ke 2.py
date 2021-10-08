# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 20:14:47 2021
Tugas Laporan Praktikum ke 3 Tugas ke 2

@author: jofi
"""

a = int(input('Masukkan Nilai a : '))
b = int(input('Masukkan Nilai b : '))
c = int(input('Masukkan Nilai c : '))


if b <= 0 :
    print('Persamaan Kuadratnya : ', a, 'x^2 + (', b, ')x +', c)

else : 
    print('Persamaan Kuadratnya : ', a, 'x^2 + (', b, ')x +', c)

which = d = (b * b) - (4 * a * c)
print('Determinannya = ', d)

if (d == 0) and (a != 0) :
    print('Merupakab Akar Kembar')
    

elif d <= 0 :
    print('Merupakan Akar Imajiner')
    
else :
    print('Merupakan Akar Berbeda ')
    
if a == 0 :
    print('Bukan Merupakan Persamaan Kuadrat')
