#Ejem. de uso de tuples

mi_tuple=(1,2,3,4)
print(mi_tuple)

##########################

mi_tuple=(1,2,(20,30),4)
print(mi_tuple[2])

##########################
"""Teniendo la misma cantidad de variables
que de elementos del tuple se asignan 1 a 1
(se aplica a diccionarios y listas tambien)"""

t=(1,2,3)
x,y,z=t
print(x,y,z)

##########################

t=(1,2,3,1,1)
print(t.count(1))
print(t.index(3))