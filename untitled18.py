# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:09:45 2024

@author: AMİNE BOZAN
"""

#Adını daha sonra soyadını doğru yazana kadar while döngüsünü kullanın.
while True:
  ad = input("adınız")
  if (ad != "yusuf tuna"):
    continue # koşulu tekrar kontrol et
  soyad = input("soyadınız")
  if (soyad == "aksüt"):
    break # döngüden çık
print("ad soyad doğru")
