"""Ejer. donde se implementa a traves de interaccion 
entre finciones el juego donde se elije un palo y 
pierde el que elige el mas corto. Para esto se deben genrar
las siguientes funciones

-Lista inicial
-Mezclar palitos
-Pedir intento
-Comprobar inteto
"""

from random import shuffle

palitos = ["-","--","---","----"]

def mezclar(lista):
    shuffle(lista)
    return lista

def probar_suerte ():
    intento=""
    
    while intento not in ["1","2","3","4" ]:
        intento= input("Elige un numero del 1 al 4: ")
    return int (intento)

def chequear_intento(lista,intento):
    if lista [intento -1] == "-":
        print("PERDISTEEE")
    else:
        print("Te has salvado")
    print(f"Te ha tocado {lista[intento-1]}")

    
palitos_mezclados= mezclar(palitos)
seleccion= probar_suerte()
chequear_intento(palitos_mezclados,seleccion)

