# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:02:45 2024

@author: AMİNE BOZAN
"""

#Bir ayın uzunluğu 28 ile 31 gün arasında değişmektedir.
#Kullanıcıdan bir ayın adını soran bir program oluşturunuz
#ve o aydaki gün sayısını ekrana yazdırınız. Artık yılların
#ele alınması için Şubat için "28 veya 29 gün" olarak varsayabilirsiniz.
ay = input("insert month:")
ay=ay.lower()
if ay==("ocak" or "mart" or"temmuz" or "mayıs" or "ağustos" or "ekim" or"aralık"):
  print("31 gün çeker")
elif ay==("şubat"):
  print("28 gün çeker")
else:
  print("30 gün çeker")