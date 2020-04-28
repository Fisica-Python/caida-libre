# -*- coding: utf-8 -*-
#Correr en python3 para evitar problemas de codificación (tildes)
#o usar la codificación anterior.

#Programa para estudiar cuerpos en caída libre

import math
#importamos la librería "math" para algunas funciones como 
#raíz cuadrada

import os
#importamos la librería "os" para limpiar la pantalla

os.system('clear')

#Creamos un Menu

print('''
 CAÍDA LIBRE
 
 1. Determinar el tiempo de caída.
 2. Hallar la posición de un objeto a partir de otros datos.
 3. Conocer la altura máxima de un objeto lanzado hacia arriba.
 4. ¿Desde qué altura se lanza?
 
 ''')
opcion = int(input('''
 Ingrese la opción que desea: 
 '''))
# creamos la variable opcion para determinar
#la incógnita deseada a partir de los datos dados.

os.system('clear') #Limpiamos la pantalla

#Definimos algunas funciones a partir de las ecuaciones
#de posición, velocidad y aceleración del MRUA.
#Estas funciones se utilizarán en todas las opciones.

def pos_vertical(y_0,v_0,t):
 y = h_0 + v_0*t -4.9*(t**2)
 return y

def tiempo_1(v,y):
 t1 = (-v + math.sqrt(v**2-4*(-4.9)*y))/(-9.8)
 return t1
def tiempo_2(v,y):
 t2 = (-v - math.sqrt(v**2-4*(-4.9)*y))/(-9.8)
 return t2

#El próximo bloque 'If' se ejecuta según la opción deseada

if opcion == 1:
 
 print('') #Dejamos un espacio
 print('Determinaremos el tiempo de caída libre a partir  de algunos datos.')
 print('')
 
 h_0 = float(input('Ingrese la altura inicial del cuerpo (en metros): h_0 = ')) #creamos la variable h_0 (es un número real por 
 #eso usamos float)
 v_0 = float(input('Ingrese la velocidad inicial del cuerpo (en m/s) recuerde que será negativa cuando se lance hacia abajo y positiva si se lanza hacia arriba: v_0 = '))
 #creamos la variable v_0

 #a partir de la ecuación de posición: y = h_0 +v_0t -gt²/2 
 #despejamos t igualando y = 0 (pues está en el suelo!)
 #como es una ecuación de segundo grado nos arrojará dos resultados
 #que llamaremos t1 y t2. Descartamos la solución negativa.
 
 t1 = tiempo_1(v_0,h_0)
 t2 = tiempo_2(v_0,h_0)
 print ('El tiempo de caída es: ', round(max(t1, t2),2), ' segundos.')
 
elif opcion == 2:
 print('') #Dejamos un espacio
 print('Podemos conocer la altura de un objeto en determinado tiempo o bien saber en qué momento se encuentra para cierta altura.')
 print('')
 h_0 = float(input('Ingrese la altura inicial del cuerpo (en metros): h_0 = ')) #creamos la variable h_0
 v_0 = float(input('Ingrese la velocidad inicial del cuerpo (en m/s) recuerde que será negativa cuando se lance hacia abajo y positiva si se lanza hacia arriba: v_0 = ')) 
  #creamos la variable v_0
 
 opcion_2 = str(input('¿Qué desea saber? (altura, tiempo): '))
 if opcion_2 == 'altura':
  t = float(input('Ingrese el tiempo en el que desea conocer la altura del objeto (en segundos): '))
  y = pos_vertical(h_0,v_0,t)
  print('La altura del objeto es de ',round(y,2),' metros')
 else:
  y=float(input('Ingrese la altura del cuerpo (en metros), hallaremos el tiempo que demora en llegar hasta allí. y= '))
  if v_0**2-4*(-4.9)*(h_0-y) >=0 : #Es el discriminante de la función
   t1 = round(tiempo_1(v_0,h_0-y),2)
   t2 = round(tiempo_2(v_0,h_0-y),2)
   if t1 == 0:
    print('El cuerpo pasa por la altura y = ',y,' metros en t = ', t2,' segundos.')
   elif t1 >= 0 and t2 == 0 and t2 >=0:
    print('El cuerpo pasa por la altura y = ',y,' metros en los momentos t1 = ', t1,' segundos y t2 = ',t2, ' segundos.')
   else:
    print('Parece que el cuerpo no pasará por allí en ningún momento. Es posible que esa altura supere la altura máxima.')
 
elif opcion == 3:
 
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
 
  h_max=round(pos_vertical(h_0,v_0,t_hmax),2)
  print('El cuerpo alcanza su máxima altura en un tiempo de ', t_hmax,' segundos, y tiene un valor de ', h_max, ' metros.')
 
elif opcion ==4:
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
 
else:
 print('La opción ', opcion, ' no es válida. Adiós.')
