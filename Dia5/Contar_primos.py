"""Efer. de implementacion de una funcion que muestra numeros primos
en un rango de 0 al numero dado como argumento"""


def es_primo (num):
    for n in range(2,num):
        if (num%n)==0:
            return False
    return True



def contar_primo(num2):
    aux=0
    for n in range(2,num2):
        if es_primo(n) == True:
            aux = aux + 1
    return aux

numero= 10

print(contar_primo(numero))