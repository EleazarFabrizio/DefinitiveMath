

import random
import os
from fractions import Fraction
from math import sqrt


# GLOBAL

op = 0
con = 0
flag = True
space = ""

menu_flag = True

bucle_paralel = True



"holi"



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
            
            resul = (Fraction(num))

            flag = False

        except ValueError:
            print("El valor ingresado no es válido. Por favor, vuelva a intentar")
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
            print("valor ingresado no era una opción válida. Por favor, vuelva a intentar")
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
                print("valor ingresado fuera de rango. Por favor, vuelva a intentar")

        except ValueError:
            print("valor ingresado no es válido. Por favor, vuelva a intentar")
            continue

    return(resul)


def creciente_decreciente(tipe,raz,prim):
        
    if tipe == 1:
        if raz > 0:
            print ("La sucesion es creciente. Dado que cada termino es mayor al anterior. a(n) <= a(n+1). d > 0")
        elif raz < 0:
            print ("La sucesion es decreciente. Dado que cada termino es menor al anterior. a(n) >= a(n+1). d < 0")
        else:
            print ("La sucesion es constante. Dado que cada termino es igual al anterior. a(n) = a(n+1). d = 0")

    if tipe == 2:

        if prim >= 0:
            if raz > 1:
                print ("La sucesion es creciente. Dado que el primer termino es positivo y la razon es mayor que 1.")
            elif (0 < raz) and (raz < 1):
                print ("La sucesion es decreciente. Dado que el primer termino es positivo y la razon es menor que 1 y mayor que 0.")
        
        if prim < 0:
            if raz > 1:
                print ("La sucesion es decreciente. Dado que el primer termino es negativo y la razon es mayor que 1.")
            elif (0 < raz) and (raz < 1):
                print ("La sucesion es creciente. Dado que el primer termino es negativo y la razon es menor que 1 y mayor que 0.")

        if raz < 0:
            print("La sucesion es alternada, dado que la razon es menor a 0.")
        if raz == 1:
            print ("La sucesion es constante, dado que la razon es igual a 1.")









