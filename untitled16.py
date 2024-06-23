# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:09:21 2024

@author: AMİNE BOZAN
"""

#faktöriyel: dışardan girilen bir sayının faktöriyelini hesaplayınız.
# 5! = 5*4*3*2*1

sayi = int(input("Bana bir sayı gir:"))

f = 1
i = 1

while i<sayi +1:
  f *=i
  i += 1
print("Girilen sayının faktöriyeli: ", f)