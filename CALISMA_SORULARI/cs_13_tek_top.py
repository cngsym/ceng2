#!usr/bin/env python
# -*- coding utf8: -*-
def tek_toplam(sayi):
    deger = 0
    while sayi:
        kalan = sayi % 10
        sayi = sayi / 10
        
        if kalan % 2 == 0:
            pass
        
        else:
            deger += kalan
    return deger    
              
            
