
import random
import os
from fractions import Fraction


# GLOBAL

op = 0
con = 0
flag = True
space = ""

menu_flag = True

bucle_paralel = True







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

def validar_rango(txt,min,max):

    flag = True

    while (flag == True):

        num = input(txt)

        try:
            num = int(num)
            if((num <= max) and (num >= min)):
                flag = False
                resul = num
            else:
                print("valor ingresado fuera de rango")

        except ValueError:
            print("valor ingresado no era un valor numerico")
            continue

    return(resul)











while 1:
    os.system("cls")
    menu_flag = True
    
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
    paralela = []
    perpendicular = []

    if op == 1:
        
        while menu_flag == True:

            # PARALELA

            coeficiente_principal = 0
            termino_independiente = 0
            con = 0
            
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


                con = 0


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




                print(perpendicular)
                print (f"""
Funcion :  {coeficiente_principal}x + {termino_independiente}

Funciones paralelas a la dada:
{coeficiente_principal}x + {paralela[0]}
{coeficiente_principal}x + {paralela[1]}
{coeficiente_principal}x + {paralela[2]}

Funciones perpendiculares a la dada:
{negative}x + {perpendicular[0]}
{negative}x + {perpendicular[1]}
{negative}x + {perpendicular[2]}

                            """)
                
                print("""
Seleccione una de las siguientes opciones:

1) Regresar al menu principal.

2) Sacar las paralelas y perpendiculares de otra funcion.

3) Intercambiar decimales por fracciones.

                """)

                op = validar_rango(":     ",1,2)

                match op:
                    case 1:
                        menu_flag = False
                        bucle_paralel = False
                    case 2:
                        bucle_paralel = False
                    case _:
                        print("opcion fuera de rango")
            else:
                space = input("""
El coeficiente principal no puede ser 0.
Precione cualquier tecla para continuar ...
    """)

            