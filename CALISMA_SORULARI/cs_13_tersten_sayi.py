#!usr/bin/env python
# -*- coding utf8: -*-
def tersten_yaz(sayi):
    dizgi = ''
    while sayi:
        kalan = sayi% 10
        sayi = sayi / 10
        dizgi += str(kalan)
    return int(dizgi)   
