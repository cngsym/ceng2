#!usr/bin/env python
# -*- coding: utf-8 -*-

def en_buyugun_basamagi(sayi):
    sayi = str(sayi)
               
    for i in sayi:
        mx = str(int(max(sayi)))
    if mx == sayi[0]:
        return 'yuzler Basamagi'
            
    elif mx == sayi[1]:
        return 'onlar Basamagi'

    elif mx == sayi[2]:
        return 'birler basamagi'
en_buyugun_basamagi(532)    
              
        
        

      

        
        
