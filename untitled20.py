# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:10:32 2024

@author: AMİNE BOZAN
"""

#ekrana 10 tane rastgele sayı yazdırın. while
import random

i = 0
while i<10:
  i+=1
  rassayi = random.randint(1,100)
  print(rassayi,end=' ')
