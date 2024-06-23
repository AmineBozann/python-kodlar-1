# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:13:31 2024

@author: AMİNE BOZAN
"""

# KLAVYEDEN GİRİLEN BİR SAYININ ASAL SAYI OLUP OLMADIĞINI
# BULAN PROGRAMI FOR DÖNGÜSÜ İLE YAZINIZ
# ASAL SAYI: 1 VE KENDİSİNDEN BAŞKA TAM BÖLENİ OLMAYAN SAYIDIR
# EN KÜÇÜK ASAL SAYI 2 DİR
asal = True
sayi = int(input("sayı giriniz"))
if  sayi <= 1:
  asal = False
for i in range(2, sayi):
  if sayi % i == 0:
    asal = False
# bu satırdan sonra for döngüsünden çıkılıyor
if  asal == True:
  print("sayı asaldır")
else:
  print("asal değildir")
# Girilen sayı ASAL SAYIDIR
# Girilen sayı ASAL SAYI DEĞİLDİR.