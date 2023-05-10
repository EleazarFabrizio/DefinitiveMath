
import random
import os
from fractions import Fraction


# GLOBAL

op = 0
con = 0
flag = True
space = ""



# PARALELA

coeficiente_principal = 0
termino_independiente = 0
paralela = []
perpendicular = []








def encajar(txt):

    flag = True

    while (flag == True):

        num = input(txt)

        try:
            resul = round(float(Fraction(num)) , 2)

            flag = False

        except ValueError:
            print("valor ingresado no correcto")
            continue

    return(resul)


def exacto(txt):

    flag = True

    while (flag == True):

        num = input(txt)

        try:
            resul = float(Fraction(num))
            if float.is_integer(resul):
                resul = int(resul)

            flag = False

        except ValueError:
            print("valor ingresado no correcto")
            continue

    return(resul)



def validar(txt):

    flag = True

    while (flag == True):

        num = input(txt)

        try:
            resul = int(num)
            flag = False

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
        coeficiente_principal = exacto("ingrese el valor principal (A):   ")
        termino_independiente = encajar("ingrese el termino independiente (B):  ")

        negative = (1 / coeficiente_principal) * (-1)
        

        os.system("cls")

        if (coeficiente_principal != 0 ):

            while (con < 3): ### Comienza a sacar las paralelas ###
                flag = True
        
                ran = random.randint(-10,10)

                numran = termino_independiente + ran

                for i in range (0,len(paralela)):
                    if ((numran == paralela[i]) or (numran == termino_independiente) or (numran == 0)):
                        flag = False
                
                if (numran < 0):
                    numran = "(" + str(numran) + ")"
                        
                if (flag == True):
                    paralela.append(numran)
                    con += 1





            while (con < 3):
                flag = True

                ran = random.randint(-10,10)
                
                numran = termino_independiente + ran

                for i in range (0,len(perpendicular)):
                    if ((numran == perpendicular[i]) or (numran == termino_independiente) or (numran == 0)):
                        flag = False
                
                if (numran < 0):
                    numran = "(" + str(numran) + ")"
                        
                if (flag == True):
                    perpendicular.append(numran)
                    con += 1





            print (f"""
Funcion :  {coeficiente_principal}x + {termino_independiente}

Funciones paralelas a la dada:
{coeficiente_principal}x + {paralela[0]}
{coeficiente_principal}x + {paralela[1]}
{coeficiente_principal}x + {paralela[2]}

Funciones perpendiculares a la dada:
{negative}x + {paralela[0]}
{negative}x + {paralela[1]}
{negative}x + {paralela[2]}

                        """)
            
            space = input("precione cualquier tecla para continuar: ")
        else:
            space = input("""
El coeficiente principal no puede ser 0.
Precione cualquier tecla para continuar ...
""")

            