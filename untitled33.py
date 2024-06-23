# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:14:07 2024

@author: AMİNE BOZAN
"""

# 1 den başlayarak kullanıcı tarafından klavyeden girilen
# bir sayıya kadar olan tam sayıların toplamını bulan ve
# ekrana yazan Python programını yazınız.
# Örn: Kullanıcı klavyeden 6 sayısını girerse
# 1+2+3+4+5 toplamı sonucunu ekrana yazdırsın.

toplam=0
sayi=int(input("sayi giirniz"))
while(sayi>0):
  toplam+=sayi
  sayi-=1
print("toplam",toplam)