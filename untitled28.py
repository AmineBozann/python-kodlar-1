# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:13:02 2024

@author: AMİNE BOZAN
"""

# 1’den 100’e kadar 3’e ve 5’e bölünebilen sayıları yazdırın.
for i in range(1,101):
   if i%3==0 and i%5==0:
       print(i)