while 1:
    os.system("cls")
    menu_flag = True
    
    print("""

Bienvenido al programa de resolución de funciones lineales y cuadráticas.
¿En qué podemos ayudarle?

    por favor ingrese una opción.

    1) Sacar las Paralelas y Perpendiculares a una Función Lineal.

    2) Resolver una Función Lineal.

    3) Resolver una Función cuadrática.

    4) Resolver una sucesión aritmética.

    5) Resolver una sucesion geométrica.
    
    """)

    op = validar_rango("      :   ",1,5)

    os.system("cls")
    

    if op == 1:
        
        while menu_flag == True:

            # PARALELA

            coeficiente_principal = 0
            termino_independiente = 0
            con = 0
            paralela = []
            perpendicular = []
            
            print("""
Perfecto. Vamos a sacar las paralelas y perpendiculares de una Función Lineal.

Ax + B

    """)
            coeficiente_principal = exacto("ingrese el valor principal (A):   ")
            termino_independiente = exacto("ingrese el término independiente (B):  ")

            
            

            os.system("cls")

            if (coeficiente_principal == 0 ):

                

                space = input("""
El coeficiente principal no puede ser 0.
Presione cualquier tecla para continuar ...     
    """)
                os.system("cls")
            else:
                negative = ((1 / coeficiente_principal) * (-1))

                while (con < 3): ### Comienza a sacar las paralelas ###
                    flag = True
            
                    numran = random.randint(-50,50)

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

                    numran = random.randint(-50,50)

                    for i in range (0,len(perpendicular)):
                        if ((numran == perpendicular[i]) or (numran == termino_independiente) or (numran == 0)):
                            flag = False
                    
                    if (numran < 0):
                        numran = "(" + str(numran) + ")"
                            
                    if (flag == True):
                        perpendicular.append(numran)
                        con += 1




                
                print (f"""
Función :  {coeficiente_principal}x + {termino_independiente}

Funciones paralelas a la dada:
{coeficiente_principal}x + {paralela[0]}
{coeficiente_principal}x + {paralela[1]}
{coeficiente_principal}x + {paralela[2]}

Funciones perpendiculares a la dada:
{negative}x + {perpendicular[0]}
{negative}x + {perpendicular[1]}
{negative}x + {perpendicular[2]}

la condición de paralelismo es que el coeficiente principal sea el mismo y el término independiente sea distinto.
La condición de perpendicularidad es que la pendiente debe ser inversa y opuesta, el término independiente puede cambiar o no hacerlo.
                            """)
                
                print("""
Seleccione una de las siguientes opciones:

1) Regresar al menú principal.

2) Sacar las paralelas y perpendiculares de otra función.

                """)

                op = validar_rango(":     ",1,2)

                match op:
                    case 1:
                        menu_flag = False
                        bucle_paralel = False
                    case 2:
                        bucle_paralel = False
                    case _:
                        print("opción fuera de rango")

                os.system("cls")
            

    if op == 2:
        
        while menu_flag == True:

            # LINEAL

            coeficiente_principal = 0
            termino_independiente = 0


            
            print("""
Perfecto. Vamos a resolver una Función lineal.

Ax + B

    """)
            coeficiente_principal = exacto("ingrese el coeficiente principal (A):   ")
            termino_independiente = exacto("ingrese el término independiente (B):  ")

            os.system("cls")

            if (coeficiente_principal == 0 ):

                space = input("""
El coeficiente principal no puede ser 0.
Presione cualquier tecla para continuar ...     
    """)
                os.system("cls")
            else:
                if (coeficiente_principal > 0):
                    tipo_pendiente = "creciente"
                else:
                    tipo_pendiente = "decreciente"

                if (termino_independiente != 0):
                    corte_x = ((termino_independiente *-1) / coeficiente_principal )
                else:
                    corte_x = 0

                os.system("cls")

                print(f"""
Solución de la función dada:
{coeficiente_principal}x + {termino_independiente}

El corte en X es = {corte_x}
El corte en Y es = {termino_independiente}
El comportamiento de la recta es {tipo_pendiente}

Seleccione una de las siguientes opciones:

1) Regresar al menú principal.

2) Sacar las paralelas y perpendiculares de otra función.
""")
                op = validar_rango(":     ",1,2)

                match op:
                    case 1:
                        menu_flag = False
                        bucle_paralel = False
                    case 2:
                        bucle_paralel = False
                    case _:
                        print("opción fuera de rango")


    if op == 3:
        
        while menu_flag == True:
            raices = []
            delta=0
            pendiente = 0
            # CUADRATICA

            valor_pendiente = exacto("Ingrese el coeficiente principal. Siendo ax² + bx + c. Ingrese el valor de a \n :     ")
            valor_lineal = exacto("Ingrese el término lineal. Siendo ax² + bx + c. Ingrese el valor de b \n :    ")
            valor_ordenada = exacto("Ingrese el término independiente. Siendo ax² + bx + c. Ingrese el valor de c \n :   ")
            
            if (valor_pendiente == 0 ):

                space = input("""
El coeficiente principal no puede ser 0.
Presione cualquier tecla para continuar ...     
    """)
                os.system("cls")
            else:

                if(valor_pendiente>0):
                    pendiente = 1
                else:
                    pendiente = -1

                delta = (valor_lineal**2 - 4 * valor_pendiente * valor_ordenada)
                    

                if delta >= 0:

                    raiz = ((valor_lineal * (-1)) + sqrt(delta)) / (2 * valor_pendiente)

                    raices.append(raiz)

                    raiz = ((valor_lineal * (-1)) - sqrt(delta)) / (2 * valor_pendiente)

                    raices.append(raiz)

                    if delta == 0:

                        tipo_raiz = "Las raíces son de doble multiplicidad" #raices doble multiplicidad
                        

                    if delta > 0:

                        tipo_raiz = "Las raíces son Reales" #raices reales

                    if (raices[0]) == raices[1]:
                        tipo_raiz = "Las raíz es una sola."



                if delta < 0:
                    tipo_raiz = "Las raíces son imaginarias/complejas" #no tiene raices reales
                    


                    
                    

                vertice_x = (valor_lineal * -1) / (2 * valor_pendiente)

                vertice_y = valor_pendiente * vertice_x ** 2 + valor_lineal * vertice_x + valor_ordenada


                if valor_lineal < 0:
                    pri_lineal = "(" + str(valor_lineal) + ")"
                else:
                    pri_lineal = valor_lineal
                
                if valor_ordenada < 0:
                    pri_ordenada = "(" + str(valor_ordenada) + ")"
                else:
                    pri_ordenada = valor_ordenada
                

                print (f"""
Solucion a la raíz dada: {valor_pendiente}x² + {pri_lineal}x + {pri_ordenada}

{tipo_raiz}
                    """)
                if delta >= 0:
                    print(f"""
Raíces: X1: {Fraction(raices[0])}     ,       X2: {Fraction(raices[1])}
                """)
                else:
                    print("La parábola no cruza el eje X en ningún punto real.")

                
                print(f"""
El vertice X es:  {vertice_x}
El vertice y es:  {vertice_y}

Coordenadas de vértice: ({vertice_x} ; {vertice_y})
                """)


                if(pendiente==1):
                    intervalo_decrecimiento = "(-∞, " + str(vertice_x) + ")"  
                    intervalo_crecimiento = "(" + str(vertice_x) + ", +∞)"
                    print("El intervalo de decrecimiento es " + intervalo_decrecimiento)
                    print("El intervalo de crecimiento es " + intervalo_crecimiento)

                elif(pendiente==-1):
                    intervalo_crecimiento = "(-∞, " + str(vertice_x) + ")"  
                    intervalo_decrecimiento = "(" + str(vertice_x) + ", +∞)"
                    print("El intervalo de crecimiento es " + intervalo_crecimiento)
                    print("El intervalo de decrecimiento es " + intervalo_decrecimiento)

                if valor_pendiente > 0:
                    print ("La parábola es cóncava para arriba")
                else:
                    print ("La parábola es cóncava para abajo")
                

                print("""
Seleccione una de las siguientes opciones:

1) Regresar al menú principal.

2) Resolver otra función cuadrática.

""")
                op = validar_rango(":     ",1,2)

                match op:
                    case 1:
                        menu_flag = False
                        bucle_paralel = False
                    case 2:
                        bucle_paralel = False
                    case _:
                        print("opción fuera de rango")

                os.system("cls")

    if op == 4:
        while flag == True:
            dif = exacto("Comencemos a resolver sucesiones aritméticas\n\nIngrese la diferencia\n:    ")
            ter = exacto("\nAhora ingrese el primer termino\n:  ")
            fag = True
            while fag == True:
                can = int(exacto("Ingrese la cantidad de términos que desea conocer. El mínimo es 5\n:  "))
                if can < 5:
                    print("Disculpe. el valor ingresado no cumple con la cantidad mínima")
                else:
                    fag = False
            secuencia = [ter]

            for i in range(0,can):
                secuencia.append(secuencia[i]+dif)
            msje=" La Sucesión aritmética es: "
            for i in secuencia:

                msje+= "("+ str(i) + ")"

                if i != secuencia[len(secuencia) - 1]:
                     msje += " - "
            
            print(msje)

            creciente_decreciente(1,dif,ter)
            break

        space = input("Perfecto. Presione cualquier tecla para continuar.")


    if op == 5:
        while flag==True:
            raz = exacto("Comencemos a resolver sucesiones geométrica\n\nIngrese la razón\n:    ")
            ante = exacto("\nAhora ingrese el primer termino\n:  ")
            fag=True
            while fag==True:
                cantidad=int(exacto("Ingrese la cantidad de términos que desea conocer. El mínimo es 5\n:  "))
                if cantidad < 5:
                    print("Disculpe. el valor ingresado no cumple con la cantidad mínima")
                else:
                    fag=False
            secuencia=[ante]
            for i in range(0,cantidad):
                secuencia.append(secuencia[i]*raz)
            msje=" La Sucesión geométrica es: "
            for i in secuencia:

                msje+= "("+ str(i) + ")"

                if i != secuencia[len(secuencia) - 1]:
                     msje += " - "
            print(msje)

            creciente_decreciente(2,raz,ante)
            break

        continuar=input("""

        Presionar enter para continuar""")

        #actu Ivi