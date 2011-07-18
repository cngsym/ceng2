#! usr/bin/env python
# -*- coding utf8: -*-
def digit_5_0 (sayi):
    say = 0
    while sayi:
        kalan = sayi % 10
        sayi =  sayi / 10  
        
        if kalan == 5 or kalan == 0:
            say += 1

    return say        
            
        
