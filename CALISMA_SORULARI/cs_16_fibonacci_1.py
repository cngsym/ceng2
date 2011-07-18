# -*- coding utf8: -*-

def fibonacci_1(sayi):
    if sayi < 2:
        return sayi
    else:
        return fibonacci_1(sayi-1) + fibonacci_1(sayi -2)
    
        
    
