# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:09:32 2024

@author: AMİNE BOZAN
"""

sayi = int(input("Bana bir sayı gir:"))
f=1
while sayi>0:
  f*=sayi
  sayi-=1
print('faktöriyel=',f)