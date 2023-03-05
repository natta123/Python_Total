#Ejem. de uso de enumerate

lista= ["a","b","c"]

for item in enumerate(lista):
    print(item)
    
##############################

lista= ["a","b","c"]

for indice, item in enumerate(lista):
    print(indice, item)
    
##############################

lista= ["a","b","c"]

for indice, item in enumerate(range(50,55)):
    print(indice, item)
    
##############################

lista= ["a","b","c"]

mis_tuples= list((lista))

print(mis_tuples)