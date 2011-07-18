#!usr/bin/env python
# -*- coding utf8: -*-
def basamaklar_toplami(sayi):
    deger = 0
    while  sayi:
        kalan = sayi % 10
        sayi = sayi / 10
        deger += kalan
    return deger         
   
    
