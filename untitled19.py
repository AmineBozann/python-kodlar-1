# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:10:08 2024

@author: AMİNE BOZAN
"""

from re import T
#Şifresini (123) 3 kere dener ve doğru giremezse çıkış yapsın, doğru
# girerse Hoşgeldiniz desin.

sayac=0
while True :
    sifre=input("şifreniz")
    if(sifre=="123"):
      print("şifreniz doğru")
      break
    else:
      sayac+=1
      print("şifrenizi tekrardan giriniz")
    if(sayac==3):
        print("hakınız bitmiştir")
        break