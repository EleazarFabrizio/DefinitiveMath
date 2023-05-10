
import random
import os
from fractions import Fraction


# GLOBAL

op = 0



# PARALELA

coeficiente_principal = 0
termino_independiente = 0








def probar(txt):

    flag = 0

    while (flag == 0):

        num = input(txt)

        try:
            resul = Fraction(num)
            flag = 1

        except ValueError:
            print("valor ingresado no correcto")
            continue

    return(resul)

def validar(txt):

    flag = 0

    while (flag == 0):

        num = input(txt)

        try:
            resul = int(num)
            flag = 1

        except ValueError:
            print("valor ingresado no era un valor numerico")
            continue

    return(resul)











while 1:
    os.system("cls")
    
    print("""

    Bienvenido al programa de resolucion de funciones lineales y cuadraticas.
    ¿En que podemos ayudarle?
    por favor ingrese un

    1) Sacar las Paralelas y Perpendiculares a una Funcion Lineal.

    2) Resolver una Funcion Lineal.

    3) Resolver una Funcion cuadratica.
    
    """)

    op = validar("      :   ")

    os.system("cls")

    if op == 1:
        
        print("""
Perfecto. Vamos a sacar las paralelas y perpendiculares de una Funcion Lineal.

Ax + B

""")
        coeficiente_principal = probar("ingrese el valor principal (A):   ")
        termino_independiente = probar("ingrese el termino independiente (B):  ")

        

        os.system("cls")

