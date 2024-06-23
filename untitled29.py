# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:13:12 2024

@author: AMİNE BOZAN
"""

# 1’den 1000’e kadar 3’e ve 5’e bölünebilen
# kaç sayı vardır ekrana yazdırın
x=0
for i in range(1,101):
   if i%3==0 and i%5==0:
     x+=1
print(x,"adet 15 e bölünen sayı vardır")
