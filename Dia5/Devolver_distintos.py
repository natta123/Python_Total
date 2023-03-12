"""Ejer. donde ña funcion devolver_distintos 
recibe 3 enteros com paramatro y segun el resultado
de su suma, ejecita distitas condiciones"""

def devolver_distintos(int1,int2,int3):
    suma= int1 + int2 + int3
    lista= [int1,int2,int3]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.remove(max(lista))
        lista.remove(min(lista))
        return lista[0]

num1=10
num2=2
num3=1

print (devolver_distintos(num1,num2,num3))
    
    