#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np

from calculadora import calc

calculo = calc()

def menu():
    print("*******       CALCULADORA       *******")
    print("*  Selecciona una opción:             *")
    print("*  1. Suma                            *")
    print("*  2. Resta                           *")
    print("*  3. Multipliación entre polinomios  *")
    print("*  4. Multiplicación por un escalar   *")
    print("*  5. Evaluación del polinomio        *")
    print("*  0. Salir                           *")
    print("***************************************")
    
    opcion = input("Opción: ")

    try:
        if int(opcion) >= 0 and int(opcion) <= 5:
            return(int(opcion))
        else:
            print("Opción incorrecta, por favor ingrese una opción entre 1 y 5")
            return(int(input("Opción: ")))
    except:
        print("Opción incorrecta, por favor ingrese una opción entre 1 y 5")
        return(int(input("Opción: ")))

while(True):
    opcion = menu()

    if opcion == 0:
        print("Fin")
        break

    else:
        
        num11 = int(input("Ingrese el número de elementos del primer coeficiente: ")) 
        num22 = int(input("Ingresa el número de elementos del segundo coeficiente: "))

        num1 = list(map(int,input("\nIngrese los elementos del primer coeficiente: ").strip().split(',')))[:num11]
        num2 = list(map(int,input("\nIngrese los elementos del segundo coeficiente: ").strip().split(',')))[:num22]

        num1 = np.array(num1)
        num2 = np.array(num2)

        if opcion == 1:
            calculo.suma(num1,num2)
        elif opcion == 2:
            calculo.resta(num1,num2)
        elif opcion == 3:
            calculo.multPolinomio(num1,num2)
        elif opcion == 4:
            calculo.multEscalar(num1,num2)
        elif opcion == 5:
            calculo.evalPolinomio(num1,num2)
        else:
            print("No es posible realizar la operación, por favor ingrese una opción del menú, entre 1 y 5")