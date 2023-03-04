#Ejem de uso de sets
"""Los sets no admiten elementos repetidos
ni estan ordenados por indices, tampoco 
diferentes tipos de datos"""

mi_set= set((1,2,3,4,5))
print(type(mi_set))
print(mi_set)

##########################################

otro_set={1,2,3}
print(type(otro_set))
print(otro_set)

##########################################
"""Los sets admiten tuples por que 
son inmutables, y el tuple cumple esta caracteristica"""

mi_set= set((1,2,3,4,5,1,2,3,(1,2,3),1,1,1,1))
print(type(mi_set))
print(mi_set)

##########################################

mi_set= set((1,2,3,4,5))
print(type(mi_set))
print(len(mi_set))
print(2 in mi_set)

##########################################

s1={1,2,3}
s2={3,4,5}
s3=s1.union(s2)
print(s3)

#########################################

s1={1,2,3}
s1.add(4)
s1.add(2)
print(s1)
s1.remove(4)
print(s1)
s1.discard(5)

#########################################

s1.pop()
print(s1)

#########################################

s1={1,2,3}
sorteo= s1.pop()
print(sorteo)

#########################################

s1.clear()
print(s1)


