# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:02:38 2024

@author: AMİNE BOZAN
"""

# a harflerinin kaçıncı sıralarda olduğunu bulup ekrana yazdıran
#programı yazın.
# ve bu a harflerini büyük harfe çevirip ekrana yazdıran programı yazın.

#merhaba
kelime = input("5 HARFLİ KELİME: ")
bos = ""
if(kelime[0]== "a"):
  print("1. Karakterde a hharfi var.")
  bos+=kelime[0].upper()
else:
  bos+=kelime[0]
if(kelime[1]== "a"):
  print("2. Kara  kterde a hharfi var.")
  bos+=kelime[1].upper()
else:
  bos+=kelime[1]
if(kelime[2]== "a"):
  print("3. Karakterde a hharfi var.")
  bos+=kelime[2].upper()
else:
  bos+=kelime[2]
if(kelime[3]== "a"):
  print("4. Karakterde a hharfi var.")
  bos+=kelime[3].upper()
else:
  bos+=kelime[3]
if(kelime[4]== "a"):
  print("5. Karakterde a hharfi var.")
  bos+=kelime[4].upper()
else:
  bos+=kelime[4]
print(bos)