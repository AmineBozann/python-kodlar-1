# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 13:13:42 2024

@author: AMİNE BOZAN
"""

"""Bir string, baştan ve sondan aynı şekilde okunuyorsa
bir palindromdur. Örneğin, «anna», «level» ve «talat»
kelimelerinin tümü palindromik kelimelere örnektir.
Kullanıcıdan bir kelime girmesini
(büyük yada küçük harf girebilir) ve bunun
bir palindrom olup olmadığını kontrol edip
ekrana yazan programı yazınız.
"""
kelime = input("Kelime giriniz")
yenikelime =''
for i in range(len(kelime)-1,-1,-1):
  yenikelime+=kelime[i]

if kelime == yenikelime:
  print("bu kelime bir PALİNDROMDUR")
else:
    print("bu kelime bir PALİNDROM DEĞİLDİR")
