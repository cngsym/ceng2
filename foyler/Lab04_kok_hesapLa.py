#!/usr/bin/env python
# -*- coding: utf8 -*-

import math
def kok_hesapLa(a,b,c):
    if (math.pow(b,2)-(4*a*c))<0:
        print 'Denklemin gercel koku bulunmamaktadir..'

    else:
        birinci_kok =(-b + (math.sqrt(math.pow(b,2) -4*a*c)))/2*a
        ikinci_kok = (-b - (math.sqrt(math.pow(b,2) -4*a*c)))/2*a

        print 'Denklemin birinci koku = ',birinci_kok
        print 'Denklemin ikinci_koku = ', ikinci_kok

        
        
