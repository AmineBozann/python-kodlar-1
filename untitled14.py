# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:08:48 2024

@author: AMİNE BOZAN
"""

#######while döngüsü########
# kullanıcıya “Türkiye’nin başkenti hangi şehirdir?” sorusunu sorsun.
# Doğru cevap verilene kadar “Yanlış cevap, tekrar deneyiniz!”
# uyarısını versin, Doğru cevap verildiğinde
# “Tebrikler, bildiniz” yazısı gösterilsin ve döngüden çıkılsın.
while True:
  sehir =input("türkiyenin başkentini giriniz:").lower()
  if sehir== "ankara":
    print("doğru bildiniz")
    break
  else:
   print("bilemediniz")