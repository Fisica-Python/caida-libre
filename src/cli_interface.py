import os
import sys
from src import funciones

def generar_menu(lista):
    print()
    num=1
    for elem in lista:
        print("     "+str(num) +". " + elem)
        num+=1
    print()



def print_menu():
    print()
    print("CAÍDA LIBRE")

    lista =["Determinar el tiempo de caída.","Hallar la posición de un objeto a partir de otros datos.",
            "Conocer la altura máxima de un objeto lanzado hacia arriba.","¿Desde qué altura se lanza?",
            "Salir"]
    generar_menu(lista)

def print_numero_invalido():
    print("Oops!  Ese no es un número valido. Intenta de nuevo...")

def select_menu_option():
    valido = False
    while not valido:
        try:
            opcion= int(input('''Ingrese la opción que desea: '''))
            valido=True
        except ValueError:
            print_numero_invalido()
    return opcion


def run():
    salir = False
    while not salir:
        os.system('clear')
        print_menu()
        opcion= select_menu_option()
        action_menu(opcion)

def action_menu(opcion):
    if opcion == 1:
        caso1()
    elif opcion == 2:
        caso2()
    elif opcion == 3:
        caso3()
    elif opcion == 4:
        caso4()
    elif opcion == 5:
        salir()


def caso1():
    print('') #Dejamos un espacio
    print('Determinaremos el tiempo de caída libre a partir  de algunos datos.')
    print('')
    h_0 = float(input('Ingrese la altura inicial del cuerpo (en metros): h_0 = ')) #creamos la variable h_0 (es un número real por
    #eso usamos float)
    v_0 = float(input('Ingrese la velocidad inicial del cuerpo (en m/s) recuerde que será negativa cuando se lance hacia abajo y positiva si se lanza hacia arriba: v_0 = '))
    #creamos la variable v_0

    #usamos la funcion tiempo_caida_libre que se encuentra en funciones.py
    print('El tiempo de caída es: ',funciones.tiempo_caida_libre(v_0,h_0), ' segundos.')
    confirmar_volver_menu()


def caso2():
    print('') #Dejamos un espacio
    print('Podemos conocer la altura de un objeto en determinado tiempo o bien saber en qué momento se encuentra para cierta altura.')
    print('')
    h_0 = float(input('Ingrese la altura inicial del cuerpo (en metros): h_0 = ')) #creamos la variable h_0
    v_0 = float(input('Ingrese la velocidad inicial del cuerpo (en m/s) recuerde que será negativa cuando se lance hacia abajo y positiva si se lanza hacia arriba: v_0 = '))
    #creamos la variable v_0
    opcion_2 = str(input('¿Qué desea saber? (altura, tiempo): '))
    if opcion_2 == 'altura':
        t = float(input('Ingrese el tiempo en el que desea conocer la altura del objeto (en segundos): '))
        y = funciones.pos_vertical(h_0,v_0,t)
        print('La altura del objeto es de ',round(y,2),' metros')
    else:
        y=float(input('Ingrese la altura del cuerpo (en metros), hallaremos el tiempo que demora en llegar hasta allí. y= '))
        if v_0**2-4*(-4.9)*(h_0-y) >=0 : #Es el discriminante de la función
            t1 = round(funciones.tiempo_1(v_0,h_0-y),2)
            t2 = round(funciones.tiempo_2(v_0,h_0-y),2)
            if t1 == 0:
                print('El cuerpo pasa por la altura y = ',y,' metros en t = ', t2,' segundos.')
            elif t1 >= 0 and t2 == 0 and t2 >=0:
                print('El cuerpo pasa por la altura y = ',y,' metros en los momentos t1 = ', t1,' segundos y t2 = ',t2, ' segundos.')
            else:
                print('Parece que el cuerpo no pasará por allí en ningún momento. Es posible que esa altura supere la altura máxima.')
    confirmar_volver_menu()

def caso3():
    print('') #Dejamos un espacio
    print ('Calcularemos la altura máxima que alcanza un objeto lanzado hacia arriba.')
    print('')
    h_0= float(input('Ingrese la altura inicial del cuerpo (en metros): h_0 = ')) #creamos la variable h_0
    v_0=float(input('Ingrese la velocidad inicial del cuerpo (en m/s) recuerde que será negativa cuando se lance hacia abajo y positiva si se lanza hacia arriba: v_0 = ')) #creamos la variable v_0
    if v_0 <= 0:
        print('Si el objeto parte del reposo o es lanzado hacia abajo, la altura máxima será la altura inicial, es decir ', h_0,' metros.')
    else:
        #A partir de la ecuación de la velocidad en función del
        # tiempo ( v = v_0 -g.t) despejamos el tiempo, imponiendo la condición
        # de que la velocidad en la altura máxima es cero. Llamaremos a esta
        # variable t_hmax

        t_hmax=round(v_0/9.8,2)
        #Ahora calculamos la altura máxima(h_max) sustituyendo el tiempo
        # por t_hmax en la función pos_vertical()

        h_max=round(funciones.pos_vertical(h_0,v_0,t_hmax),2)
        print('El cuerpo alcanza su máxima altura en un tiempo de ', t_hmax,' segundos, y tiene un valor de ', h_max, ' metros.')
    confirmar_volver_menu()
def caso4():
    print('') #Dejamos un espacio
    print ('Suponga que se suelta un objeto desde cierta altura, que llamaremos h_0. Vamos a calcularla suponiendo que conocemos el tiempo de caída (t_caída).')
    print('')
    t_caida = float(input('Ingrese el tiempo de caída (en segundos), t_caída= '))#ingresamos la variable t_caida
    #A partir de la ecuación de posición y = h_0 + v_0.t - 1/2.g.t²
    # despejamos h_0 imponiendo la condición y=0.
    if t_caida < 0:
        print('Un valor negativo para el tiempo no tiene mucho sentido en este contexto. Revise sus datos.')
    else:
        h_0 = round(4.9*t_caida**2,2)
    #Como el objeto se suelta (asumimos velocidad inicial 0)
    print('El objeto se suelta desde una altura de ', h_0, ' metros.')
    confirmar_volver_menu()

def salir():
    sys.exit(0)

def confirmar_volver_menu():
    input('Presione enter para volver al menú. ')



