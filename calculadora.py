#!/usr/bin/env python
# -*- coding: utf-8 -*-
from numpy.polynomial import polynomial as P

class calc:

    def suma(self, x, y):
        '''argumentos de entrada: dos arrays de 1D, cada uno con un polinomio
        retorna: la suma de los dos polinomios
        '''
        sum = P.polyadd(x,y)
        print("--------------------------------------------------------------")
        print("El resultado de sumar ", str(x), "+", str(y), " es: ", str(sum))
        print("--------------------------------------------------------------")