# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:06:46 2024

@author: AMİNE BOZAN
"""

while True:
  isim = input('isim gir:')
  if isim !='ahmet':
    continue # while koşulunu tekrar kontrol edioyr
  sifre = input('merhaba ahmet şifren nedir?')
  if sifre == '123':
    break
print('giriş onaylandı')