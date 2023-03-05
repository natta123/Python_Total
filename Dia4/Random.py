#Ejem de uso de libreria random

from random import *

# Valor entero aleatorio

aleatorio= randint(1,50)
print(aleatorio)

########################################
#Valor decimal aleatorio

aleatorio= uniform(1,50)
print(aleatorio)

########################################

aleatorio= round(uniform(1,50),2)
print(aleatorio)

########################################
#Numero aleatorio entre cero y 1 

aleatorio= random()
print(aleatorio)

########################################
#Elige una opcion aleatoria 

colores= ["azul","rojo","amarillo","verde"]

aleatorio= choice(colores)
print(aleatorio)

########################################
#Mezcla las posibles opciones

numeros=list(range(5,50,5))
shuffle(numeros)
print(numeros)