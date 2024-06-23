# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:05:20 2024

@author: AMİNE BOZAN
"""

#Ekrana girilen iki sayının birbirlerine bölünüp bölünmediğini yazsın.
sayi1=int(input('1.sayıyı giriiniz:'))
sayi2=int(input('2.sayıyı giriniz:'))
sonuc=sayi1/sayi2
if sayi1%sayi2==0 or sayi2%sayi1==0:
else:
  print('iki sayı birbirine tam bölünmez. Sonucu=',sonuc)