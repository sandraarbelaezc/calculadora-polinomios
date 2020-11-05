#!/usr/bin/env python
# -*- coding: utf-8 -*-

class calc:

    def suma(self, x, y):
        '''argumentos de entrada: dos listas, cada una con un polinomio
        retorna: la suma de los dos polinomios
        '''
        may = x
        men = y
        sum = [0]*len(may)
        if len(x) < len(y):
            men = x
            may = y
        sum = [men[i] + may[i] for i in range(len(men))]    
        aux = [may[i] for i in range(len(men),len(may))]
        sum = sum + aux

        print("--------------------------------------------------------------")
        print("El resultado de sumar ", str(x), "+", str(y), " es: ", str(sum))
        print("--------------------------------------------------------------")
    
    def resta(self, x, y):
        '''argumentos de entrada: dos listas, cada una con un polinomio
        retorna: la resta de los dos polinomios
        '''
        may = x
        men = [y[i]*(-1) for i in range(len(y))]
        sum = [0]*len(may)
        if len(x) < len(y):
            men = x
            may = [y[i]*(-1) for i in range(len(y))]
        sum = [men[i] + may[i] for i in range(len(men))]    
        aux = [may[i] for i in range(len(men),len(may))]
        res = sum + aux

        print("--------------------------------------------------------------")
        print("El resultado de restar ", str(x), "-", str(y), " es: ", str(res))
        print("--------------------------------------------------------------")
    
    def multPolinomio(self, x, y):
        '''argumentos de entrada: dos listas, cada una con un polinomio
        retorna: la multiplicación de los dos polinomios
        '''
        p1 = len(x) - 1
        p2 = len(y) - 1
        p_mult = [0]*(p1 + p2 + 1)
        for i in range(len(x)):
            for j in range(len(y)):
                p_mult[i+j] += x[i]*y[j]

        print("------------------------------------------------------------------------------------")
        print("El resultado de multiplicar los polinomios ", str(x), "*", str(y), " es: ", str(p_mult))
        print("------------------------------------------------------------------------------------")
    
    def multEscalar(self, x, y):
        '''argumentos de entrada: dos listas, una con un polinomio y otra con el valor correpsondiente al escalar
        retorna: la multiplicación de un polinomio y un escalar
        '''
        e_mult = [x[i]*(y[0]) for i in range(len(x))]
        print("-----------------------------------------------------------------------------------------------")
        print("El resultado de multiplicar el polinomio y el escalar ", str(x), "*", str(y), " es: ", str(e_mult))
        print("------------------------------------------------------------------------------------------------")
    
    def evalPolinomio(self, x, y):
        '''argumentos de entrada: dos listas, una con un polinomio y otra con el valor correpsondiente al escalar
        retorna: la evaluación de los dos polinomios
        '''
        eval, power = 0, 0
        for coeff in x:
            eval += (y[0]**power) * coeff
            power += 1

        print("--------------------------------------------------------------------------------")
        print("El resultado de evaluar los polinomios ", str(x), "y", str(y), " es: ", str(eval))
        print("--------------------------------------------------------------------------------")