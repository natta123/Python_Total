#Ejemplo de uso de listas.

mi_lista = ["a","b","c"]
resultado= len(mi_lista)
print(resultado)

##############################

resultado= mi_lista[0]
print(resultado)

##############################

mi_lista2=["d","e","f"]
resultado= mi_lista[0:]
print(mi_lista+mi_lista2)

##############################

mi_lista3= mi_lista + mi_lista2
print(mi_lista3)

##############################

mi_lista3[0]= "alfa"
print(mi_lista3)

##############################

mi_lista3.append("g")
print(mi_lista3)

##############################

mi_lista3.pop()
print(mi_lista3)

##############################

mi_lista3.append("g")
eliinado= mi_lista3.pop()
print(eliinado)

##############################
"""Sort ordena la lista pero
no devuelve ningun dato"""

lista= ["g","o","b","m","c"]
lista.sort()
print(lista)
lista.reverse()
print(lista)

