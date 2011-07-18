#!usr/bin/env python
# -*- coding utf8: -*-
import string
def en_buyuk_sayi(sayi):
    sayi=str(sayi)
    liste = []
    
    for i in range(len(sayi)):
        
        liste.append(sayi[i])
        liste.sort()
        liste.reverse()
        new_liste = string.join(liste ,'')
    return   int(new_liste)

    

