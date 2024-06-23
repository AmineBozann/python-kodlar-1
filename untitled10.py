# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:07:39 2024

@author: AMİNE BOZAN
"""

sayi = int(input('kontrol edilecek sayıyı girin:'))
for i in range(0,6):
  if i ==sayi:
    break
  print(i,end=' ')
else:
  print('tüm sayılar işlendi')