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
    
    def resta(self, x, y):
        '''argumentos de entrada: dos arrays de 1D, cada uno con un polinomio
        retorna: la resta de los dos polinomios
        '''
        res = P.polysub(x,y)
        print("--------------------------------------------------------------")
        print("El resultado de restar ", str(x), "-", str(y), " es: ", str(res))
        print("--------------------------------------------------------------")
    
    def multPolinomio(self, x, y):
        '''argumentos de entrada: dos arrays de 1D, cada uno con un polinomio
        retorna: la multiplicación de los dos polinomios
        '''
        multP = P.polymul(x,y)
        print("------------------------------------------------------------------------------------")
        print("El resultado de multiplicar los polinomios ", str(x), "*", str(y), " es: ", str(multP))
        print("------------------------------------------------------------------------------------")
    
    def multEscalar(self, x, y):
        '''argumentos de entrada: un arrays de 1D con un polinomio y un escalar
        retorna: la multiplicación de un polinomio y un escalar
        '''
        multE = x*y
        print("-----------------------------------------------------------------------------------------------")
        print("El resultado de multiplicar el polinomio y el escalar ", str(x), "*", str(y), " es: ", str(multE))
        print("------------------------------------------------------------------------------------------------")