# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:12:49 2024

@author: AMİNE BOZAN
"""

# klavyeden maaşı girilen 3 Kişinin vergi
# dilimlerine göre ödeyeceği vergi
# //1000 liraya kadar%10 vergi
# //1000 üzerinden %20 vergi
# //10.000 üzerinde %30 vergi
for i in range (1,4):
  maas= int(input(str(i)+".kişinin Maaşınızı giriniz:"))
  if maas<1000:
    print(i,". kişinin vergisi ",maas*0.1 )
  elif 1000<=maas<=10000:
    print(i,". kişinin vergisi ",maas*0.2)
  else:
    print(i,". kişinin vergisi ",maas*0.3)