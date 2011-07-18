
#!usr/bin/env python
# -*- coding utf8: -*-
def carpim_tablosu_olustur_1( genislik ,deger):
    i = 1
    while i <= genislik:
        print i *deger , 
        i +=1
    
def carpim_tablosu_olustur_2(deger , genislik):
    i = 1
    while i <= deger:
        carpim_tablosu_olustur_1(genislik ,i) 
        i += 1
        print
carpim_tablosu_olustur_2(3,4)
