#!/usr/bin/env python
# -*- coding: utf-8 -*-

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